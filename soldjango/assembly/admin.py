from django.contrib import admin
from .models import Member

# Register your models here.
admin.site.register(Member) #member라는 모델을 내 site에 등록하겠다는 의미
