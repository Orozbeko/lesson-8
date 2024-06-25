from django.db import models

class Slogan(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class YouTubeVideo(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f'Review for {self.product.name}'

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product.name} ({self.quantity})'


class Order(models.Model):
    items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} at {self.created_at}'