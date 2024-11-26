from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100, help_text="Full name of the customer")
    email = models.EmailField(unique=True, help_text="Email address of the customer")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Time when the customer was created")


#to convert the objects being called to string
    def __str__(self):
        return self.name

