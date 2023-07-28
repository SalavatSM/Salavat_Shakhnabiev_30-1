from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    rate = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    ''' categories '''
    category = models.ManyToManyField(Category)


class Review(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    ''' product '''
    product = models.ForeignKey('Product', on_delete=models.CASCADE)



