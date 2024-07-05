from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
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



def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        errors = []

        if not username or not password1 or not password2:
            errors.append("All fields are required.")
        if password1 != password2:
            errors.append("Passwords do not match.")
        if User.objects.filter(username=username).exists():
            errors.append("Username already exists.")
        
        if not errors:
            user = User.objects.create(username=username, password=make_password(password1))
            login(request, user)
            # return redirect(reverse('shorten_view'))
            return render(request, 'basehome/homepage.html')

        else:
            return render(request, 'user/signup.html', {'errors': errors})
    
    return render(request, 'user/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            # return redirect(reverse('shorten_view'))
            return render(request, 'basehome/homepage.html')

    return render(request, 'user/login.html')

@login_required
def user_dashboard(request):
    """View function for displaying the user dashboard page."""
    user_short_urls = ShortURL.objects.filter(user=request.user).order_by('-date_created')
    short_code = None  # Initialize short_code here
    qr_code = None 

    if request.method == 'POST':
        original_url = request.POST['url']
        if ShortURL.objects.filter(original_url=original_url).exists():
            short_url = ShortURL.objects.get(original_url=original_url)
            short_code = short_url.short_code
            qr_code = generate_qr_code(request.build_absolute_uri(f'/{short_code}'))
        else:
            short_code = str(uuid.uuid4())[:5]
            short_url = ShortURL.objects.create(original_url=original_url, short_code=short_code, user=request.user)
            qr_code = generate_qr_code(request.build_absolute_uri(f'/{short_code}'))
            short_url.save()
        short_code = request.build_absolute_uri(f'/{short_code}')

    context = {
        'user_short_urls': user_short_urls,
        'short_code': short_code,
        'qr_code': qr_code,
    }
    return render(request, 'user/userdashboard.html', context)



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



@login_required
def user_links(request):
    user_short_urls = ShortURL.objects.filter(user=request.user)
    # click_user = Click.objects.filter(click_count=click_count)

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
        # click_user=click_user.filter(click_count__gte=min_clicks)
    # print(Click.click_count)
    return render(request, 'user/links.html', {'user_short_urls': user_short_urls})



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
