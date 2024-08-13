from faker import Faker
import factory
from your_project.models import Product

fake = Faker()

class ProductFactory(factory.Factory):
    class Meta:
        model = Product
    
    id = factory.Sequence(lambda n: n)
    name = factory.LazyAttribute(lambda x: fake.word())
    description = factory.LazyAttribute(lambda x: fake.text())
    price = factory.LazyAttribute(lambda x: round(fake.random_number(decimal_places=2), 2))
    category = factory.LazyAttribute(lambda x: fake.word())
    availability = factory.LazyAttribute(lambda x: fake.boolean())
