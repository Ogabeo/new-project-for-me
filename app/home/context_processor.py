
from .models import Category, Tags, About, Ads

def index_processor(request):
    kategoriyalar=Category.objects.all()
    tags=Tags.objects.all()[:20]
    about=About.objects.all().first()
    ads_one=Ads.objects.all().filter(position="one", is_active="True").order_by("?").first()
    ads_two=Ads.objects.all().filter(position="two", is_active=True).order_by("?")[:2]




    context={
        
        "kategoriyalar":kategoriyalar,
        "tags":tags,
        "about":about,
        "ads_one":ads_one,
        "ads_two":ads_two,

    }
    return context
