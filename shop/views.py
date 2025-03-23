from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from shop.models import Customer
from shop.forms import CustomerForm
from shop.models import Category, Product

# Create your views here.

def index(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        products = Product.objects.filter(category__slug=category_slug)
        context = {'products': products}
        return render(request, 'shop/product-list.html', context)
    context = {'categories': categories, 'products': products}
    return render(request, 'shop/index.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'shop/product-detail.html', context)


class ProductDetail(DetailView):
    model = Product
    template_name = 'shop/product-detail.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'


class IndexView(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        category_slug = self.kwargs['category_slug']
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.filter(
            category__slug=category_slug) if category_slug else Product.objects.all()

        if category_slug:
            self.template_name = 'shop/product-list.html'

        return context


class CustomerListView(ListView):
    model = Customer
    template_name = 'shop/customers.html'
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
    success_url = reverse_lazy('shop:customers')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'shop/customer_delete.html'
    success_url = reverse_lazy('shop:customers')

    def get_object(self, queryset=None):
        return get_object_or_404(Customer, id=self.kwargs.get('customer_id'))