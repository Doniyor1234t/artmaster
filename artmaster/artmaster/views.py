from django.shortcuts import render 
from adminka.models import Arts, Frames


def home(request):
    return render(request, 'home.html')

def frame(request):
    data = {"Frames": Frames.objects.all().order_by('-id')}
    return render(request, 'frame.html', data)

def picture(request):
    data = {"Arts": Arts.objects.all().order_by('-id')}
    return render(request, 'picture.html',data)

def shop(request):
    return render(request, 'shop.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def page_not_found_view(request, exception):
    return render(request, 'notfound.html', status=404)

def page_frame(request, frameId):
    return render(request, 'tabframe.html' )