from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
from .models import Commentary
# Create your views here.
def view(request):
    return render(request, "html/commentary.html")
# def test(request):
#     return render(request, "html/homepage.html")
def insert_comment(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        comment = request.POST['comment']
        com = Commentary(first_name=first_name, last_name=last_name, email=email, comment=comment)
        com.save()
        # return HttpResponse("Data saved")
        return render(request, "html/success.html")
    else:
        return render(request, "html/commentary.html")
