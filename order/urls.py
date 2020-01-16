from django.urls import path
from .views      import OrdersView

urlpatterns = [
    path('/ordersview', OrdersView.as_view()),
]