from django.shortcuts import render
from django.views import View


class ProductListView(View):
    def get(self, request):
        return render(request, 'category.html')


class ProductDetailView(View):
    def get(self, request, pk):
        return render(request, 'product.html')


class CartView(View):
    def get(self, request):
        return render(request, 'cart.html')


class WishlistView(View):
    def get(self, request):
        return render(request, 'wishlist.html')


class CheckoutView(View):
    def get(self, request):
        return render(request, 'checkout.html')
