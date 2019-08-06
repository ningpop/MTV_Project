from django.shortcuts import render, redirect
from review.models import Review
from django.utils import timezone

# Create your views here.

def home(request):
    reviews = Review.objects.all
    return render(request,'home.html',{"reviews":reviews})

def air(request):
    return render(request,'air.html')

def act(request):
    return render(request,'act.html')

def lodge(request):
    return render(request,'lodge.html')

def pak(request):
    return render(request,'pak.html')

def trans(request):
    return render(request,'trans.html')

def new(request):
    return render(request,'new.html')

def create(request):
    # 여기서 글을 DB에 저장
    title = request.GET["title"]
    body = request.GET["body"]
    review = Review()
    review.title = title
    review.body = body
    review.pub_date = timezone.now()
    review.save()
    return redirect('home')
