from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, "html/test.html")

def faqs(request):
    return render(request, "html/faqs.html")