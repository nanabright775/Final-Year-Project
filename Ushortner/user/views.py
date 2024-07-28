from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from urlshortner.models import ShortURL
import uuid
from urlshortner.views import generate_qr_code
from urlshortner.models import ShortURL, Click
from user.forms import CustomShortURLForm, GenerateQRCodeForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db.models import Q 
from django.utils.dateparse import parse_date
from django.db.models import Count
import json
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.conf import settings
from django.db.models import Count
from datetime import datetime

#signup view for a user
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        errors = []

        if not username or not email or not first_name or not last_name or not password1 or not password2:
            errors.append("All fields are required.")
        if password1 != password2:
            errors.append("Passwords do not match.")
        if User.objects.filter(username=username).exists():
            errors.append("Username already exists.")
        if User.objects.filter(email=email).exists():
            errors.append("Email already exists.")
        
        if not errors:
            user = User.objects.create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=make_password(password1)
            )
            user.backend = f'{settings.AUTHENTICATION_BACKENDS[0]}'
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard')) 

        else:
            for error in errors:
                messages.error(request, error)
            return render(request, 'user/signup.html', {'errors': errors})
    
    return render(request, 'user/signup.html')


#logging in view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        errors = []

        if not username or not password:
            errors.append("All fields are required.")

        if not errors:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user) 
                # return redirect(request, 'dashboard_view')
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                errors.append("Incorrect username or password.")
        else:
            errors.append("Incorrect username or password.")

        for error in errors:
            messages.error(request, error)
        
        return render(request, 'user/login.html', {'errors': errors})
    return render(request, 'user/login.html')

#views for creating a short urls using the random method
@login_required
def user_dashboard(request):
    """View function for displaying the user dashboard page."""
    user_short_urls = ShortURL.objects.filter(user=request.user).order_by('-date_created')
    short_code = None  
    qr_code = None 

    if request.method == 'POST':
        original_url = request.POST['url']
        if ShortURL.objects.filter(original_url=original_url).exists():
            short_url = ShortURL.objects.get(original_url=original_url)
            short_code = short_url.short_code
            qr_code = generate_qr_code(request.build_absolute_uri(f'/{short_code}'))
        else:
            short_code = str(uuid.uuid4())[:5]
            short_url = ShortURL.objects.create(original_url=original_url, short_code=short_code, qr_code_data = generate_qr_code(original_url), user=request.user)
            qr_code = generate_qr_code(request.build_absolute_uri(f'/{short_code}'))
            short_url.save()
        short_code = request.build_absolute_uri(f'/{short_code}')

    context = {
        'user_short_urls': user_short_urls,
        'short_code': short_code,
        'qr_code': qr_code,

    }
    if 'original_url' in locals():  # Check if 'original_url' is defined
        context['original_url'] = original_url
    return render(request, 'user/userdashboard.html', context)


#logging out view
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


def redirect_view(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    
    # Extract user agent and IP address
    user_agent_string = request.META.get('HTTP_USER_AGENT', '')
    referer = request.META.get('HTTP_REFERER', '')
    ip_address = request.META.get('REMOTE_ADDR', '')
    
    # Create a new Click object
    click = Click.objects.create(
        short_url=short_url,
        user_agent_string=user_agent_string,
        referer=referer,
        ip_address=ip_address,
    )
    click.save()
    Click.click_count =+ 1
    return redirect(short_url.original_url)


#analytics view for displaying the analytics of a shortened url
@login_required
def analytics_view(request):
    clicks = Click.objects.filter(short_url__user=request.user)
    short_urls = ShortURL.objects.filter(user=request.user)

    url_clicks = {short_url: 0 for short_url in short_urls}

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    search_query = request.GET.get('search', '')

    if start_date and end_date:
        start_date = parse_date(start_date)
        end_date = parse_date(end_date)
        clicks = clicks.filter(timestamp__range=[start_date, end_date])

    if search_query:
        short_urls = short_urls.filter(
            Q(original_url__icontains=search_query) |
            Q(short_code__icontains=search_query)
        )

    for click in clicks:
        if click.short_url in url_clicks:
            url_clicks[click.short_url] += 1

    sort_by = request.GET.get('sort_by')
    if sort_by == 'clicks':
        url_clicks = dict(sorted(url_clicks.items(), key=lambda item: item[1], reverse=True))



    context = {
        'url_clicks': url_clicks,
        'clicks': clicks,
        'start_date': start_date,
        'end_date': end_date,
        'sort_by': sort_by,
        'search_query': search_query,
        'username': request.user.username
    }

    return render(request, 'user/analytics.html', context)


#detail of a shortened links
@login_required
def url_details_view(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    clicks = Click.objects.filter(short_url=short_url)
    qr_coded = generate_qr_code(f"http://127.0.0.1:8000/{short_url.short_code}")

    clicks_per_day = clicks.extra({'day': 'date(timestamp)'}).values('day').annotate(clicks=Count('id')).order_by('day')
    clicks_per_day = list(clicks_per_day)

    referrer_distribution = clicks.values('referer').annotate(count=Count('id')).order_by('-count')
    device_distribution = clicks.values('device').annotate(count=Count('id')).order_by('-count')
    browser_distribution = clicks.values('browser').annotate(count=Count('id')).order_by('-count')
    context = {
        'short_url': short_url,
        'clicks_per_day': json.dumps(clicks_per_day),
        'referrer_distribution': json.dumps(list(referrer_distribution)),
        'device_distribution': json.dumps(list(device_distribution)),
        'browser_distribution': json.dumps(list(browser_distribution)),
        'clicks': clicks,
        'qr_coded': qr_coded,
    }

    return render(request, 'user/url_details.html', context)


#views for customizing the a link
@login_required
def customize_short_url_view(request):
    short_url = None
    qr_code = None

    if request.method == 'POST':
        form = CustomShortURLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            custom_short_code = form.cleaned_data['custom_short_code']

            if ShortURL.objects.filter(short_code=custom_short_code).exists():
                form.add_error('custom_short_code', 'This short code is already in use.')
            else:
                short_url = ShortURL.objects.create(
                    user=request.user,
                    original_url=original_url,
                    short_code=custom_short_code
                )
                qr_code = generate_qr_code(f"http://127.0.0.1:8000/{short_url.short_code}")
    else:
        form = CustomShortURLForm()
    
    return render(request, 'user/customize_short_url.html', {'form': form, 'short_url': short_url, 'qr_code': qr_code})



#for the user to only generate a qr code 
def generate_qr_code_view(request):
    qr_code = None

    if request.method == 'POST':
        form = GenerateQRCodeForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            qr_code = generate_qr_code(url)
    else:
        form = GenerateQRCodeForm()

    return render(request, 'user/generate_qr_code.html', {'form': form, 'qr_code': qr_code})




#for deletion of url
def delete_short_url(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    if request.method == 'POST':
        short_url.delete()
        return redirect('user_links')
    return redirect('user_links')


#getting the all of a users shortern links
@login_required
def user_links(request):
    user_short_urls = ShortURL.objects.filter(user=request.user)
    search_query = request.GET.get('search', '')
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')
    min_clicks = request.GET.get('min_clicks', '')
    
    if search_query:
        user_short_urls = user_short_urls.filter(
            Q(original_url__icontains=search_query) | 
            Q(short_code__icontains=search_query)
        )

    if date_from:
        user_short_urls = user_short_urls.filter(date_created__gte=date_from)
    if date_to:
        user_short_urls = user_short_urls.filter(date_created__lte=date_to)
    
    if min_clicks:
        user_short_urls = user_short_urls.filter(clicks__gte=min_clicks)
    return render(request, 'user/links.html', {'user_short_urls': user_short_urls, })


#views for settings 
@login_required
def settings_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        errors = []

        if not username:
            errors.append("Username is required.")
        if password1 and password1 != password2:
            errors.append("Passwords do not match.")

        if not errors:
            request.user.username = username
            if password1:
                request.user.password = make_password(password1)
                update_session_auth_hash(request, request.user)  # Prevents user from being logged out
            request.user.save()
            return redirect('settings')

        return render(request, 'user/settings.html', {'errors': errors})

    return render(request, 'user/settings.html')


#getting the greeting base on the time a user logged in
def get_greeting():
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good Morning"
    elif current_hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"

#dashboard for a user after logging in
@login_required   
def dashboard_view(request):
    clicks = Click.objects.filter(short_url__user=request.user)
    short_urls = ShortURL.objects.filter(user=request.user)

    url_clicks = {short_url: 0 for short_url in short_urls}

    for click in clicks:
        if click.short_url in url_clicks:
            url_clicks[click.short_url] += 1

    total_links = short_urls.count()
    total_clicks = sum(url_clicks.values())


    best_links = sorted(url_clicks.items(), key=lambda item: item[1], reverse=True)[:10]

    if best_links:
        best_link, _ = best_links[0]
        clicks = Click.objects.filter(short_url=best_link).order_by('-timestamp')
        # Aggregating click statistics for charts
        clicks_per_day = clicks.extra({'day': 'date(timestamp)'}).values('day').annotate(clicks=Count('id')).order_by('day')
        clicks_per_day = list(clicks_per_day)

        referrer_distribution = clicks.values('referer').annotate(count=Count('referer')).order_by('-count')
        device_distribution = clicks.values('device').annotate(count=Count('device')).order_by('-count')
        browser_distribution = clicks.values('browser').annotate(count=Count('browser')).order_by('-count')
    else:
        best_link = None
        clicks = []
        clicks_per_day = []
        referrer_distribution = []
        device_distribution = []
        browser_distribution = []
        
    greeting = get_greeting()

    context = {
        'best_links': best_links,
        'total_links': total_links,
        'total_clicks': total_clicks,
        'best_link': best_link,
        'clicks': clicks,
        'greeting': greeting,
        'clicks_per_day': list(clicks_per_day),
        'referrer_distribution': list(referrer_distribution),
        'device_distribution': list(device_distribution),
        'browser_distribution': list(browser_distribution),
        
    }

    return render(request, 'user/dashboard.html', context)