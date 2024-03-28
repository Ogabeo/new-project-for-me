from django.urls import path
from .views import IndexView, ContactUs, Aboutt, detail, category_list, NewCreateView, NewUpdateView, DeleteView, deletepage, SearchView

app_name="home"

urlpatterns=[

    path("", IndexView.as_view(), name="home"),
    path("contact/", ContactUs.as_view(), name="contact"),
    path('about/', Aboutt.as_view(), name="about"),
    path("detail/<int:id>/", detail.as_view(), name="detail") ,
    path("category_list/<int:id>/", category_list.as_view() , name="category_list") ,
    path("newcreate/", NewCreateView.as_view(), name="newcreate"),
    path("newupdate/<int:id>/", NewUpdateView.as_view(), name="newupdate"),
    path('delete/<int:id>/', DeleteView.as_view(), name='delete'),
    path('deletewarning/<int:id>/', deletepage.as_view(), name='warning_delete'),
    path('search/', SearchView.as_view(), name='search')
    

    

]



