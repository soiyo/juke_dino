from django.shortcuts import render, redirect
from .models import UserModel, UserClass
from django.http import HttpResponse


# Create your views here.
def sign_up_view(request):
    if request.method == "GET":
        return render(request, "user/signup.html")  # 페이지 보여주기
    elif request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        password2 = request.POST.get("password2", None)  # request.POST에서 가져오기
        bio = request.POST.get("bio", None)

        if password != password2:
            return render(request, "user/signup.html")  # 회원가입화면 다시 보여줌
        else:
            exist_user = UserModel.objects.filter(username=username)
            if exist_user:
                return render(request, "user/signup.html")
            else:
                new_user = UserModel()
                new_user.username = username
                new_user.password = password
                new_user.bio = bio
                new_user.save()  # DB에 저장
                return redirect("/sign-in")  # 회원가입 완료시에만 실행됨


def sign_in_view(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        me = UserModel.objects.get(username=username)
        # me = 모델Username = Post에서 불러온 username
        if me.password == password:
            request.session["user"] = me.username
            return HttpResponse("로그인 성공! 사용자 이름은 : " + me.username)
        else:
            return redirect("/sign-in")
    elif request.method == "GET":
        return render(request, "user/signin.html")


# 타임어택3.
def sign_up_view_2(request):
    if request.method == "GET":
        return render(request, "user/register.html")  # 페이지 보여주기
    elif request.method == "POST":
        email = request.POST.get("email", None)
        email_2 = UserClass.objects.get("email", None)
        password = request.POST.get("password", None)
        password_2 = UserClass.objects.get("password", None)

        if password != password_2:
            return HttpResponse("비밀번호 길이 에러")
        elif email != email_2:
            return HttpResponse("이메일 형식에러!")
        else:
            return HttpResponse("회원 가입 완료!")
