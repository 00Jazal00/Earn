from django.shortcuts import render, redirect
from .models import Join_User
# Create your views here.
def Home(request):
    return render(request, 'index.html')

def Join_us(request):
    if request.method == "POST":
        username = request.POST['username']
        gender = request.POST['gender']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        qualification = request.POST['qualification']
        qualification = request.POST['qualification']
        experience = request.POST['experience']
        location = request.POST['location']
        Join_User(username=username, gender=gender, email=email, mobile_number=mobile_number, qualification=qualification, experience=experience, location=location).save()
        return redirect('/thanks_for_join/')
    return render(request, 'join.html')
    
def Thanks_for_join(request):
    return render(request, 'welcome.html')