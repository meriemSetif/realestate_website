from django.shortcuts import render
from listings.models import Listing
from listings.choices import bedrooms_choices, prices_choices, states_choices
from realtors.models import realtor


# Create your views here.
def index(request):
    latest_listings = Listing.objects.order_by("-list_date").filter(is_published=True)[
        :3
    ]
    context = {
        "listings": latest_listings,
        "bedrooms_choices": bedrooms_choices,
        "prices_choices": prices_choices,
        "states_choices": states_choices,
    }
    return render(request, "pages/index.html", context)


def about(request):
    realtors = realtor.objects.all()
    best_seller = realtor.objects.order_by("-id").filter(is_mvp=True)
    context = {
        "realtors": realtors,
        "best_seller": best_seller[0] if best_seller else "",
    }
    return render(request, "pages/about.html", context)
