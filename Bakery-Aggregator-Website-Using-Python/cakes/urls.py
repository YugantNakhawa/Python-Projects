
from django.urls import path
from .views import CakesListView, CakesDetailView, CakeCheckoutView, paymentComplete, SearchResultsListView, create_order, order_success


urlpatterns = [
    path('', CakesListView.as_view(), name = 'list'),
    path('<int:pk>/', CakesDetailView.as_view(), name = 'detail'),
    path('<int:pk>/checkout/', CakeCheckoutView.as_view(), name = 'checkout'),
    path('complete/', paymentComplete, name = 'complete'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
    path('order/', create_order, name='create_order'),
    path('order/success/', order_success, name='order_success')
]