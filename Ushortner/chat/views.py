from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from .forms import MessageForm
from django.db.models import Q 
from django.core.mail import send_mail

@login_required
def chat_list(request):
    # Get all users the current user has sent or received messages from
    users = User.objects.filter(
        Q(id__in=Message.objects.filter(sender=request.user).values_list('receiver_id', flat=True)) |
        Q(id__in=Message.objects.filter(receiver=request.user).values_list('sender_id', flat=True))
    ).distinct()

    # Get unread message counts for each user
    unread_counts = {}
    for user in users:
        unread_counts[user.id] = Message.objects.filter(sender=user, receiver=request.user, is_read=False).count()

    return render(request, 'chat/chat_list.html', {'users': users, 'unread_counts': unread_counts})


#chat details
@login_required
def chat_detail(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = user
            message.save()

            # Send an email notification
            send_mail(
                subject='New Message Notification',
                message=f'You have received a new message from {request.user.username}.',
                from_email='developeregyakofi@gmail.com',
                recipient_list=[user.email],
                fail_silently=False,
            )

            return redirect('chat_detail', username=user.username)
    else:
        form = MessageForm()

    # Get messages between the current user and the target user
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(receiver=user)) |
        (Q(sender=user) & Q(receiver=request.user))
    ).order_by('timestamp')

    # Mark messages as read
    unread_messages = messages.filter(receiver=request.user, is_read=False)
    unread_messages.update(is_read=True)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(sender=request.user, receiver=user, content=content)

    if request.method == 'POST' and 'delete_message_ids' in request.POST:
        message_ids = request.POST.getlist('delete_message_ids')
        Message.objects.filter(id__in=message_ids).delete()

    return render(request, 'chat/chat_detail.html', {'messages': messages, 'form': form, 'user': user})



#deleting a chat
@login_required
def delete_chat(request, user_id):
    user = get_object_or_404(User, id=user_id)
    Message.objects.filter(
        (Q(sender=request.user) & Q(receiver=user)) |
        (Q(sender=user) & Q(receiver=request.user))
    ).delete()
    return redirect('chat_list')