from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from dish.tests.factories import DishFactory

class DishListAPITestCase(APITestCase):
    def setUp(self):
        self.url = reverse('dishes')
    def test_get_dish_list_success(self):
        dish_1 = DishFactory(name='Лагман', price=130)
        dish_2 = DishFactory()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)

        expected_data_1 = {
            'id': dish_1.id,
            'name': 'Рамен',
            'price': 150
        }

        expected_data_2 = {
            'id': dish_2.id,
            'name': dish_2.name,
            'price': dish_2.price
        }
        self.assertEqual(expected_data_1, response.data[1])
        self.assertEqual(expected_data_2, response.data[0])


    def test_post_dish_list_other_method_should_return_405(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 405)

        response = self.client.put(self.url)
        self.assertEqual(response.status_code, 405)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 405)
        

