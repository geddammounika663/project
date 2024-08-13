import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Product

@pytest.mark.django_db
def test_list_all_products():
    # Setup: Create multiple product instances
    product1 = Product.objects.create(
        name='Product 1',
        description='Description 1',
        price=19.99,
        category='Gadgets',
        availability=True
    )
    product2 = Product.objects.create(
        name='Product 2',
        description='Description 2',
        price=29.99,
        category='Accessories',
        availability=False
    )
    
    # Create an instance of the APIClient
    client = APIClient()

    # Send a GET request to the list all endpoint
    response = client.get(reverse('product-list'))

    # Assert the response status code
    assert response.status_code == status.HTTP_200_OK

    # Assert that the response data contains the created products
    response_data = response.json()
    assert len(response_data) == 2  # Ensure there are two products in the response
    assert any(product['name'] == 'Product 1' for product in response_data)
    assert any(product['name'] == 'Product 2' for product in response_data)
