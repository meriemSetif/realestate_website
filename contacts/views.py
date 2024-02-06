from pprint import pprint
import smtplib
from django.shortcuts import render, redirect
from .models import Contact
from listings.models import Listing
from django.contrib import messages


# Create your views here.
def contact(request):
    contacts = Contact.objects.order_by("-contact_date")
    context = {"contacts": contacts}
    if request.method == "POST":

        listing = Listing.objects.get(pk=request.POST.get("listing_id", ""))
        user = request.user
        message = request.POST.get("message", "")
        email_from = request.POST.get("emailfrom", "")
        print(f"the user {user} submitted the query!")
        print(f"in the listing: {listing}")
        if contacts.filter(listing=listing).filter(user=user).exists():
            messages.error(
                request, f"you've already made an iquiry about {listing.title}"
            )
            return redirect(f"/listings/{listing.pk}")
        contact = Contact(
            listing=listing, user=user, name=user.username, message=message
        )
        contact.save()
        print("teh metadata of the mail to be sent are:")
        pprint(
            (
                f"Property listing inquiry",
                f"there has been query about {listing} sign in the panel for more info",
                f"yahialinus21alg@gmail.com",
                [f"{listing.instructor.email}"],
            )
        )

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            proxy_email_address = "yahialinus21alg@gmail.com"
            proxy_email_password = "qxnx wwlu ehuj kjtg"  # Use the App Password you generated
            pprint(connection.login(proxy_email_address, proxy_email_password))
            connection.sendmail(proxy_email_address, listing.instructor.email,
                                f'Subject:inquiry about listing {listing}\n\n{message} by {user.email}')

        return redirect("dashboard")
    return render(request, "contacts/contact.html", context)
