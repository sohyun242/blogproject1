from django.db import models

class Portfolio(models.Model): 
    title = models.CharField(max_length = 255) # 문자열 담은거 
    image = models.ImageField(upload_to='images/') # 이미지 필드에 이미지 담은거 upload는 이미지라는 디렉토리에 넣을겁니다하고 넣은거
    description = models.CharField(max_length=500) # 문자열 담은거

def __str__ (self): 
    return self.title #오브젝트 넘버 말고 타이틀 뜨기 바라는 거니까 title 쓴거