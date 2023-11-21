import os
from decimal import Decimal

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# from django.core.exceptions import ValidationError
# from main_app.models import Customer, Book, Product, DiscountedProduct, SpiderHero, FlashHero
