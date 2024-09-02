from django.shortcuts import render, get_object_or_404
from contact.models import Contact
from django.http import Http404

# Create your views here.


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - ',
    }
    return render(request, 'contact/index.html', context)


def contact(request, contact_id):
    single_contact = get_object_or_404(
        Contact.objects, pk=contact_id, show=True)

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title
    }
    return render(request, 'contact/contact.html', context)
