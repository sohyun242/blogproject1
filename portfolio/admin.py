from django.contrib import admin
from .models import Portfolio
#마이그레이션한 데이터를 등록해주는 곳

admin.site.register(Portfolio)