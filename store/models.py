from typing import Iterable
from django.db import models

class Item(models.Model):
    
    item_category = models.ForeignKey('ItemCategory',on_delete=models.CASCADE, null=True)
    item_name = models.CharField(max_length=200, blank=False, null=True)
    item_price = models.FloatField(blank=False, null=True)
    item_discount_price = models.FloatField(blank=True, null=True)
    item_front_image = models.ImageField(blank = True, null = True)
    item_back_image = models.ImageField(blank = True, null = True)
    item_description = models.TextField(max_length=500, null=True)
    
    YES = 'YE'
    NO = 'NO'
    ITEM_FEATURE = [
        (YES, 'Yes'),
        (NO, 'No')
    ]

    SALE = 'SA'
    OUT_OF_STOCK = 'OUT'
    ITEM_STATUS = [
        (SALE, 'Sale'),
        (OUT_OF_STOCK, 'Out Of Stock')
    ]

    item_feature = models.CharField(
        max_length=2,
        choices=ITEM_FEATURE,
        default=NO,
    )
    item_status = models.CharField(
        max_length=20,
        choices= ITEM_STATUS,
        default=SALE,
    )

    def __str__(self):
        return self.item_name

    @property
    def image_front(self):
        try:
            url = self.item_front_image.url
        except:
            url = ''
        return url

    @property
    def image_back(self):
        try:
            url = self.item_back_image.url
        except:
            url = ''
        return url
    


class ItemCategory(models.Model):

    category_name = models.CharField(max_length=100, blank=False, null=True)
    category_image = models.ImageField(null = True, blank = True)

    YES = 'YE'
    NO = 'NO'
    CATEGORY_FEATURE = [
        (YES, 'Yes'),
        (NO, 'No')
    ]
    category_feature = models.CharField(
        max_length=2,
        choices=CATEGORY_FEATURE,
        default=NO,
    )

    def __str__(self):
        return self.category_name

    @property
    def image_front(self):
        try:
            url = self.category_image.url
        except:
            url = ''
        return url
