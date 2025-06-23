from django.shortcuts import render
from list_of_helps.models import HelpList, PromoBlock, BannerBlock, SponsorBlock, OrderBlock, ProductBlock, ProductBlock2, ProductBlock3, ProductBlock4

def index(request):
    list = HelpList.objects.all()
    promo = PromoBlock.objects.all()
    banner = BannerBlock.objects.all()
    sponsor = SponsorBlock.objects.all()
    return render(request, 'index.html', {'list': list, 'promo': promo, 'banner': banner, 'sponsor': sponsor})

def subscribe_view(request):
    order = OrderBlock.objects.all()
    return render(request, 'subscribe.html', {'order': order})

def product_detail(request):
    product = ProductBlock.objects.all()
    return render(request, 'product.html', {'product': product})

def product_detail2(request):
    product2 = ProductBlock2.objects.all()
    return render(request, 'product2.html', {'product2': product2})

def product_detail3(request):
    product3 = ProductBlock3.objects.all()
    return render(request, 'product3.html', {'product3': product3})

def product_detail4(request):
    product4 = ProductBlock4.objects.all()
    return render(request, 'product4.html', {'product4': product4})
# Create your views here.
