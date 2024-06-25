from django.views.generic import TemplateView
from .models import Slogan, YouTubeVideo, Product
from django.views.generic import ListView, DetailView, CreateView
from .models import Product, Review
from .forms import ReviewForm
from django.views.generic import FormView, ListView
from .models import CartItem, Order
from .forms import CartItemForm

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slogan'] = Slogan.objects.first()
        context['video'] = YouTubeVideo.objects.first()
        context['top_products'] = Product.objects.order_by('?')[:5]
        return context

class ProductListView(ListView):
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(product=self.object)
        context['form'] = ReviewForm()
        return context

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'add_review.html'

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['pk']
        return super().form_valid(form)

class CartView(FormView):
    template_name = 'cart.html'
    form_class = CartItemForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class OrderListView(ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'orders'
