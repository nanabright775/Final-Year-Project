from django.shortcuts import render
from .forms import URLForm
import joblib
import tldextract


# Load the trained model
model = joblib.load('detect/url_detector_model.pkl')


def detect_link(request):
    result = None
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            ext = tldextract.extract(url)
            url_features = f"{ext.domain}.{ext.suffix}"
            result = model.predict([url_features])[0]
    else:
        form = URLForm()
    return render(request, 'detect/detect_link.html', {'form': form, 'result': result})
