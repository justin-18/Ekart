import os
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string

class Command(BaseCommand):
    help = 'Generate static HTML files from templates'

    def handle(self, *args, **kwargs):
        templates = [
            'index.html',
            'base.html',
            'cart-list.html',
            'checkout.html',
            'home.html',
            'offer-products.html',
            'order-list.html',
            'product-detail.html',
            'review.html',
            'signup.html'

            # Add all your template files here
        ]
        output_dir = 'static_site'
        os.makedirs(output_dir, exist_ok=True)

        for template in templates:
            rendered = render_to_string(template)
            output_path = os.path.join(output_dir, template)
            with open(output_path, 'w') as f:
                f.write(rendered)
            self.stdout.write(self.style.SUCCESS(f'Successfully rendered {template}'))
