from django.shortcuts import render,redirect
import qrcode
from io import BytesIO
import base64
from django.core.mail import send_mail
from django.conf import settings


def shorten_view(request):
        return render(request, 'basehome/landingpage.html')

def about(request):
        return render(request, 'basehome/about.html')

def service(request):
        return render(request, 'basehome/service.html')


def contact(request):
        return render(request, 'basehome/contact.html')


def contact_submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        # Compose the email content
        email_subject = f"Contact Form Submission: {subject}"
        email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        
        # Send email
        send_mail(
            email_subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],  # Send to your email
            fail_silently=False,
        )
        return redirect('contact')
    return render(request, 'contact.html')



def landingpage(request):
    return render(request, 'basehome/landingpage.html') 


def api_documentation(request):
    return render(request, 'api/api_documentation.html')            

#function to generate qr code
def generate_qr_code(url):
    img = qrcode.make(url)
    img_io = BytesIO()
    img.save(img_io, 'JPEG')
    img_bytes = img_io.getvalue()
    img_base64 = base64.b64encode(img_bytes)
    img_base64_str = img_base64.decode('utf-8')
    return img_base64_str



