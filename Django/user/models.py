from django.db import models
import re

# 이름, 비번, 상태메세지, 생성일, 수정일 클래스에 넣기
class UserModel(models.Model):
    class Meta:
        db_table = "my_user"
        # DB 테이블의 이름 : my_user

    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)
    bio = models.CharField(max_length=256, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# 타임어택 2.
class UserClass:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def greeting(self):
        print(self.email)
        print(self.password)

    def is_email_valid(email):
        REGEX_EMAIL = email
        if not re.fullmatch(REGEX_EMAIL, email):
            return "이메일 형식을 확인하세요."
        else:
            pass

    def is_password_valid(password):
        if not len(password) > 8:
            return "비밀번호는 8글자 이상 입력해주세요."
        else:
            pass


# gh = UserClass("soiyosauce@gmail.com", "0000password")
# gh.greeting()
