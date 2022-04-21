from django.shortcuts import render
from .models import Personal


def WelcomeView(request):
    person = Personal.objects.all().first()
    context = {
        "full_name": person.full_name
    }
    return render(request, 'welcome.html', context)


def HomeView(request):
    person = Personal.objects.all().first()
    context = {
        "my_full_name": person.full_name,
    }
    return render(request, 'includes/home.html', context)


def AboutView(request):
    person = Personal.objects.all().first()
    print(person.full_name)
    context = {
        "page_title": "HOME", "sub_title": "Home Page",
        "my_full_name": person.full_name, 'my_address': person.address, 'my_sex': person.sex,
        "my_site": person.site, 'my_degree': person.degree, 'my_phone': person.phone,
        'my_email': person.email, 'my_freelance': person.freelance, "my_age": "calc",
        "my_birth": person.dob, 'my_city': person.city, 'my_country': person.country,
    }
    return render(request, 'includes/about.html', context)


def ResumeView(request):
    context = {
    }
    return render(request, 'includes/resume.html', context)


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
    person = Personal.objects.all().first()
    context = {
        "page_title": "HOME", "sub_title": "Home Page",
        "my_full_name": person.full_name, 'my_address': person.street, 'my_sex': person.sex,
        "my_site": person.site, 'my_degree': person.degree, 'my_phone': person.phone, "my_telephone": person.telephone,
        'my_email': person.email, 'my_freelance': person.freelance, "my_age": "calc",
        "my_birth": person.dob, 'my_city': person.city, 'my_country': person.country,
    }
    return render(request, 'includes/contact.html', context)