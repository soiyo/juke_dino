from django.http import HttpResponse
from django.shortcuts import render


def base_response(request):
    return HttpResponse("안녕하세요! 장고의 시작입니다!")


# 타임어택 1.
def first_view(request):
    return render(request, "index.html")
