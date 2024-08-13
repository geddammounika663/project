import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Product

@pytest.mark.django_db
def test_update_product():
    # Setup
    product = Product.objects.create(
        name='Old Product',
        description='Old description',
        price=29.99,
        category='Books',
        availability=True
    )
    
    # Create an instance of the APIClient
    client = APIClient()

    # Define the updated data
    updated_data = {
        'name': 'Updated Product',
        'description': 'Updated description',
        'price': 39.99,
        'category': 'Electronics',
        'availability': False
    }
    
    # Send a PUT request to update the product
    response = client.put(reverse('product-detail', kwargs={'pk': product.pk}), updated_data, format='json')

    # Assert the response status code
    assert response.status_code == status.HTTP_200_OK

    # Refresh the product instance from the database
    product.refresh_from_db()

    # Assert the updated values
    assert product.name == 'Updated Product'
    assert product.description == 'Updated description'
    assert product.price == 39.99
    assert product.category == 'Electronics'
    assert product.availability == False
