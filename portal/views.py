import requests
from django.shortcuts import render, get_object_or_404
from .models import news
from django.utils import timezone

#from .models import City
#from .forms import CityName

def portal(request):
    posts = news.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'portal/portal.html', {'posts': posts})     

def post_detail(request, pk):
    post = get_object_or_404(news, pk=pk)
    return render(request, 'portal/post_detail.html', {'post': post})