from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Cake, Order, Category, PinCode
from .forms import OrderForm
from django.urls import reverse_lazy
from django.db.models import Q # for search method
from django.http import JsonResponse
import json

class CakesListView(ListView):
    model = Cake
    template_name = 'list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category_name = self.request.GET.get('category')
        if category_name:
            queryset = queryset.filter(categories__name=category_name)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Pass all categories to the template
        return context


class CakesDetailView(DetailView):
    model = Cake
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pincode_list'] = list(PinCode.objects.values_list('code', flat=True))
        return context


class SearchResultsListView(ListView):
	model = Cake
	template_name = 'search_results.html'

	def get_queryset(self): # new
		query = self.request.GET.get('q')
		return Cake.objects.filter(
		Q(name__icontains=query)
		)

class CakeCheckoutView(LoginRequiredMixin, DetailView):
    model = Cake
    template_name = 'checkout.html'
    login_url     = 'login'


def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	product = Cake.objects.get(id=body['productId'])
	Order.objects.create(
		product=product
	)
	return JsonResponse('Payment completed!', safe=False)

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')  # Redirect to a success page or show a success message
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})

def order_success(request):
    return render(request, 'order_success.html')

