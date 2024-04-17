"""blood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from.import views


urlpatterns = [
    
    # path('forgot_password/',views.forgot_password,name='forgot_password'),
    # path('enter_otp',views.enter_otp,name='enter_otp'),
     path('new_password',views.new_password,name='new_password'),
   
    # path('admin/', admin.site.urls),
     path('', views.index,name="index"),
     path('bank_index/',views.bank_index,name="bank_index"),
     path('bank_register/',views.bank_register,name="bank_register"),
     path('donor_index/',views.donor_index,name="donor_index"),
     path('donor_register/',views.donor_register,name="donor_register"),
     
     path('recipient_register/',views.recipient_register,name="recipient_register"),
     path('user_register/',views.user_register,name="register"),
     
     
     
     path('login_form/',views.login_form,name='login_form'),
     
     path('admin_home/',views.admin_home,name="admin_home"),
     path('donor_home/',views.donor_home,name="donor_home"),
     
     path('adminmanagebank/',views.adminmanagebank,name="adminmanagebank"),
     path('admin_view_bank_details/',views.admin_view_bank_details,name="admin_view_bank_details"),
     
     path('delete_bank/<id>',views.delete_bank,name="delete_bank"),
     path('delete_donor/<id>',views.delete_donor,name="delete_donor"),
     
     
     
    #  path('AdminManageDonor/',views.AdminManageDonor,name="AdminManageDonor"),
     path('admin_view_donor_details/',views.admin_view_donor_details,name="admin_view_donor_details"),
     path('admin_view_blood_group_status/',views.admin_view_blood_group_status,name="admin_view_blood_group_status"),
     path('admin_home/',views.admin_home,name="admin_home"),
     
     path('bank_home/',views.bank_home,name="bank_home"),
     path('bank_add_blood_group/',views.bank_add_blood_group,name="bank_add_blood_group"),
   
     path('user_home/',views.user_home,name="user_home"),
     path('search_blood_group/',views.search_blood_group,name="search_blood_group"),
     
     
     path('adminadddonor/',views.adminadddonor),
     
     
     path('admin_update_bank_details/<id>',views.admin_update_bank_details,name="admin_update_bank_details"),
     path('admin_update_donor_details/<id>',views.admin_update_donor_details,name="admin_update_donor_details"),
     
     path('search_blood_group/', views.search_blood_group, name='search_blood_group'),
     path('logout.html/', views.logout, name="logout.html"),
     path('blood_booking/', views.blood_booking, name='blood_booking'),
    path('user_view_blood_booking/', views.user_view_blood_booking, name='user-view_blood_booking'),
    path('user_update_blood_booking/', views.user_update_blood_booking, name='user_update_blood_booking'),
    path('request_list/<id>/', views.request_list,name='request_list'),
    path('donor_view_blood_request/', views.donor_view_blood_request, name='donor_view_blood_request'),
    path('accept_req/<id>/<user_id>/', views.accept_req, name='accept_req'),
    
    path('reject_req/<id>/<user_id>/', views.reject_req, name='reject_req'),
    
    path('donor_update_profile', views.donor_update_profile, name='donor_update_profile'),
    path('donor_view_request_history', views.donor_view_request_history, name='donor_view_request_history'),
    
    path('user_update_profile',views.user_update_profile, name='user_update_profile'),
    
    
    path('bank_view_donor_list', views.bank_view_donor_list, name='bank_view_donor_list'),
    path('bank_view_blood_groups', views.bank_view_blood_groups, name='bank_view_blood_groups'),
    path('add_blood_product/', views.add_blood_product, name='add_blood_product'),
    path('inventory', views.display_inventory, name='display_inventory'),
    path('list_donors', views.list_donors, name='list_donors'),
    path('registration_success', views.registration_success, name='registration_success'),
     path('success', views.success_message, name='success_message'),
    path('awareness', views.awareness_session, name='awareness_session'),
    path('book-slot', views.book_slot, name='book_slot'),
    path('blood_bank_view_requests/', views.blood_bank_view_requests, name='blood_bank_view_requests'),
    path('food_menu/', views.food_menu, name='food_menu'),
    
    path('order-food/<int:selected_item_id>/', views.order_food, name='order_food'),
    
    path('order_success/<int:selected_item_id>/', views.order_success, name='order_success'),
    
    
    
    
    # path('food-products/', views.food_product_list, name='food_product_list'),
    # path('food-products/<int:pk>/', views.food_product_detail, name='food_product_detail'),
    # path('orders/', views.order_list, name='order_list'),
    # path('admin/', admin.site.urls),
    # path('', include('blood.urls')), 
    
    
    
    
    path('logout', views.logout, name='logout')

    
    


    
       
     
    ]
     
    

        
         
