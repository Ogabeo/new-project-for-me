from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import About, Contact, New, Category, Tags
from django.contrib import messages
from .forms import NewCreateForm
from django.db.models import Q
from itertools import chain

# Create your views here.


class IndexView(View):
    def get(self, request):
        news=New.objects.all().order_by('?')[:5]
        advertise_news=New.objects.all().order_by("?")[:3]
        sport=New.objects.filter(category__name="Sports")
        tech_news=New.objects.filter(category__name="Technology")
        global_news=New.objects.filter(category__name="Jahon Yangiliklari")
        entertainment=New.objects.filter(category__name="entertainment")
        kundalik=New.objects.filter(category__name="Kundalik Hayot")
        business=New.objects.filter(category__name="Business")
        lastest_news=New.objects.all().order_by("-id")[:4]
        famous_news=New.objects.all().order_by("-views")[:6]

        



        context={  
            "lastest_news":news,
            "sports":sport,
            "technology":tech_news,
            "global_news":global_news,
            "entertainment":entertainment,
            "kundalik":kundalik,
            "business":business,
            "songiyangiliklar":lastest_news,
            "advertise":advertise_news,
            "famous":famous_news

        }
        return render(request, "index.html", context )




class Aboutt(View):
    
    
    def get(self, request):
        data=About.objects.all()
        context={
        "data":data
    }
        return render(request, "detail.html", context)
    

class detail(View):
    def get(self, request, id):
        data=New.objects.get(id=id)
        data.views+=1
        data.save()
        context={
            "data":data
        }
        return render(request, "detail.html", context)
    

class category_list(View):
    def get(self, request, id):
        ctg=Category.objects.get(id=id)
        categorynew= ctg.category_news.all()

        context={
            "categorynew":categorynew
        }
        return render(request, 'category_news.html', context)
    

class ContactUs(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        data=request.POST

        contact=Contact()


        contact.name=data.get('name')
        contact.email=data.get('email')
        contact.subject=data.get('subject')
        contact.message=data.get('message')
        contact.save()


        
        return render(request, 'contact.html')


class NewCreateView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form= NewCreateForm()
            return render(request, "new_create.html", {"form":form})
        messages.error(request, "Please log in before creating new post...")
        return redirect("accounts:login")
    def post(self, request):
        form = NewCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new=form.save(commit=False)
            new.author = request.user
            new.save()
            messages.success(request, "Yangilik yaratildi...")
            return redirect("home:home")
        messages.warning(request, "Yangilik yaratilmadi...")
        return render(request, "new_create.html", {"form":form}) 


class NewUpdateView(View):
  
    def get(self, request, id):
        new = get_object_or_404(New, id=id)
        if request.user.is_authenticated and  request.user == new.author:
            form = NewCreateForm(instance=new)
            return render(request, 'new_update.html', {'form':form})
        messages.error(request, 'You are not allowed to edit...')
        return redirect('home:home')
    def post(self, request, id):
        new = get_object_or_404(New, id= id)
        form= NewCreateForm(data=request.POST, files=request.FILES, instance=new)
        if form.is_valid():
            new=form.save(commit=False)
            new.author= request.user
            new.save()
            messages.success(request, 'Post was successfully updated...')
            return redirect('home:home')
        messages.error(request, "Oops, New was not updated...")
        return render(request, 'new_update.html', {'form':form})
    
        
class DeleteView(View):
    def get(self, request, id):
        new = get_object_or_404(New, id=id)
        if request.user.is_authenticated and request.user == new.author:
            new.delete()
            messages.success(request, "Post was successfully deleted...")
            return redirect('home:home')
        messages.error(request, 'You are not allowed to delete this post...')
        return redirect('home:home')
    
class deletepage(View):
    def get(self, request, id):
        data = get_object_or_404(New, id=id)
        return render(request, 'deletenew.html', {'data' : data}) 
    
class SearchView(View):
    def get(self, request):
        query=request.GET.get('query')
        if not query:
            news = New.objects.all()
        
        news = New.objects.all().filter( Q(title__icontains = query) | Q(body__icontains = query))
        # tag=get_object_or_404(Tags, name=query)
        # tag_news= tag.new_set.all()
        # result_list = list(chain(tag_news, news))
        context={
            "searchnews":news
            # "searchnews":result_list
        }
        return render(request, 'search.html', context )
