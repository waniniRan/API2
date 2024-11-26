from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100, help_text="Full name of the customer")
    email = models.EmailField(unique=True, help_text="Email address of the customer")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Time when the customer was created")


#to convert the objects being called to string
    def __str__(self):
        return self.name





class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders', help_text="The customer who placed the order")
    order_date = models.DateTimeField(auto_now_add=True, help_text="The date and time the order was placed")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total amount for the order")

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"

