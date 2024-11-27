#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()



from ecommerce import Customer, Order


customer= Customer.objects.create(name="John Doe", email="john.doe@example.com")


order = Order.objects.create(customer=customer, total_amount=150.00)


print(customer.orders.all())  # Output: <QuerySet [<Order: Order 1 by John Doe>]>
