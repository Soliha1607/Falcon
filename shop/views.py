from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shop.models import Category, Product, Customer
from shop.forms import CustomerForm

def index(request, category_id=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_id:
        products = Product.objects.filter(category=category_id)
        context = {'products': products}
        return render(request, 'shop/product-list.html', context)
    context = {'categories': categories, 'products': products}
    return render(request, 'shop/index.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'shop/product-detail.html', context)


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

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))
        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product-detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'

    def get_object(self, queryset=None):
        return Product.objects.get(id=self.kwargs['product_id'])



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
    template_name = 'shop/customer-details.html'
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