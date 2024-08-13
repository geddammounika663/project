import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Product

@pytest.mark.django_db
def test_delete_product():
    # Setup: Create a product instance
    product = Product.objects.create(
        name='Product to Delete',
        description='Description to be deleted',
        price=19.99,
        category='Gadgets',
        availability=True
    )
    
    # Create an instance of the APIClient
    client = APIClient()

    # Send a DELETE request to the delete endpoint
    response = client.delete(reverse('product-detail', kwargs={'pk': product.pk}))

    # Assert the response status code
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Check that the product was actually deleted
    assert not Product.objects.filter(pk=product.pk).exists()
