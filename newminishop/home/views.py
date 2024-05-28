from django.shortcuts import render,get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def home (request,c_slug=None):
    pagi=product.objects.order_by('id')
    paginator=Paginator(pagi,5)
    page=request.GET.get('page')
  #  paginated==paginator.get_page(page)




    if c_slug!=None:
        c_page=get_object_or_404(cate,slug=c_slug)
        pro=product.objects.filter(category=c_page,available=True)
    else:
        pro=product.objects.all().filter(available=True)
    catr=cate.objects.all()

    return render(request,'index.html',{'j':catr,'p':pro})


def about(request):
    return render(request,'about.html')

def details(request,c_slug,product_slug):
    pro =get_object_or_404(product,category__slug=c_slug,slug=product_slug)
    return render(request,'product-single.html',{'pro':pro})  #to render a html file

def search(request):
    if 'q' in request.GET:
        query =request.GET.get('q')
        pro=product.objects.all().filter(Q(name__icontains=query)|Q(desc__icontains=query),available=True)
    return render(request,'search.html',{'pr':pro})

