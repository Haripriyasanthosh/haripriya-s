from django.db import models
from django.contrib.auth.models import User 



                    

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=255)
    passwword = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    
class users(models.Model):
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    blod_type = models.CharField(max_length=100)
    u_phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
    
 
class bank_reg(models.Model):
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=100)
    bank_email = models.CharField(max_length=100)
    bank_phone = models.CharField(max_length=100)
    bank_address = models.CharField(max_length=100)
    
    
    
    
    
    
    
    
class blood_group(models.Model):
    b_group = models.CharField(max_length=100)
    b_deatils = models.CharField(max_length=100)
    b_expiry = models.CharField(max_length=100)
    b_status = models.CharField(max_length=100)
    b_name = models.CharField(max_length=50)
    bank_reg=models.ForeignKey(bank_reg,on_delete=models.CASCADE)


class bank_recipient(models.Model):
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    blod_type = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    

   
   
    
class Donor(models.Model):
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    blod_type = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    last_donation_date = models.DateField(null=True, blank=True)  
    
class recipient(models.Model):
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    blod_type = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
# class booking(models.Model):
#     login=models.ForeignKey(login,on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     blod_type = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)
    
class blood_booking(models.Model): 
    user = models.ForeignKey(users,on_delete=models.CASCADE)
    donor= models.ForeignKey(Donor, on_delete=models.CASCADE)
    b_litres = models.CharField(max_length=20)
    b_date = models.DateField(auto_now_add=True )
    b_status = models.CharField(max_length=20)
    
    
    
    
    
# class DonationCamp(models.Model):
#     date = models.DateField()
#     time = models.TimeField()
#     allow_self_donation = models.BooleanField(default=True)


class SelfDonationForm(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    age = models.IntegerField(max_length=50)
    blood_group = models.CharField(max_length=5,choices=[
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ])
    willing_to_donate = models.BooleanField()
    date_of_donation = models.DateField()
    last_donated_date = models.DateField() 
class DonationDrive(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
  
class DonorRegistration(models.Model):
    users = models.ForeignKey(users, on_delete=models.CASCADE)
    donation_drive = models.ForeignKey(DonationDrive, on_delete=models.CASCADE)
    # Add more fields as needed, like contact information, health details, etc.
    
    
    



class BloodProduct(models.Model):
    donor_id = models.CharField(max_length=50)
    blood_type = models.CharField(max_length=10)
    product_type = models.CharField(max_length=50)
    expiration_date = models.DateField()

    def __str__(self):
        return f"Donor ID: {self.donor_id}, Blood Type: {self.blood_type}, Product Type: {self.product_type}, Expiration Date: {self.expiration_date}"

class BloodBank(models.Model):
    inventory = models.ManyToManyField(BloodProduct)

    def __str__(self):
        return "Blood Bank Inventory"
    
    
    
class FoodProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    allergens = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name  

class Order(models.Model):
    food_product = models.ForeignKey(FoodProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Assuming minimum quantity is 1
    ordered_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.quantity * self.food_product.price

    def __str__(self):
        return f"Order #{self.id}: {self.food_product.name} - Quantity: {self.quantity}"
      

  
  



  
     
    

