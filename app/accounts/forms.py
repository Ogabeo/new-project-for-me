from django import forms 
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, EmailInput, PasswordInput
from .models import User
from PIL import Image

class CustomAuthForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'+998972001426'}))
    password=forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))


class UserRegisterForm(forms.ModelForm):
    username=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'admin'}))
    first_name=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'Ogabek'}))
    last_name=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'Toshniyozov'}))
    email=forms.EmailField(widget=EmailInput(attrs={'class':'validate', 'placeholder':'admin@admin.com'}))
    phone=forms.CharField(widget=TextInput(attrs={'placeholder':'+998972001426'}))
    avatar=forms.ImageField()
    password=forms.CharField(widget=PasswordInput(attrs={'placeholder':'password'}))
    confirm_password=forms.CharField(widget=PasswordInput(attrs={'placeholder':'confirm password'}))



    

    class Meta:
        model=User
        
        fields = ('username', 'first_name', 'last_name', 'email', 'phone','avatar' )
    def clean_username(self):
        username=self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Bu username ro'yxatdan o'tgan")
        return username
    
    
    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Parollar bir-biriga mos kelmadi!')
        return confirm_password
    
    def save(self, commit=True):
        user=super().save(commit)
        user.set_password(self.cleaned_data['confirm_password'])
        user.save()
        
    
        img = Image.open(user.avatar.path)
        if img.height>100 or img.width>100:
            new_img=(500, 500)
            img.thumbnail(new_img)
            img.save(user.avatar.path)
        return user  

class UserUpdateForm(forms.ModelForm):
    first_name=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'Ogabek'}))
    last_name=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'Toshniyozov'}))
    email=forms.EmailField(widget=EmailInput(attrs={'class':'validate', 'placeholder':'admin@admin.com'}))
    phone=forms.CharField(widget=TextInput(attrs={'placeholder':'+998972001426'}))
    avatar=forms.ImageField()
    


    class Meta:
        model=User
        fields = ('first_name', 'last_name', 'email', 'phone','avatar' )


    def save(self, commit=True):
        user=super().save(commit)
        user.save()
        img = Image.open(User.avatar.path)
        if img.height>300 or img.width>300:
            new_img=(300, 300)
            img.thumbnail(new_img)
            img.save(User.avatar.path)
        return user
  
