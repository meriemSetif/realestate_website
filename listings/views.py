from pprint import pprint
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from .models import Listing
from .choices import bedrooms_choices, prices_choices, states_choices


# Create your views here.
def index(request):
    # listings = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    for listing in listings:
        print("the address is:", listing.address)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    
    context = {"listings": page_listings}
    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    print(listing_id)
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {"listing": listing}
    return render(request, "listings/listing.html", context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    keywords = request.GET.get('keywords','')
    if keywords.strip():
        queryset_list = queryset_list.filter(description__icontains=keywords)

    city = request.GET.get('city','')
    if city.strip():
        queryset_list = queryset_list.filter(city__iexact=city)

    state = request.GET.get('state','')
    if state.strip():
        queryset_list = queryset_list.filter(state__iexact=state)

    bedrooms = request.GET.get('bedrooms','')
    if bedrooms:
        queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    price = request.GET.get('price','')
    if price:
        queryset_list = queryset_list.filter(price__lte=price)


    paginator = Paginator(queryset_list, 3)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {
        "bedrooms_choices": bedrooms_choices,
        "prices_choices": prices_choices,
        "states_choices": states_choices,
        "listings":page_listings,
        "values": request.GET
    }

    return render(request, "listings/search.html",context)
