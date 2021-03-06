from django.shortcuts import render
# from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices


def index(request):
    print('User: ', request.user.username)
    listings = Listing.objects.filter(is_published=True).order_by(
        '-price')[:3]
    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get All realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
    }
    return render(request, 'pages/about.html', context)
