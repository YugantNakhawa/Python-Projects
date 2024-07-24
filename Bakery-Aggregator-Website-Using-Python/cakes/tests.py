from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Cake


class CakeTest(TestCase):

    def setUp(self): # filling user data (credentials)
        self.user = get_user_model().objects.create_user(
            username = 'cake',
            email = 'cake@cake.com',
            password = 'secret',
        )

        self.cake = Cake.objects.create(    # filling cake model fields
            name = 'cake1',
            weight = '1kg',
            description = 'anything',
            price = '30',
            image_url = 'https://forexample.jpg',
            cake_available = 'True',
        )

    def test_string_representation(self):
        cake = Cake(name='new cake')
        self.assertEqual(str(cake), cake.name)

    def test_cake_model_fields_content(self):
        self.assertEqual(f'{self.cake.name}', 'cake1')
        self.assertEqual(f'{self.cake.weight}', '1kg')
        self.assertEqual(f'{self.cake.description}', 'anything')
        self.assertEqual(f'{self.cake.price}', '30')
        self.assertEqual(f'{self.cake.image_url}', 'https://forexample.jpg')
        self.assertEqual(f'{self.cake.cake_available}', 'True')

    def test_cake_list_view_for_logged_in_user(self):
        self.client.login(username = 'cake', email='cake@cake.com', password='secret')
        request = self.client.get(reverse('list'))
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, 'cake1')
        self.assertContains(request, '30')

    def test_cake_list_view_for_anonymous_user(self): # a user who doesn't have an account on our site
        self.client.logout()
        request = self.client.get(reverse('list'))
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, 'cake1')
        self.assertContains(request, '30')

    def test_cake_detail_view_for_logged_in_user(self):
        self.client.login(username = 'cake', email='cake@cake.com', password='secret')
        request = self.client.get(reverse('detail', args='1'))
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, 'cake1')
        self.assertContains(request, '30')

    def test_cake_detail_view_for_anonymous_user(self):
        self.client.logout()
        request = self.client.get(reverse('detail', args='1'))
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, 'cake1')
        self.assertContains(request, '30')

    def test_checkout_view_for_logged_in_user(self):
        self.client.login(username = 'cake', email='cake@cake.com', password='secret')
        request = self.client.get(reverse('checkout', args='1'))
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, 'cake1')
        self.assertContains(request, '30')

    def test_checkout_view_for_anonymous_user(self):
        self.client.logout()
        request = self.client.get(reverse('checkout', args='1'))
        self.assertEqual(request.status_code, 302)
        self.assertRedirects(request, '/accounts/login/?next=/1/checkout/') # redirects the user to login page

    def test_cake_when_available(self):  # a second cake is created (out of stock)
        request = self.client.get(reverse('detail', args = '1'))
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, 'Buy Now') 
        self.assertNotContains(request, 'Out of Stock !') # should not be there
        
    def test_cake_when_out_of_stock(self):  # a second cake is created which is out of stock
            cake = Cake.objects.create(
                name = 'new cake',
                weight = '1kg',
                description = 'anything',
                price = '300',
                image_url = 'https://forexample.jpg',
                cake_available = 'False',   # out of stock when False
            )
            request = self.client.get(reverse('detail', args = '2'))
            self.assertEqual(request.status_code, 200)
            self.assertContains(request, 'Out of Stock !')
            self.assertNotContains(request, 'Buy Now') # buy now option is no longer present
            