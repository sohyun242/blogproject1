from django.shortcuts import render
from .models import Portfolio

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios':portfolios})

    #우리가 데이터베이스에 있는 객체를 모두 가지고 와라
    
