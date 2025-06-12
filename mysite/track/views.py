from django.shortcuts import render

def track_home(request):
    return render(request, 'track/track_home.html')
