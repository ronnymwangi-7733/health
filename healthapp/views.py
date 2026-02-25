from django.shortcuts import render

# Create your views here.
from healthapp.models import *
def home(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')


def about(request):
    return render(request, 'about.html')

def appointment(request):

    if request.method == 'POST':

        all = Myappointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            datetime = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message'],
        )
        all.save()
        return render(request, 'appointment.html')

    else:
        return render(request, 'appointment.html')


def show(request):
    allappointment = Myappointment.objects.all()
    return render(request, 'show.html', {'allappointment': allappointment})

