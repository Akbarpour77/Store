from django.shortcuts import render
from .models import Mobiles, Sabadekharid
from django.views.generic import View
from .forms import Product_list
import simplejson


# Create your views here.

class Mobile(View):

    def get(self, request):
        product = Product_list()
        brand = Mobiles.objects.values('brand', 'price', 'quantity', 'idnumber')
        context = Mobiles.objects.all()
        all = zip(context, brand)
        return render(request, 'mobiles.html', {'mobiles': all, 'product': product})

    def post(self, request):
        brand = request.POST.get('brand.brand')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        id = request.POST.get('idnumber')

        sabad = Sabadekharid(price=price, brand=brand)
        sabad.save()
        allsabad = Sabadekharid.objects.all()

        total = Sabadekharid.Aggregate()
        allsabad.totalprice = total
        allsabad.save(update_fields=['totalprice'])

        mobile = Mobiles(idnumber=id, price=price, brand=brand, quantity=quantity - 1)
        mobile.save()
