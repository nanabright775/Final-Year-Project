from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserProfileForm, PortfolioForm
from .models import UserProfile, Portfolio
from django.contrib.auth.decorators import login_required
from .api_client import CohereAPI
import cohere

@login_required
def display_generated_content(request, choice, username):
    portfolio = get_object_or_404(Portfolio, user__username=username, url=f"{choice}/{username}")
    return render(request, 'portfolio_generator/display_generated_content.html', {'portfolio': portfolio})


@login_required
def create_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('portfolio_generator:choose_generation')
    else:
        form = UserProfileForm(instance=user_profile)
    
    return render(request, 'portfolio_generator/create_profile.html', {'form': form})


@login_required
def choose_generation(request):
    if request.method == 'POST':
        choice = request.POST.get('choice')
        user_profile = request.user.userprofile
        
        prompt = (
            f"Generate a {choice} for a user with the following details:\n"
            f"Name: {user_profile.name}\n"
            f"Email: {user_profile.email}\n"
            f"Bio: {user_profile.bio}\n"
            f"Include relevant sections and content."
        )
        
        try:
            generated_content = CohereAPI.generate_content(prompt)
        except cohere.errors.CohereError as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('portfolio_generator:choose_generation')
        
        portfolio = Portfolio.objects.create(
            user=request.user,
            title=f"{user_profile.name}'s {choice.capitalize()}",
            content=generated_content,
            url=f"{choice}/{request.user.username}"
        )
        
        return redirect('portfolio_generator:display_generated_content', choice=choice, username=request.user.username)
    
    return render(request, 'portfolio_generator/choose_generation.html')


@login_required
def list_portfolios(request):
    portfolios = Portfolio.objects.filter(user=request.user)
    return render(request, 'portfolio_generator/list_portfolios.html', {'portfolios': portfolios})

@login_required
def edit_portfolio(request, portfolio_id):
    portfolio = Portfolio.objects.get(id=portfolio_id, user=request.user)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio_generator:list_portfolios')
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, 'portfolio_generator/edit_portfolio.html', {'form': form})


@login_required
def display_generated_content(request, choice, username):
    portfolio = get_object_or_404(Portfolio, user__username=username, url=f"{choice}/{username}")
    return render(request, 'portfolio_generator/display_generated_content.html', {'portfolio': portfolio})
