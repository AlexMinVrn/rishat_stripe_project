from django.urls import path
from . import views

app_name = 'item_app'

urlpatterns = [
    path('', views.index),
    path('item/', views.item_list),
    # Оплата одного товара
    path('item/<int:pk>/', views.item_detail, name='item'),
    path(
        'buy/<int:pk>/',
        views.item_checkout_session,
        name='item_checkout_session'
    ),
    # Странички успешной и неуспешной оплаты
    path('success/', views.PaymentSuccessView.as_view(), name='success'),
    path('failed/', views.PaymentFailedView.as_view(), name='failed'),
]
