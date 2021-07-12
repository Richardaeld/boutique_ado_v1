from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in yuour bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key' :'pk_test_51JCQGcArKPEW0Hcsf2h8gDYJh0byg44zN9iEh3mbMSTnoSzkZpk6qQMMa4I1gQeccR1SdjnhBgYPNsoj78I821ew003PXjJaP2',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)