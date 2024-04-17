from django.test import TestCase,Client
from django.urls import reverse

from .models import bank_reg , login
from django.template import Context, Template
from .models import login


from .models import users,login



import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import BloodProduct
from .views import add_blood_product



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
# class BloodRequestViewTests(TestCase):
#     def setUp(self):
#         # Create some sample login instances
#         login_instance1 = login.objects.create(username='john_doe', password='password1')
#         login_instance2 = login.objects.create(username='jane_smith', password='password2')

#         # Create some sample users associated with the login instances
#         users.objects.create(
#             login=login_instance1,
#             full_name='John Doe',
#             email='johndoe@example.com',
#             blod_type='O+',  # Corrected typo here
#             u_phone='1234567890',
#             address='123 Main Street'
#         )
#         users.objects.create(
#             login=login_instance2,
#             full_name='Jane Smith',
#             email='janesmith@example.com',
#             blod_type='A-',
#             u_phone='0987654321',
#             address='456 Elm Street'
#         )

#     def test_blood_bank_view_requests(self):
#         # Access the blood request view
#         response = self.client.get(reverse('blood_bank_view__requests'))

#         # Check if the view returns a 200 OK status code
#         self.assertEqual(response.status_code, 200)

#         # Check if the users' details are present in the response context
#         self.assertQuerysetEqual(
#             response.context['users'],
#             ['<users: John Doe>', '<users: Jane Smith>'],
#             ordered=False
#         )

#         # Check if the users' details are displayed correctly in the response content
#         self.assertContains(response, 'John Doe')
#         self.assertContains(response, 'johndoe@example.com')
#         self.assertContains(response, 'O+')
#         self.assertContains(response, '1234567890')
#         self.assertContains(response, '123 Main Street')

#         self.assertContains(response, 'Jane Smith')
#         self.assertContains(response, 'janesmith@example.com')
#         self.assertContains(response, 'A-')
#         self.assertContains(response, '0987654321')
#         self.assertContains(response, '456 Elm Street')


# class ListDonorsTestCase(unittest.TestCase):
#     def setUp(self):
#         # Initialize WebDriver
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(10)  # Implicit wait to wait for elements to be found

#     def test_list_donors_page(self):
#         # Open the list donors page
#         self.driver.get("http://127.0.0.1:8000/list_donors")
#         print("Navigate to the list donors page")

#         # Wait for donors to load
#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, ".donor"))
#         )

#         # Find all donors on the page
#         donors = self.driver.find_elements_by_css_selector(".donor")

#         # Check if there are donors displayed
#         self.assertTrue(len(donors) > 0, "No donors found on the page")

#     def tearDown(self):
#         # Close the WebDriver
#         self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()


class BloodBankViewRequestsTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Implicit wait to wait for elements to be found

        # Create some sample user details
        users.objects.create(full_name='testuser1', email='test1@example.com')
        users.objects.create(full_name='testuser2', email='test2@example.com')
        # Add more sample users as needed

    def test_blood_bank_view_requests(self):
        # Open the URL
        self.driver.get("http://127.0.0.1:8000/blood_bank_view_requests")  # Replace with the actual URL

        # Find the user details elements
        user_details = self.driver.find_elements(By.CLASS_NAME, "user-details")  # Assuming each user detail is wrapped in an element with class "user-details"

        # Check if the correct number of user details are displayed
        self.assertEqual(len(user_details), 2)  # Assuming two users were created in setUp
        # Add more specific checks on user_details if needed

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()