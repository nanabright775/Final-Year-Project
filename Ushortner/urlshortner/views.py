from django.shortcuts import render
from user_agents import parse as ua_parse
import qrcode
from io import BytesIO
import base64
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import ShortURL
import uuid
from django.http import HttpResponsePermanentRedirect
from .models import ShortURL, Click
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect



def shorten_view(request):
    if request.method == 'POST':
        original_url = request.POST['url']
        if ShortURL.objects.filter(original_url=original_url).exists():
            short_code = ShortURL.objects.get(original_url=original_url).short_code
            qr_code = generate_qr_code(request.build_absolute_uri(f'/{short_code}'))
            return render(request, 'basehome/homepage.html', {'original_url': original_url, 'short_code': short_code, 'qr_code': qr_code})
            # return render(request, 'shorten.html', {'original\_url': original_url, 'short\_code': short_code})

        else:
            short_code = str(uuid.uuid4())[:10]
            ShortURL.objects.create(original_url=original_url, short_code=short_code)
            short_url = request.build_absolute_uri(f'/{short_code}')
            qr_code = generate_qr_code(request.build_absolute_uri(f'/{short_code}'))
            return render(request, 'basehome/homepage.html', {'original_url': original_url, 'short_code': short_code, 'qr_code': qr_code})
            return HttpResponseRedirect(f'/{short_code}')
        
    else:
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



