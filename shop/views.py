from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shop.models import Category, Product, Customer
from shop.forms import CustomerForm


class IndexView(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        category_id = self.kwargs.get('category_id')
        if category_id:
            context['products'] = Product.objects.filter(category=category_id)
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product-detail.html'
    context_object_name = 'product'


class CustomerListView(ListView):
    model = Customer
    template_name = 'shop/customer_add.html'
    context_object_name = 'customers'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Customer.objects.filter(name__icontains=query)
        return Customer.objects.all()


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'shop/customer_details.html'
    context_object_name = 'customer'


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'shop/customer_add.html'
    success_url = reverse_lazy('customers')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'shop/customer_update.html'
    success_url = reverse_lazy('customers')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'shop/customer_delete.html'
    success_url = reverse_lazy('customers')

    def get_object(self, queryset=None):
        return get_object_or_404(Customer, id=self.kwargs.get('customer_id'))