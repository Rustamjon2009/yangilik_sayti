from django.shortcuts import render

# Create your views here.

from .models import Users


def users_view(request):

    foydalanuvchilar = Users.objects.all()

    context = {
        'foydalanuvchilar': foydalanuvchilar,

    }

    return render(request, context=context, template_name='users.html')


def get_users(request, name):

    foydalanuvchi = Users.objects.get(name=name)

    context = {
        'foydalanuvchi': foydalanuvchi
    }

    return render(request, context=context, template_name='user_info.html')
