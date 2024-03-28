from django.db import models
from app.accounts.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
# Create your models here.

class BaseModel(models.Model):
    created_At=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)


    class Meta:
        abstract=True
    
    
class Category(BaseModel):
    name=models.CharField(max_length = 50)
    slug = models.SlugField(verbose_name="slug")

    def __str__(self):
        return self.name
    
class Tags(BaseModel):
    name=models.CharField(max_length = 50)
    def __str__(self):
        return self.name
class New(BaseModel):
    image=models.ImageField(upload_to = "news_images/")
    slug=models.SlugField(null=True, unique=True, verbose_name="slug")
    title = models.CharField(max_length = 255)
    body=RichTextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_new")
    views=models.IntegerField(default = 0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name="category_news")
    tags=models.ManyToManyField(Tags, blank=True)

    def __str__(self):
        return f"{self.author} - {self.title}"
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True )
        return super().save(*args, **kwargs)
    
class About(BaseModel):
    linkedin=models.CharField(max_length=100)
    twitter=models.CharField(max_length=100)
    facebook=models.CharField(max_length=100)
    instagram=models.CharField(max_length=100)
    youtube=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=450)
    phone=models.CharField(max_length=17) 

    def __str__(self):
        return "About"
     

class Contact(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    
    def __str__(self):
        return self.name
    
class Ads(BaseModel):
    image=models.ImageField(upload_to = "adss_images/")
    link=models.CharField(max_length=150)
    choices_new= (
        ("one", "ONE"),
        ("two", "TWO"),
    )
    position = models.CharField( max_length=5, choices=choices_new )





