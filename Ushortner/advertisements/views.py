from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Campaign, Reel, Comment, Like
from .forms import CampaignForm, ReelForm, CommentForm
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q,F
from django.http import JsonResponse


#getting all the content from reels and campaigns and placin them in content as one
def content_list(request):
    campaigns = Campaign.objects.all()
    reels = Reel.objects.all()
    content = sorted(list(campaigns) + list(reels), key=lambda x: x.created_at, reverse=True)
    return render(request, 'advertisements/content_list.html', {'content': content})

#creating reels and/or campaings
@login_required
def content_create(request, content_type):
    initial_data = {}
    short_url = request.GET.get('short_url', None)
    if short_url:
        initial_data['url'] = short_url

    if content_type == 'campaign':
        form_class = CampaignForm
    else:
        form_class = ReelForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.user = request.user
            content.save()
            return redirect('content_list')
    else:
        form = form_class(initial=initial_data)

    return render(request, 'advertisements/content_create.html', {'form': form})


#getting all the content from reels and campaigns and placin them in content as one
@login_required
def my_content(request):
    campaigns = Campaign.objects.filter(user=request.user)
    reels = Reel.objects.filter(user=request.user)
    content = sorted(list(campaigns) + list(reels), key=lambda x: x.created_at, reverse=True)
    return render(request, 'advertisements/my_content.html', {'content': content})


#updating reels or campaign
@login_required
def update_content(request, content_type, content_id):
    if content_type == 'campaign':
        content = get_object_or_404(Campaign, id=content_id, user=request.user)
        form_class = CampaignForm
    else:
        content = get_object_or_404(Reel, id=content_id, user=request.user)
        form_class = ReelForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=content)
        if form.is_valid():
            form.save()
            return redirect('content_detail', content_type=content_type, content_id=content_id)
    else:
        form = form_class(instance=content)
    return render(request, 'advertisements/update_content.html', {'form': form, 'content': content})

#deleting reels of campaigns
@login_required
def delete_content(request, content_type, content_id):
    if content_type == 'campaign':
        content = get_object_or_404(Campaign, id=content_id, user=request.user)
    else:
        content = get_object_or_404(Reel, id=content_id, user=request.user)
    
    if request.method == 'POST':
        content.delete()
        return redirect('my_content')
    return render(request, 'advertisements/delete_content.html', {'content': content})


#getting the details of a comments on a campaign or reels
def content_detail(request, content_type, content_id):
    if content_type == 'campaign':
        content = get_object_or_404(Campaign, id=content_id)
    else:
        content = get_object_or_404(Reel, id=content_id)

    comments = Comment.objects.filter(content_type=ContentType.objects.get_for_model(content), object_id=content.id)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.content_object = content
            new_comment.save()
            return redirect('content_detail', content_type=content_type, content_id=content_id)
    else:
        comment_form = CommentForm()

    return render(request, 'advertisements/content_detail.html', {'content': content, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})


#quary for searching reels or campaigns
def search(request):
    query = request.GET.get('q')
    if query:
        campaigns = Campaign.objects.filter(
            Q(description__icontains=query) | Q(url__icontains=query)
        )
        reels = Reel.objects.filter(
            Q(description__icontains=query) | Q(url__icontains=query)
        )
        results = sorted(list(campaigns) + list(reels), key=lambda x: x.created_at, reverse=True)
    else:
        results = []

    return render(request, 'advertisements/search_results.html', {'results': results})



def like_content(request, content_type_id, object_id):
    content_type = get_object_or_404(ContentType, id=content_type_id)
    content_object = content_type.get_object_for_this_type(id=object_id)
    
    # Increment the like count
    content_object.like_count = F('like_count') + 1
    content_object.save(update_fields=['like_count'])
    
    # Fetch the updated like count
    content_object.refresh_from_db()
    return redirect(content_list)

#creating a comment
def comment_content(request, content_type_id, object_id):
    content_type = get_object_or_404(ContentType, id=content_type_id)
    content_object = content_type.get_object_for_this_type(id=object_id)
    comments = Comment.objects.filter(content_type=content_type, object_id=object_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.content_type = content_type
            comment.object_id = object_id
            comment.save()
            return redirect('comment_content', content_type_id=content_type_id, object_id=object_id)
    else:
        form = CommentForm()
    
    return render(request, 'advertisements/comment_content.html', {'content_object': content_object, 'comments': comments, 'form': form})
