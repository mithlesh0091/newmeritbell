from django.urls import path
from .import views
from django.conf.urls import url
from . import views
from django.urls import include, path
###############################
from django.urls import path
from. import views
####################################we######################################################


from django.urls import path
from .import views
from django.conf.urls import url
from . import views
from django.urls import include, path
##################
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


################################################################################################
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
####################

urlpatterns = [

    # path('', classroom.home, name='home'),
    path('', views.home, name='home'),

    path('register/', views.register, name='register'),
    path('customer_register/', views.customer_register.as_view(), name='customer_register'),
    path('employee_register/', views.employee_register.as_view(), name='employee_register'),
    path('consultancy_register/', views.consultancy_register.as_view(), name='consultancy_register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),



    path('School_register_form/', views.School_register_form, name='School_register_form'),
    # path('registerpage/', views.registerpage, name='resisterpage'),
    path('Collages_register_form/', views.Collages_register_form, name='Collages_register_form'),
    path('Consultancy_register_form/', views.Consultancy_register_form, name='Consultancy_register_form'),


    path('addyourschool/', views.addyourschool, name='addyourschool'),
     # path('reg_sign/', views.reg_sign, name='reg_sign'),
    # path('login/', views.login,name='login'),
    path('Basic_information', views.Basic_information, name='Basic_information'),

    path('admission_informationvarn', views.admission_informationvarn, name='admission_informationvarn'),
    path('Facility', views.Facility, name='Facility'),
    # path('infrastructure_and_campus', views.infrastructure_and_campus, name='infrastructure_and_campus'),
    path('Sports_curricular', views.Sports_curricular, name='Sports_curricular'),
    path('Awards_Recognition', views.Awards_Recognition, name='Awards_Recognition'),
    path('fee_Scructure', views.fee_Scructure, name='fee_Scructure'),
    path('Hostel_Accomodation', views.Hostel_Accomodation, name='Hostel_Accomodation'),
    path('create_myClass', views.create_myClass, name='create_myClass'),
    # path('sports_and_curr', views.sports_and_curr, name='sports_and_curr'),
    path('College_Basic_information/', views.College_Basic_information, name='College_Basic_information'),
    path('Admission_document_eligibility', views.Admission_document_eligibility, name='Admission_document_eligibility'),
    # path('logout/', views.logout,name='logout'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('collages/', views.collages,name='collages'),
    path('consultancy/', views.consultancy,name='consultancy'),

####################################menu-page###############################################


    path('School_dashboard/', views.School_dashboard, name='School_dashboard'),
    path('school/<int:pk>/', views.schools_details, name='schools_details'),
    # path('schools_details/', views.schools_details, name='schools_details'),
    path('Collage_dashboard/', views.Collage_dashboard, name='Collage_dashboard'),
    path('popular_states_school/', views.popular_states_school, name='popular_states_school'),
    path('popular_states_collages/', views.popular_states_collages, name='popular_states_collages'),
    path('schoolsp/', views.schoolsp, name='schoolsp'),
    path('collagep/', views.collagep, name='collagep'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('admin_contact/', views.admin_contact, name='admin_contact'),
    path('add_college/', views.add_college, name='add_college'),
    path('contactaddress/', views.contactaddress, name='contactaddress'),
    path('change_pass/', views.change_pass, name='change_pass'),

    path('main_register_form', views.main_register_form, name='main_register_form'),

    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),



##############################ENDmenu-page##################################################


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


