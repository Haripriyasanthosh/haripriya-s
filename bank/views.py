from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from  .models import *
from django.contrib import messages


from django.shortcuts import render, redirect, get_object_or_404


from django.core.mail import send_mail
from django.conf import settings



from .models import BloodBank, BloodProduct
from .models import Donor
from .models import BloodProduct
from .models import FoodProduct





from django.utils import timezone  # Import the timezone module
from datetime import timedelta  # Import timedelta for date manipulation



# Create your views here.

def new_password(request):
    request.session['lid']
    if 'new_p' in request.POST:
        np=request.POST['np']
        cp=request.POST['cp']
        if np == cp:
            
            lg=login.objects.get(pk=request.session['lid'])
            lg.passwword=cp
            lg.save()
            return HttpResponse("<script>alert('Password Successfully Changed.');window.location='/login_form'</script>")
        else:
            return HttpResponse("<script>alert('Confirm password mismatched.');window.location='/new_password'</script>")
    return render(request,'new_password.html')

def enter_otp(request):
    print("#############", request.session['otp'])
    if 'et_otp' in request.POST:
        otp_v=int(request.POST['otp_v'])
        if otp_v == request.session['otp']:
            return HttpResponse("<script>alert('Successfully Verified.');window.location='/new_password'</script>")
        else:
            return HttpResponse("<script>alert('Invalid OTP.');window.location='/enter_otp'</script>")
   

    return render(request,'enter_otp.html')

def forgot_password(request):
    import random
    otp = random.randint(1000, 9999)
    request.session['otp'] = otp
    print(random.randint(1000, 9999))
    if 'forgot' in request.POST:
        uname = request.POST['uname']
        email = request.POST['email']
        try:
            uu = login.objects.get(username=uname)
            if uu:
                if uu.type == "user":
                    try:
                        ee = users.objects.get(email=email)
                        if ee:
                            request.session['lid'] = uu.pk
                            send_mail(
                                'Forgot Password Request' + uname,
                                'Your OTP(One Time Password) is: ' + str(otp),
                                'aquaworld8547@gmail.com',
                                [email],
                                fail_silently=False,
                            )
                            return HttpResponse("<script>alert('Check Your Email.');window.location='/enter_otp'</script>")
                        else:
                            return HttpResponse("<script>alert('Invalid Email');window.location='/forgot_password'</script>")
                    except:
                        return HttpResponse("<script>alert('Invalid Email');window.location='/forgot_password'</script>")
                elif uu.type == "donor":
                    print('helloooooooooooooooooooooooooooo')
                    try:
                        ee1 = Donor.objects.get(email=email)
                        print(ee1.first_name, '//////////////////////////////////')
                        if ee1:
                            print('gggggggggggggggggggggggggggg')
                            request.session['lid'] = uu.pk
                            send_mail(
                                'Forgot Password Request' + uname,
                                'Your OTP(One Time Password) is: ' + str(otp),
                                'aquaworld8547@gmail.com',
                                [email],
                                fail_silently=False,
                            )
                            return HttpResponse("<script>alert('Check Your Email.');window.location='/enter_otp'</script>")
                        else:
                            return HttpResponse("<script>alert('Invalid Email');window.location='/forgot_password'</script>")
                    except:
                        return HttpResponse("<script>alert('Invalid Email');window.location='/forgot_password'</script>")
            else:
                return HttpResponse("<script>alert('Invalid Username.');window.location='/forgot_password'</script>")
        except:
            return HttpResponse("<script>alert('Invalid Username.');window.location='/forgot_password'</script>")
    return render(request, 'forgot_password.html')
        
    























def index(request):
    return render(request, 'index.html')

def bank_index(request):
    return render(request, 'bank_index.html')
def bank_register(request):
    return render(request, 'bank_register.html')
def donor_index(request):
    return render(request, 'donor_index.html')
def donor_register(request):
    return render(request, 'donor_register.html')








# def about(request):
#     return render(request,'about.html')
# def services(request):
#     return render(request,'services.html')
# def register(request):
#     if request.method == "POST":
#         username = request.POST.get("email")
#         email = request.POST.get("email")
#         fname = request.POST.get("fullName")
#         phone=request.POST.get("phone")
#         password = request.POST.get("password")
#         cpassword = request.POST.get("confirmPassword")
        
#         if (
#             CustomUser.objects.filter(username=username).exists()
#             or CustomUser.objects.filter(email=email).exists()
#         ):
#             messages.error(request, "Email or Username Already Exists")
#             return render(request, "signin.html")
#         else:
#             user = CustomUser.objects.create_user(
#                 username=username,
#                 first_name=fname,
#                 email=email,
#                 password=password,
#                 is_doctor=True,
#             )
#             user.save()
#             return redirect('login')
#     else:
#         return render(request, "register.html")
    
# def contact(request):
#     return render(request,'contact.html')
def login_form(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if request.method == "POST":
        try:
            q = login.objects.get(username=username, passwword=password)
            request.session['id'] = q.pk
            if q:
                if q.type == 'admin':
                    return HttpResponse("<script>alert('login successful');window.location='/admin_home'</script>")
                elif q.type == 'user':
                    qr = users.objects.get(login_id=request.session['id'])
                    if qr:
                        request.session['uid'] = qr.pk
                    return HttpResponse("<script>alert('login successful');window.location='/user_home'</script>")
                elif q.type == 'bank':
                    qb = bank_reg.objects.get(login_id=request.session['id'])
                    if qb:
                        request.session['bank_id'] = qb.pk
                    return HttpResponse("<script>alert('login successful');window.location='/bank_home'</script>")
                elif q.type == 'donor':
                    qdd = Donor.objects.get(login_id=request.session['id'])
                    print("kkkkkkkkkkkkkkkkkkkk",qdd)
                    if qdd:
                        request.session['donor_id'] = qdd.pk
                    return HttpResponse("<script>alert('login successful');window.location='/donor_home'</script>")
                elif q.type == 'recipient':
                    qr = recipient.objects.get(login_id=request.session['id'])
                    if qr:
                        request.session['recipient_id'] = qr.pk
                    return HttpResponse("<script>alert('login successful');window.location='/recipient_register'</script>")
        except:
            return HttpResponse("<script>alert('Invalid Username or Password');window.location='/login'</script>")     
    return render(request,"login_form.html")
            
def user_register(request):
    if request.method == "POST":
        fullname = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']
        blood_type = request.POST['blood_type']
        u_phone = request.POST['phone']
        address = request.POST['address']
        mylo = login(username=email,passwword=password,type='user')
        print("haiiiiiiiiiiiiiiiiiii")
        mylo.save()
        myuse=users(full_name=fullname,email=email,blod_type=blood_type,u_phone=u_phone,address=address,login=mylo)
        myuse.save()
        return HttpResponse("<script>alert('registration sucessfully');window.location='/login_form'</script>")
    return render(request,'user_register.html')


def recipient_register(request):
    if request.method == 'POST':
        recipient_name = request.POST['name']
        recipient_email =request.POST['email']
        recipient_phone =request.POST['phone']
        recipient_address = request.POST['address']
        password = request.POST['password']
        mylo = login(username=recipient_email,passwword=password,type='recipient')
        mylo.save()
        myuse=recipient(recipient_name=recipient_name,recipient_email=recipient_email,recipient_phone=recipient_phone,recipient_address=recipient_address,login=mylo)
        myuse.save()
        return HttpResponse("<script>alert('registration sucessfully');window.location='/login_form'</script>")
    return render(request,'user_register.html')
    
    

def admin_home(request):
    return render(request,'admin_home.html')

def adminmanagebank(request):
    if request.method=="POST":
        bank_name = request.POST['name']
        bank_email =request.POST['email']
        bank_phone =request.POST['phone']
        bank_address = request.POST['address']
        password = request.POST['password']
        mylo = login(username=bank_email,passwword=password,type='bank')
        mylo.save()
        myuse=bank_reg(bank_name=bank_name,bank_email=bank_email,bank_phone=bank_phone,bank_address=bank_address,login=mylo)
        myuse.save()
        return HttpResponse("<script>alert('register successfully');window.location='/adminmanagebank'</script>")
    return render(request, 'admin_bank.html')

def admin_view_bank_details(request):
    docview=bank_reg.objects.all()
    return render(request,'admin_view_bank_details.html',{'docview':docview})


def admin_view_blood_group_status(request):
    docview=blood_group.objects.all()
    return render(request,'admin_view_blood_group_status.html',{'docview':docview})





def delete_bank(request):
    docview=bank_reg.objects.filter(login_id=id)
    docview.delete()
    qr=login.objects.get(id=id)
    qr.delete()
    return HttpResponse("<script>alert('delete successfully');window.location='/admin_home'</script>")



def adminadddonor(request):
    if request.method =="POST":
        full_name=request.POST['name']
        email=request.POST['email']
        blod_type=request.POST['blod_type']
        phone=request.POST['phone']
        address=request.POST['address']
        password=request.POST['password']
        mylo = login(username=email,passwword=password,type='donor')
        mylo.save()
        myuse=Donor(full_name=full_name,email=email,blod_type=blod_type,phone=phone,address=address,login=mylo)
        myuse.save()
        return redirect('success_message')
    return render(request, 'admin_donor.html')
    #     return HttpResponse("<script>alert('register successfully');window.location='/adminadddonor'</script>")
    # return render(request, 'success_message.html')

        
    
    

def admin_view_donor_details(request):
    docview=Donor.objects.all()
    return render(request,'admin_view_donor_details.html',{'docview':docview}) 


def donor_home(request):
    return render(request,'donor_home.html')
    
def logout(request):
    return render(request,'logout.html')    
        
        
        
def delete_donor(request,id):
    docview=Donor.objects.filter(login_id=id)
    docview.delete()
    qr=login.objects.get(id=id)
    qr.delete()
    return HttpResponse("<script>alert('delete successfully');window.location='/admin_home'</script>")






        
        
        
        
        
        
#################bank

def bank_home(request):
    return render(request, 'bank_home.html')

def bank_add_blood_group(request):
    if request.method=="POST":
        b_group = request.POST['b_group']
        b_details =request.POST['b_details']
        b_expiry =request.POST['b_expiry']
        b_status = request.POST['b_status']
        b_name = request.POST['b_name']
        # mylo = login(username=bank_email,passwword=password,b_status='available',b_expiry=b_expiry)
        # mylo.save()
        myuse=blood_group(b_group=b_group,b_details=b_details,b_expiry=b_expiry,b_name=b_name,b_status='available',bank_reg_id=request.session['bank_id'] )
        myuse.save()
        return HttpResponse("<script>alert('inserted successfully');window.location='/bank_add_blood_group'</script>")
    return render(request, 'bank_add_blood_group.html')









##########################users################




def user_home(request):
    return render(request, 'user_home.html')



def user_view_blood_booking(request):
    request=blood_booking.objects.all() 
    return render(request, 'blood_booking.html') 

def user_update_blood_booking(request):
    request=blood_booking.objects.all()
    return render(request, 'blood_booking.html')      



###########update bank######
def admin_update_bank_details(request):
    qr=bank_reg.objects.get(login_id=request.session['login_id'])
    if request.method == 'POST':
        qr.bank_name=request.POST['bank_name']
        qr.bank_email=request.POST['bank_email']
        qr.bank_phone=request.POST['bank_phone']
        qr.bank_address=request.POST['bank_address']
        qr.save()
        return HttpResponse("<script>alert('updated successfully');window.location='/admin_home'</script>")
    return render(request, 'admin_update_bank.html', {'bank_up':qr})

    





    
        

######################update donor#######
def admin_update_donor_details(request):
    qr=Donor.objects.get(login_id=request.session['login_id'])


    
    

# def blood_bookingss(request):
#     qr=blood_booking.objects.get(donor_id=request.session['donor_id'])
#     if request.method == 'POST':
#         qr.b_litres = request.POST['b_litres'] 
#         qr.b_date = request.POST['b_date']
#         qr.b_status = request.POST['b_status']
#         myuse=blood_booking(b_litres=b_litres,b_date=b_date,b_status='available',blood_booking_id=request.session['donor_id'] )
#         myuse.save()
#         return HttpResponse("<script>alert('registration sucessfully');window.location='/blood_booking'</script>")
#     return render(request, 'blood_booking.html')
      
      

      
      
      
      

      
def request_list(request,id):
    if request.method== 'POST':
        b_litres=request.POST['bloodLiters']
        b_date=request.POST['b_date']
        myuse=blood_booking(b_litres=b_litres,b_date=b_date,b_status="Pending", user_id=request.session['uid'] ,donor_id=id)
        myuse.save()
        return HttpResponse("<script>alert('Requested');window.location='/user_home'</script>")
    return render(request,'request_list.html')
    
# def donor_update_profile(request):
#     donor_up=Donor.objects.get(id=request.session['donor_id'])
#     if request.method == 'POST':
#         donor_up.full_name = request.POST['name'] 
#         donor_up.email = request.POST['email']
#         donor_up.phone = request.POST['phone']
#         donor_up.address = request.POST['address'] 
#         donor_up.save()
#         return HttpResponse("<script>alert('Your Profile Updated Sucessfully');window.location='/donor_update_profile'</script>")
#     return render(request, 'donor_update_profile.html',{'donor_up':donor_up})

def donor_update_profile(request):
    # Check if donor_id is in session
    donor_id = request.session.get('donor_id')
    if donor_id:
        try:
            donor_up = Donor.objects.get(id=donor_id)
        except Donor.DoesNotExist:
            return HttpResponse("<script>alert('Donor does not exist');window.location='/login'</script>")
        
        if request.method == 'POST':
            donor_up.full_name = request.POST.get('name', '') 
            donor_up.email = request.POST.get('email', '')
            donor_up.phone = request.POST.get('phone', '')
            donor_up.address = request.POST.get('address', '') 
            donor_up.save()
            return HttpResponse("<script>alert('Your Profile Updated Successfully');window.location='/donor_update_profile'</script>")
        return render(request, 'donor_update_profile.html', {'donor_up': donor_up})
    else:
        return HttpResponse("<script>alert('Please login first');window.location='/login'</script>")





















 
 
 
 
  
def user_update_profile(request):
    user_up = users.objects.get(id=request.session['uid']) 
    if request.method == 'POST':
        user_up.full_name = request.POST['name'] 
        user_up.email = request.POST['email']
        user_up.blood_type = request.POST['blood_type']
        user_up.phone = request.POST['phone']
        user_up.password = request.POST['password'] 
        user_up.save()
        return HttpResponse("<script>alert('Your Profile Updated Sucessfully');window.location='/user_update_profile'</script>")
    return render(request, 'user_update_profile.html',{'user_up':user_up}) 
       
        

    
    
    #     qr=blood_booking.objects.get(donor_id=request.session['donor_id'])
#     if request.method == 'POST':
#         qr.b_litres = request.POST['b_litres'] 
#         qr.b_date = request.POST['b_date']
#         qr.b_status = request.POST['b_status']
#         myuse=blood_booking(b_litres=b_litres,b_date=b_date,b_status='available',blood_booking_id=request.session['donor_id'] )
#         myuse.save()
#         return HttpResponse("<script>alert('registration sucessfully');window.location='/blood_booking'</script>")
#     return render(request, 'blood_booking.html')

    





   
   
###############################user profile #############################

    
    
    
    
    
    
    
    # def admin_update_donor_deatils(request):
    #      qr=bank_reg.objects.get(login_id=request.session['login_id'])
    #      if request.method=='POST':
    #         qr.full_name=request.POST['full_name']
    #         qr.email=request.POST['email']
    #         qr.blod_type=request.POST['blod_type']
    #         qr.phone=request.POST['phone']
    #         qr.address=request.POST['address']
    #         qr.save()
    #         return HttpResponse("<script>alert('updated successfully');window.location='/donor_home'</script>")
    #      return render(request, 'admin_update_donor.html', {'donor_up':qr})
     
        
        
def search_blood_group(request):
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    dview=Donor.objects.all()
    print(dview,"haiiiiiiiiiiiiiiiiiiiiiiii")
    return render(request, 'search_blood_group.html', {'dview': dview})
        
      


def donor_view_blood_request(request):
    docview=blood_booking.objects.filter(donor_id=request.session['donor_id'])
    print(docview,"haiiiiiiiiiiiii")
    # docview=blood_booking.objects.all
    return render(request, 'donor_view_blood_request.html',{'docview': docview}) 

def reject_req(request,id,user_id):
    qview=blood_booking.objects.get(id=id)
    qview.b_status='notavailable'
    qview.save()
    qv = users.objects.filter(id=user_id)
    if qv.exists():
        user = qv.first()
        eid = user.email
        print(eid)
        subject = 'Blood Request'
        message = f"Sir/Madam,\n Your Blood Request Rejected please send Request to Another Person "
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [eid]
        send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("<script>alert('sucessfully');window.location='/donor_home'</script>")

def accept_req(request,id,user_id):
    qviews=blood_booking.objects.get(id=id)
    qviews.b_status='available'
    qviews.save()
    qv = users.objects.filter(id=user_id)
    if qv.exists():
        user = qv.first()
        eid = user.email
        print(eid)
        subject = 'Blood Request'
        message = f"Sir/Madam,\n Your Blood Request Accepted. Thanq "
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [eid]
        send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("<script>alert('sucessfully');window.location='/donor_home'</script>")
                  
    
def donor_view_request_history(request):
    docview=blood_booking.objects.filter(donor_id=request.session['donor_id'],b_status='available')
    print(docview,"haiiiiiiiiiiiii")
    # docview=blood_booking.objects.all
    return render(request, 'donor_view_request_history.html',{'docview': docview}) 







def bank_view_donor_list(request):
    donors = Donor.objects.all()
    return render(request, 'bank_view_donor_list.html', {'donors': donors})


# def bank_view_donor_list(request):
#     donor_id = request.session.get('donor_id')
#     if donor_id:
#         docview = Donor.objects.filter(donor_id=donor_id, b_status='available')
#         print(docview, "haiiiiiiiiiiiii")  # Debugging statement
#         return render(request, 'bank_view_donor_list.html', {'docview': docview})
#     else:
#         # Handle the case where 'donor_id' is not set in the session
#         # You can redirect the user to the login page or handle it based on your application's logic
#         return HttpResponse("Donor ID not found in session.")

def logout(request):
    request.session.clear()
    return redirect('login_form')  # redirect  to login page   for logged out  users   only 



def bank_view_blood_groups(request):
    bank_reg_entries = bank_reg.objects.values('blood_group')
    return render(request, 'bank_view_blood_groups.html', {'bank_reg_entries': bank_reg_entries})                                                                      

    
def self_donation_form(request):
    if request.method == 'POST':
        model= SelfDonationForm(request.POST)
        if model.is_valid():
            messages.success(request, 'You have registered successfully!')
            return redirect('bank_header.html')  # Redirect to appropriate view
            # Process the form data
            # Save the form data to the database or perform any other actions
            pass  # Placeholder for processing form data
    else:
        model= SelfDonationForm()

    return render(request, 'self_donation_form.html', {'form': model})    
# def donation_drive_list(request):
#     drives = DonationDrive.objects.all()
#     return render(request, 'donation_drive_list.html', {'drives': drives})




# def add_blood_product(request):
#    if request.method == 'POST':
#          donor_id = request.POST.get('donor_id')
#          blood_type = request.POST.get('blood_type')
#          product_type = request.POST.get('product_type')
#          expiration_date = request.POST.get('expiration_date')

#          BloodProduct.objects.create(
#             donor_id=donor_id,
#             blood_type=blood_type,
#             product_type=product_type,
#             expiration_date=expiration_date
#         )
#          return render(request, 'add_blood_product.html')


from django.utils import timezone
from datetime import timedelta

# In your views.py file

    














def display_inventory(request):
    inventory = BloodProduct.objects.all()
    return render(request, 'inventory.html', {'inventory': inventory})




def list_donors(request):
    # Retrieve all donors
    donors = Donor.objects.all()
    return render(request, 'list_donors.html', {'donors': donors})



def registration_success(request):
    # Get the newly registered donor (you may need to modify this logic based on your registration process)
    donor = Donor.objects.latest('id')  # Assuming 'id' is the primary key field of Donor model

    # Display a success message
    messages.success(request, 'Successfully registered!')

    # Redirect to a page with details and awareness about blood donation
    return render(request, 'registration_success.html', {'donor': donor})


def success_message(request):
    return render(request, 'success_message.html')


def awareness_session(request):
    # Logic to retrieve awareness session details (date, time, doctor details, etc.)
    # You can retrieve this information from the database or define it directly in the view
    session_details = {
        'date': '2024-03-20',
        'time': '10:00 AM',
        'doctor': 'Dr. John Doe',
        # Add more details as needed
    }
    return render(request, 'awareness_session.html', {'session_details': session_details})


def book_slot(request):
    # Logic to handle slot booking
    # This view will handle the form submission for booking a slot
    if request.method == 'POST':
        # Process the form data to book a slot
        # You may need to create a form for booking slots and handle the form submission here
        pass  # Placeholder for form processing logic
    return render(request, 'book_slot.html')







def add_blood_product(request):
    # Check for upcoming expiry dates
    upcoming_expiry_products = BloodProduct.objects.filter(expiration_date__lte=timezone.now() + timedelta(days=7))

    # Prepare warning message for upcoming expiry products
    expiry_warning_message = None
    if upcoming_expiry_products.exists():
        expiry_warning_message = []
        for product in upcoming_expiry_products:
            expiry_warning_message.append((product.donor_id, product.product_type, product.expiration_date))

    if request.method == 'POST':
        # Process the form data to add a new blood product
        # This logic remains unchanged
        pass

    # Render the template with the expiry warning message
    return render(request, 'add_blood_product.html', {'expiry_warning_message': expiry_warning_message})



def blood_bank_view_requests(request):
    user_details = users.objects.all()
    return render(request, 'blood_bank_view_requests.html', {'user_details': user_details})


def food_menu(request):
    food_items = FoodProduct.objects.filter(available=True)
    return render(request, 'food_menu.html', {'food_items': food_items})


def order_food(request):
    if request.method == 'POST':
        # Retrieve the selected item's name and quantity from the form data
        selected_item_name = request.POST.get('selected_items')
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not provided

        # Retrieve the corresponding FoodProduct object from the database
        selected_item = get_object_or_404(FoodProduct, name=selected_item_name)

        # Redirect to the order success page with the selected item's ID and quantity
        return redirect('order_success', selected_item_id=selected_item.id, quantity=quantity)
    else:
        # If the request method is GET, render the food menu page
        food_items = FoodProduct.objects.filter(available=True)
        return render(request, 'food_menu.html', {'food_items': food_items})
    
    
    
def order_success(request, selected_item_ids):
    selected_items = []
    for item_id in selected_item_ids:
        try:
            selected_item = FoodProduct.objects.get(id=item_id)
            selected_items.append(selected_item)
        except FoodProduct.DoesNotExist:
            pass  # You may want to handle this case differently, like logging it or displaying an error message
    return render(request, 'order_success.html', {'selected_items': selected_items})


# def food_product_list(request):
#     food_products = FoodProduct.objects.all()
#     return render(request, 'food_product_list.html', {'food_products': food_products})

# def food_product_detail(request, pk):
#     food_product = get_object_or_404(FoodProduct, pk=pk)
#     return render(request, 'food_product_detail.html', {'food_product': food_product})

# def order_list(request):
#     orders = Order.objects.all()
#     return render(request, 'order_list.html', {'orders': orders})

# # Add views for generating reports