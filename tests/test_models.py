import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Product

@pytest.mark.django_db
def test_read_product():
    # Setup
    product = Product.objects.create(
        name='Test Product',
        description='A description of the test product',
        price=19.99,
        category='Electronics',
        availability=True
    )
    
    # Create an instance of the APIClient
    client = APIClient()

    # Send a GET request to retrieve the product
    response = client.get(reverse('product-detail', kwargs={'pk': product.pk}))

    # Assert the response status code
    assert response.status_code == status.HTTP_200_OK

    # Assert the response data
    assert response.data['name'] == 'Test Product'
    assert response.data['description'] == 'A description of the test product'
    assert response.data['price'] == '19.99'
    assert response.data['category'] == 'Electronics'
    assert response.data['availability'] == True
