from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reel
from .forms import ReelForm

def reel_list(request):
    reels = Reel.objects.all().order_by('-created_at')
    return render(request, 'reel_list.html', {'reels': reels})


@login_required
def my_reels(request):
    user_reels = Reel.objects.filter(user=request.user)
    return render(request, 'my_reels.html', {'user_reels': user_reels})



@login_required
def reel_upload(request):
    initial_data = {}
    short_url = request.GET.get('short_url', None)
    if short_url:
        initial_data['url'] = short_url
    
    if request.method == 'POST':
        form = ReelForm(request.POST, request.FILES)
        if form.is_valid():
            reel = form.save(commit=False)
            reel.user = request.user
            reel.save()
            return redirect('reel_list')
    else:
        form = ReelForm(initial=initial_data)
    return render(request, 'reel_upload.html', {'form': form})

@login_required
def reel_update(request, reel_id):
    reel = get_object_or_404(Reel, id=reel_id, user=request.user)
    if request.method == 'POST':
        form = ReelForm(request.POST, request.FILES, instance=reel)
        if form.is_valid():
            form.save()
            return redirect('reel_list')
    else:
        form = ReelForm(instance=reel)
    return render(request, 'reel_update.html', {'form': form, 'reel': reel})

@login_required
def reel_delete(request, reel_id):
    reel = get_object_or_404(Reel, id=reel_id, user=request.user)
    if request.method == 'POST':
        reel.delete()
        return redirect('my_reels')
    return render(request, 'reel_delete.html', {'reel': reel})
