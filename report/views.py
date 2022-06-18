from django.shortcuts import render

# Create your views here.
def report(request):
    return render(request, "html/report.html")
def report_test(request):
    return render(request, "html/report-generation.html")