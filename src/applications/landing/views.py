from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    result = render(request, "landing/_base.html")

    return HttpResponse(result)
