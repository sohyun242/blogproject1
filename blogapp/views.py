from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects #쿼리셋
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id)) # 함수들 다 처리하고 이 url로 이동하세요라는 뜻
    #blog.id는 인트형인데 str은 문자열이니까 문자열로 변환시켜준거 그래서 str(blog.id)써준거

def cover(request):
    return render(request, 'cover.html')

def one(request):
    return render(request, 'one.html')