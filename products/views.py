from django.shortcuts import render
from django.views import View


class ProductListView(View):
    def get(self, request):
        return render(request, 'ecommerce/category.html')


class ProductDetailView(View):
    def get(self, request, pk):
        return render(request, 'ecommerce/product.html')


class CartView(View):
    def get(self, request):
        return render(request, 'ecommerce/cart.html')


class WishlistView(View):
    def get(self, request):
        return render(request, 'ecommerce/wishlist.html')


class CheckoutView(View):
    def get(self, request):
        return render(request, 'ecommerce/checkout.html')
