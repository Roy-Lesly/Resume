from django.shortcuts import render
from .models import Personal


person = Personal.objects.all().first()


def WelcomeView(request):
    context = {
        "full_name": person.full_name
    }
    return render(request, 'welcome.html', context)


def HomeView(request):
    context = {
        "my_full_name": person.full_name,
    }
    return render(request, 'includes/home.html', context)


def AboutView(request):
    print(person.full_name)
    context = {
        "page_title": "HOME", "sub_title": "Home Page",
        "my_full_name": person.full_name, 'my_address': person.address, 'my_sex': person.sex,
        "my_site": person.site, 'my_degree': person.degree, 'my_phone': person.phone,
        'my_email': 'Add Model', 'my_freelance': person.freelance,
        "my_age": "Add Model", 'my_city': 'Add Model', 'my_country': 'Add Model',
    }
    return render(request, 'includes/about.html', context)


def ResumeView(request):
    context = {
    }
    return render(request, 'includes/about.html', context)


def PortfolioView(request):
    context = {
    }
    return render(request, 'includes/portfolio.html', context)


def ServicesView(request):
    person = Personal.objects.all().first()
    context = {
    }
    return render(request, 'includes/services.html', context)


def ContactView(request):
    context = {
    }
    return render(request, 'includes/about.html', context)