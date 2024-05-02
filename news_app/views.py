from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm
from .models import News


def yangiliklar_view(request):

    yangiliklar = News.published.all()
    latest_news_5 = News.published.all()[:5]
    iqtisodiy_news_1 = News.published.filter(category__nomi='Iqtsodiyot')[0]
    iqtisodiy_news_4 = News.published.filter(category__nomi='Iqtsodiyot')[0:5]
    sport_news = News.published.filter(category__nomi='Sport')[:5]
    technology_news = News.published.filter(category__nomi='Texnologiya')[:5]
    xorij_news = News.published.filter(category__nomi='Xorij')[:5]

    context = {

        'yangiliklar': yangiliklar,
        'latest_news_5': latest_news_5,
        'iqtisodiy_news_1': iqtisodiy_news_1,
        'iqtisodiy_news_4': iqtisodiy_news_4,
        'sport_news': sport_news,
        'technology_news': technology_news,
        'xorij_news': xorij_news,

    }

    return render(request, context=context, template_name='index.html')


def get_yangilik(request, id):

    yangilik = News.objects.get(id=id)
    yaqin_news = News.objects.filter(category__nomi=yangilik.category)[:3]

    context = {
        'yangilik': yangilik,
        'yaqin_news': yaqin_news,
    }

    return render(request, context=context, template_name='single_page.html')


def texno_news_view(request):

    news_list = News.published.filter(category__nomi='Texnologiya')

    context = {
        'news_list': news_list
    }

    return render(request, context=context, template_name='texno.html')


def contact_view(request):
    form = ContactForm(request.POST)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return HttpResponse("Xabaringiz yuborildi")
    context = {
        'form': form
    }

    return render(request, context=context, template_name='contact.html')


def about_view(request):

    return render(request, template_name='about.html')

