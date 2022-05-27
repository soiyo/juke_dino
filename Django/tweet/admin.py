from django.contrib import admin
from .models import TweetModel

# Register your models here.
admin.site.register(TweetModel)  # 트윗모델을 어드민페이지에 적용해주겠다
