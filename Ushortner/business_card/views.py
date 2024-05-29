# business_card/views.py

from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import BusinessCardTemplate, UserBusinessCard
from .forms import UserBusinessCardForm
from PIL import Image, ImageDraw, ImageFont
import qrcode



@login_required
def create_business_card(request):
    if request.method == 'POST':
        form = UserBusinessCardForm(request.POST, request.FILES)
        if form.is_valid():
            business_card = form.save(commit=False)
            business_card.user = request.user
            business_card.save()
            # image_path = generate_business_card(business_card)
            return redirect('business_card_detail', pk=business_card.pk)
    else:
        form = UserBusinessCardForm()

    templates = BusinessCardTemplate.objects.all()
    return render(request, 'business_card/create_business_card.html', {'form': form, 'templates': templates})

@login_required
def business_card_detail(request, pk):
    business_card = get_object_or_404(UserBusinessCard, pk=pk)
    return render(request, 'business_card/business_card_detail.html', {'business_card': business_card})

@login_required
def render_business_card(request, business_card_id):
    business_card = get_object_or_404(UserBusinessCard, id=business_card_id)
    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename="{business_card.name}_business_card.png"'
    return response

@login_required
def business_card_list(request):
    business_cards = UserBusinessCard.objects.filter(user=request.user)
    return render(request, 'business_card/business_card_list.html', {'business_cards': business_cards})

@login_required
def business_card_update(request, pk):
    business_card = get_object_or_404(UserBusinessCard, pk=pk, user=request.user)
    if request.method == 'POST':
        form = UserBusinessCardForm(request.POST, instance=business_card)
        if form.is_valid():
            form.save()
            return redirect('business_card_list')
    else:
        form = UserBusinessCardForm(instance=business_card)
    return render(request, 'business_card/business_card_form.html', {'form': form})

@login_required
def business_card_delete(request, pk):
    business_card = get_object_or_404(UserBusinessCard, pk=pk, user=request.user)
    if request.method == 'POST':
        business_card.delete()
        return redirect('business_card_list')
    return render(request, 'business_card/business_card_confirm_delete.html', {'business_card': business_card})



def generate_business_card(business_card):
    # Load the template image
    template_img = Image.open(business_card.template.image.path)

    # Prepare the drawing context
    draw = ImageDraw.Draw(template_img)

    # Load a font
    # font = ImageFont.truetype("arial.ttf", 40)
    font = ImageFont.load_default()

    # Add text to the image
    draw.text((50, 50), business_card.name, font=font, fill="black")
    draw.text((50, 100), business_card.company_name, font=font, fill="black")
    draw.text((50, 150), business_card.email, font=font, fill="black")
    draw.text((50, 200), business_card.phone_number, font=font, fill="black")
    draw.text((50, 250), business_card.linkedin, font=font, fill="black")
    draw.text((50, 300), business_card.twitter, font=font, fill="black")
    draw.text((50, 350), business_card.facebook, font=font, fill="black")
    draw.text((50, 400), business_card.instagram, font=font, fill="black")

    # Add the logo
    if business_card.logo:
        logo_img = Image.open(business_card.logo.path)
        logo_img.thumbnail((100, 100))
        template_img.paste(logo_img, (50, 450))

    # Generate and add the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr_data = f"Name: {business_card.name}\nCompany: {business_card.company_name}\nEmail: {business_card.email}\nPhone: {business_card.phone_number}\nLinkedIn: {business_card.linkedin}\nTwitter: {business_card.twitter}\nFacebook: {business_card.facebook}\nInstagram: {business_card.instagram}"
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white")
    qr_img.thumbnail((100, 100))
    template_img.paste(qr_img, (200, 450))

    # Save the image
    output_path = f"generated_cards/{business_card.user.username}_{business_card.id}.png"
    template_img.save(output_path)
    return output_path