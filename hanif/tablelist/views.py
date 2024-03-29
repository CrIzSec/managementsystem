from django.shortcuts import render

# Create your views here.
def tablelist(request):
    return render(request, 'tablelist.html')