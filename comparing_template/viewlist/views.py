from django.views.generic import ListView

from .models import Product


class ProductList(ListView):
    model = Product
    template_name = 'your_template.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-name', '-price')
