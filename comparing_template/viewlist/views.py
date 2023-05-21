from django.views.generic import ListView
from .models import Product


class ProductList(ListView):
    model = Product
    template_name = 'your_template.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('name', 'price')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        products = self.get_queryset()

        product_groups = {}
        for product in products:
            product_name = product.name
            if product_name in product_groups:
                product_groups[product_name].append(product)
            else:
                product_groups[product_name] = [product]

        context['product_groups'] = product_groups

        return context
