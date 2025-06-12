from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from complaint.models import Complaint

def is_superuser(user):
    return user.is_superuser

def admin_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect("admin_dashboard")
        else:
            return render(request, "adminportal/login.html", {"error": "Invalid credentials or not an admin."})
    return render(request, "adminportal/login.html")

@login_required
@user_passes_test(is_superuser)
def dashboard(request):
    complaints = Complaint.objects.all().order_by('-submitted_at')
    return render(request, "adminportal/dashboard.html", {"complaints": complaints})

@login_required
@user_passes_test(is_superuser)
def update_status(request, complaint_id):
    if request.method == "POST":
        new_status = request.POST.get("status")
        complaint = get_object_or_404(Complaint, id=complaint_id)
        complaint.status = new_status
        complaint.save()
    return redirect("admin_dashboard")

@login_required
@user_passes_test(is_superuser)
def delete_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    complaint.delete()
    return redirect("admin_dashboard")

def admin_logout(request):
    logout(request)
    return redirect("home")
