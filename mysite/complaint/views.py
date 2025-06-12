from django.shortcuts import render, redirect
from .forms import ComplaintForm
from .models import Complaint

def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            complaint = form.save()
            return render(request, 'complaint/popup_redirect.html', {
                'tracking_code': complaint.tracking_code
            })

    else:
        form = ComplaintForm()
    return render(request, 'complaint/submit.html', {'form': form})

def track_complaint(request):
    code = request.GET.get('code')
    complaint = Complaint.objects.filter(tracking_code=code.upper()).first() if code else None
    return render(request, 'complaint/track.html', {'complaint': complaint, 'code': code})
