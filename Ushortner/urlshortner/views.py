from django.shortcuts import render
import qrcode
from io import BytesIO
import base64
from django.shortcuts import render



def shorten_view(request):
        return render(request, 'basehome/homepage.html')
              

#function to generate qr code
def generate_qr_code(url):
    img = qrcode.make(url)
    img_io = BytesIO()
    img.save(img_io, 'JPEG')
    img_bytes = img_io.getvalue()
    img_base64 = base64.b64encode(img_bytes)
    img_base64_str = img_base64.decode('utf-8')
    return img_base64_str



