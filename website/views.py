from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render (request, 'home.html', {})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['your-message']

        #send function is populated by the details of the customers
        send_mail(message,email, subject, ['encychar@gmail.com'])


        return render (request, 'contact.html', {'name': name, 'message': message, 'subject': subject})




    else:
        return render(request, 'contact.html', {})










def gallery(request):
    return render (request,'gallery.html', {})