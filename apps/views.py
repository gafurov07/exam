from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.models import Product, Profile


# from apps.models import Humans
#
#
# def human_view(request):
#     context = {
#         'humans': Humans.objects.all()
#     }
#     return render(request, 'apps/human-list.html', context)
#
#
# def deteil_view(request, pk):
#     context = {
#         'human': Humans.objects.get(pk=pk)
#     }
#     return render(request, 'apps/deteil.html', context)

def send_email_view(request):
    subject = 'Welcome to my site'
    massage = 'Thank you for creating an account!'
    recipient_list = ['faxriddingafurov395@gmail.com']
    send_mail(subject, massage, EMAIL_HOST_USER, recipient_list)
    return HttpResponse('Successfully sent email!')


def form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        Product.objects.create(name=name, price=price, description=description)
    return render(request, 'apps/send-email.html')


def profile_view(request):
    # if request.method == 'POST':
    #     full_name = request.POST.get('full_name')
    #     description = request.POST.get('description')
    #     email = request.POST.get('email')
    #     phone = request.POST.get('phone')
    #     image = request.POST.get('image')
    #     Profile.objects.create(full_name=full_name, email=email, phone=phone, image=image, description=description)
    # return render(request, 'apps/profile.html')
    context = {
        'profile': Profile.objects.all()
    }
    return render(request, 'apps/profile.html', context)


def profile_deteil_view(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        image = request.POST.get('image')
        description = request.POST.get('description')
        profile.full_name = full_name
        profile.email = email
        profile.phone = phone
        profile.image = image
        profile.description = description
        profile.save()
        return redirect('profiles')
    context = {
        'profile': profile
    }
    return render(request, 'apps/profile-deteil.html', context)


def add_profile_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        image = request.POST.get('image')
        description = request.POST.get('description')
        profile = Profile.objects.create(full_name=full_name, email=email, phone=phone, image=image, description=description)
        return redirect('profiles')
    return render(request, 'apps/add-profile.html')