# tweet/models.py
from django.db import models
from user.models import UserModel  # user앱의 models 을 가져와 사용할건데 이름이 UserModel인 애를 가져오겠다


# Create your models here.
class TweetModel(models.Model):
    class Meta:
        db_table = "tweet"

    author = models.ForeignKey(
        UserModel, on_delete=models.CASCADE
    )  # ForeignKey : 다른 데이터베이스에서 내용을 가져오겠다 ( 다른 모델 가져와서 넣어놓겠다)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
