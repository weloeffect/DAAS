from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "html/homepage.html")
def home1(request):
    return render(request, "html/homepage.html")

def test2(request):
      return render(request, "html/test2.html")