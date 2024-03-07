from django.shortcuts import render, redirect
from mysite.models import Post, Product
from django.http import HttpResponse, Http404
from datetime import datetime
import random

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, "index.html", locals()) # locals() 將打包區域變數到一個dict

def showpost(request, slug):
    
    post = Post.objects.get(slug = slug)
    if post != None:
        return render(request, 'post.html', locals())
    
def index(request):
    quotes = ['今日事，今日畢',
            '要怎麼收穫，先那麼栽',
            '知識就是力量',
            '一個人的個性就是他的命運']
    quote = random.choice(quotes)
    return render(request, 'about.html', locals())

def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')
    return render(request, 'disp.html', locals())