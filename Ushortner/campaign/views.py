from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Campaign
from .forms import CampaignForm

def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'campaign/campaign_list.html', {'campaigns': campaigns})

@login_required
def campaign_create(request):
    initial_data = {}
    short_url = request.GET.get('short_url', None)
    if short_url:
        initial_data['url'] = short_url
    
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.user = request.user
            campaign.save()
            return redirect('campaign_list')
    else:
        form = CampaignForm(initial=initial_data)
    
    return render(request, 'campaign/campaign_create.html', {'form': form})

@login_required
def my_campaigns(request):
    user_campaigns = Campaign.objects.filter(user=request.user)
    return render(request, 'campaign/my_campaigns.html', {'user_campaigns': user_campaigns})


#update campaign function
def update_campaign(request, campaign_id):
    campaign = get_object_or_404(Campaign, pk=campaign_id)

    if request.method == 'POST' and campaign.user == request.user:
        form = CampaignForm(request.POST, instance=campaign)
        if form.is_valid():
            form.save()
            return redirect('campaign_detail', campaign_id=campaign_id)
    else:
        form = CampaignForm(instance=campaign)
    return render(request, 'campaign/update_campaign.html', {'form': form, 'campaign': campaign})


#for detail view of the campaign
def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, pk=campaign_id)
    return render(request, 'campaign/campaign_detail.html', {'campaign': campaign})


@login_required
def my_campaigns(request):
    user_campaigns = Campaign.objects.filter(user=request.user)
    return render(request, 'campaign/my_campaign.html', {'user_campaigns': user_campaigns})



@login_required
def delete_campaign(request, campaign_id):
    campaign = get_object_or_404(Campaign, pk=campaign_id)
    if request.method == 'POST' and campaign.user == request.user:
        campaign.delete()
        return redirect('my_campaigns')  # Redirect to the user's campaign list after deletion
    return redirect('campaign_detail', campaign_id=campaign_id)  # Redirect to the campaign detail page if deletion fails
