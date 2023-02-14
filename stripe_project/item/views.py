import stripe
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from .models import Item


def index(request):
    return HttpResponse('Главная страница')


def item_list(request):
    return HttpResponse('Список элементов')


def item_detail(request, pk):
    """Рендер страницы оплаты одного товара."""
    item = get_object_or_404(Item, pk=pk)
    return render(
        request,
        'item/item.html',
        {
            'item': item,
            'stripe_publishable_key': settings.STRIPE_PUBLIC_KEY
        }
    )


@csrf_exempt
def item_checkout_session(request, pk):
    """Stripe-сессия оплаты одного предмета."""
    item = get_object_or_404(Item, pk=pk)
    stripe.api_key = settings.STRIPE_SECRET_KEY

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': item.name},
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url='http://127.0.0.1:8000/success/',
        cancel_url='http://127.0.0.1:8000/failed/',
    )

    return JsonResponse({'sessionId': checkout_session.id})


class PaymentSuccessView(TemplateView):
    template_name = "item/success.html"


class PaymentFailedView(TemplateView):
    template_name = "item/failed.html"
