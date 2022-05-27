from django.contrib import admin  # 어드민 툴을 장고에서 사용하겠다
from .models import UserModel  # 우리가 생성한  UserModel 모델(동일경로에서) 가져옴

# Register your models here.
admin.site.register(UserModel)  # UserModel을 Admin(관리자페이지)에 추가 해 줍니다
