from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    result = render(request, "landing/payload.html")

    return HttpResponse(result)
