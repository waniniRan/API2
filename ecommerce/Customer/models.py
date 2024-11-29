from django.db import models




class Customer(models.Model):
    name = models.CharField(max_length=100, help_text="Full name of the customer")
    phone =models.CharField(max_lenght=15, null=True, blank=True)
    email = models.EmailField(unique=True, help_text="Unique email address of the customer")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Time when the customer was created")

    #change to string
    def __str__(self):
        return self.name
    
    
class Meta:
      app_label = 'Customer' # add app name here


# name- charField to store the customer's name
#email-An emails to store a unique email




