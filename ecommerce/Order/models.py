from django.db import models
from Customer import Customer

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders', help_text="The customer who placed the order")
    order_date = models.DateTimeField(auto_now_add=True, help_text="The date and time the order was placed")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total amount for the order")

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"


class Meta:
      app_label = 'Order' # add app name here

#in order the thing linking it to the Customer model  is the 
#customer foreign key , the on_delete=models.CASCADE ensures that if a customer is deleted so is the order.
#the relationship is one to many relationship because one customer has multiple orders.

