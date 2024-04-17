from django.test import TestCase
from django.urls import reverse
from bank.models import login, users

from django.template import Context, Template
# class LoginTestCase(TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(10)
        
#     def tearDown(self):
#         self.driver.quit()
#     def test_login(self):
#         self.driver.get('http://127.0.0.1:8000/login_form/')
#         email_input = self.driver.find_element(By.ID,'email')
#         password_input = self.driver.find_element(By.ID,'password')
#         login_button = self.driver.find_element(By.ID,'login')
#         email_input.send_keys('sharipriya531@gmail.com')
#         password_input.send_keys('sreekutty@23')
#         login_button.click() 
class BloodRequestViewTests(TestCase):
    def setUp(self):
        # Create some sample login instances
        login_instance1 = login.objects.create(username='john_doe', password='password1')
        login_instance2 = login.objects.create(username='jane_smith', password='password2')

        # Create some sample users associated with the login instances
        users.objects.create(
            login=login_instance1,
            full_name='John Doe',
            email='johndoe@example.com',
            blod_type='O+',  # Corrected typo here
            u_phone='1234567890',
            address='123 Main Street'
        )
        users.objects.create(
            login=login_instance2,
            full_name='Jane Smith',
            email='janesmith@example.com',
            blod_type='A-',
            u_phone='0987654321',
            address='456 Elm Street'
        )

    def test_blood_bank_view_requests(self):
        # Access the blood request view
        response = self.client.get(reverse('blood_bank_view__requests'))

        # Check if the view returns a 200 OK status code
        self.assertEqual(response.status_code, 200)

        # Check if the users' details are present in the response context
        self.assertQuerysetEqual(
            response.context['users'],
            ['<users: John Doe>', '<users: Jane Smith>'],
            ordered=False
        )

        # Check if the users' details are displayed correctly in the response content
        self.assertContains(response, 'John Doe')
        self.assertContains(response, 'johndoe@example.com')
        self.assertContains(response, 'O+')
        self.assertContains(response, '1234567890')
        self.assertContains(response, '123 Main Street')

        self.assertContains(response, 'Jane Smith')
        self.assertContains(response, 'janesmith@example.com')
        self.assertContains(response, 'A-')
        self.assertContains(response, '0987654321')
        self.assertContains(response, '456 Elm Street')
