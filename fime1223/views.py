from django.contrib import messages
from django.contrib import messages
from django.contrib.auth.models import auth
from django.http import *
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
#
from fime1223.models import School
from django.http import HttpResponseRedirect
from .form import *
from .models import *
from .models import Admission_document_eligibility_info
from .models import Awards_Recognitioninfo
from .models import Hostel_Accomodationinfo
from .models import Sports_curricularinfo
from .models import admission_infonn
from .models import fee_structureinfo
from .models import Basic_informationinfo
from .models import Col_Basic_informationinfo
from .models import Facility_info
from .models import contactaddressinfo
from .models import Customer
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404


# from django.db.models.deletion import CASCADE





# from django.conf import settings
# from django.core.mail import send_mail
# Create your views here.
##############multiple####################
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import CustomerSignUpForm, EmployeeSignUpForm,ConsultancyForm
from django.contrib.auth.forms import AuthenticationForm
# from .models import User

#######################################################################contact for#########################
#views.py
from django.shortcuts import render, redirect

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# from myapp.forms import ContactForm
########################################################################################################
# from django.contrib.auth import get_user_model

#from django.contrib.auth.models import User ############chang on 29
from django.contrib.auth import get_user_model
User = get_user_model()
#######################################################
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
###############################
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from .tokens import account_activation_token
#from .form import  SignUpForm
from django.core.mail import send_mail
from django.conf import settings
# from .form import  signup
import datetime, time

###############################pagination############################
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
###########################ENDpagination############################


# Create your views here.
##############################
# UserModel = get_user_model()
# from .form import SignUpForm


# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'signup.html')
#     if request.method == 'POST':
#         form1 = SignUpForm(request.POST)
#         # print(form.errors.as_data())
#         if form1.is_valid():
#             User  = form1.save(commit=False)
#             User .is_active = False
#             User .save()
#             current_site = get_current_site(request)
#             mail_subject = 'Activate your account.'
#             message = render_to_string('acc_active_email.html', {
#                 'user': User ,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(User .pk)),
#                 'token': default_token_generator.make_token(User ),
#             })
#             to_email = 'mithkr.mith24@gmail.com'
#             email = EmailMessage(
#                 mail_subject, message, to=[to_email]
#             )
#             email.send()
#             return HttpResponse('Please confirm your email address to complete the registration')
#     else:
#         form1 = SignUpForm()
#     return render(request, 'signup.html', {'form1': form1})

# def signup(request, format=None):
#     if request.method == 'POST':
#       form = form(request.POST or None)
#       if form.is_valid():
#         User = form.save(commit=False)
#         User.is_active = False
#         User.save()
#         current_site = get_current_site(request)
#         subject = 'Ative sua conta Controller-Gastos'
#         uid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
#         token = account_activation_token.make_token(User)

#         # activation_link = "{0}/uid={1}/token={2}".format(current_site, uid, token)
#         activation_link = "{0}/activate/{1}/{2}".format(current_site, uid, token)

#         email_from = settings.EMAIL_HOST_USER
#         to_email = [form.cleaned_data.get('email')]
#         message = "Hello {0},\n {1}".format(User.username, activation_link)
#         # send_mail(subject, message, email_from, to_email)
#         return HttpResponse('Please confirm your email address to complete the registration using the link below<br>' + message)
#     else:
#         form = form()

#     return render(request, 'signup.html', {'form': form})


# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.profile.email_confirmed = True
#         user.save()
#         login(request, user)
#         return HttpResponse('Account activated successfully')
#         # time.sleep(5)
#         # return redirect('url_home')
#     else:
#         return render(request, 'account_activation_invalid.html')


# def activation_sent(request):
#     return render(request, 'acc_active_email.html.html')

# def activate(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = UserModel._default_manager.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')
################################################################

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['mithkr.mith24@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
#######################################################################contact form########################
def register(request):
    return render(request, '../templates/register.html')


class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        # user.is_active = False
        user = form.save()
        # email_subject = 'activate your account'
        # email_body = ''
        # email = EmailMessage(
        #       email_subject,
        #       email_body,
        #      'noreply@meritbell.com',
        #       [email],
        #      'from@example.com',
        #      ['to1@example.com', 'to2@example.com'],
        #      ['bcc@example.com'],
        #      reply_to=['another@example.com'],
        #      headers={'Message-ID': 'foo'},
        # )
        login(self.request, user)
        return redirect('login')


class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

class consultancy_register(CreateView):
    model = User
    form_class = ConsultancyForm
    template_name = '../templates/consultancy_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


def login_request(request):
    if request.method == 'POST':
        forms = AuthenticationForm(data=request.POST)
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            password = forms.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #current_user = request.user
                # //print (current_user.id)
                # user = User.objects.get(id=id)  # id is the view param
                # if hasattr(user, 'User'):
                #     print("Student")
                # else:  # hasattr(User, 'teacher')
                #     print("Teacher")
                # type_obj = User.objects.get(user=user)

                if user.is_authenticated and user.is_customer:
                    subject = 'welcome to Meritbell'
                    message = f'Hi {user.username}, thank you for login in Meritbell.com.'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [user.email, ]
                    send_mail( subject, message, email_from, recipient_list )
                    return redirect('School_dashboard')  # Go to student home

                elif user.is_authenticated and user.is_employee:
                    return redirect('Collage_dashboard')

                elif user.is_authenticated and user.is_consultancy:
                    return redirect('consultancy')


            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, '../templates/login.html',
                  context={'forms': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')


#############end multipleeeew###########

def home(request):
    return render(request, 'home.html', {'name': 'navin'});

def School_dashboard(request):
    return render(request, 'School_dashboard.html', {'name': 'navin'});

def Collage_dashboard(request):
    return render(request, 'Collage_dashboard.html');


def registerpage(request):
    return render(request, 'registerpage.html');

def School_register_form(request):
    return render(request, 'School_register_form.html');

def Collages_register_form(request):
    return render(request, 'Collages_register_form.html');


def Consultancy_register_form(request):
    return render(request, 'Consultancy_register_form.html');


def popular_states_collages(request):
    return render(request, 'popular_states_collages.html');








@login_required
def dashboard(request):

    return render(request, 'dashboard.html');


def collages(request):
    return render(request, 'collages.html');

def consultancy(request):
    return render(request, 'consultancy.html');


# def login(request):
# if request.method == 'POST':
# username = request.POST['username']
# password = request.POST['password']
# user = auth.authenticate(username=username, password=password)
# if user is not None:
# auth.login(request, user)
# # return redirect("dashboard")
# return render(request, 'dashboard.html');
# else:
# messages.info(request, 'invalid credentails')
# return redirect('login')
# return render(request, 'login.html');


#


# def reg_sign(request):
#     if request.method == 'POST':
#         form = reg_sign(request.POST)
#         if form.is_valid():
#             form.save()
#             return  HttpResponseRedirect('reg_sign')
#         else:
#             form = reg_sign()
#     return render(request, 'reg_sign.html',{form:form});


def addyourschool(request):
    if 'term' in request.GET:
        qs = School.objects.filter(title__icontains=request.GET.get('term'))
        titles = list()
        for school in qs:
            titles.append(school.title)
        titles = [product.title for product in qs]
        return JsonResponse(titles, safe=False)
    # if request.method == 'POST':
    #     schoolname = request.POST['schoolname']
    #     form_cfschpool = request.POST['form_cfschpool']
    #     Pessonname = request.POST['Pessonname']
    #     DesignationatSchool = request.POST['DesignationatSchool']
    #     password1 = request.POST['password']
    #     # password2 = request.POST['password2']
    #     email = request.POST['email']
    #     phone = request.POST['phone']
    #
    #     user = User.objects.created_user(schoolname=schoolname,Pessonname=Pessonname,DesignationatSchool=DesignationatSchool,password=password1,email=email,phone=phone)
    #     user.save()

    else:
        return render(request, 'addyourschool.html')


# def user_register(request):
# # if this is a POST request we need to process the form data
# template = 'register.html'

# if request.method == 'POST':
# # create a form instance and populate it with data from the request:
# form = RegisterForm(request.POST)
# # check whether it's valid:
# if form.is_valid():
# if User.objects.filter(username=form.cleaned_data['username']).exists():
# return render(request, template, {
# 'form': form,
# 'error_message': 'Username already exists.'
# })
# elif User.objects.filter(email=form.cleaned_data['email']).exists():
# return render(request, template, {
# 'form': form,
# 'error_message': 'Email already exists.'
# })
# elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
# return render(request, template, {
# 'form': form,
# 'error_message': 'Passwords do not match.'
# })
# else:
# # Create the user:
# user = User.objects.create_user(
# form.cleaned_data['username'],
# form.cleaned_data['email'],
# form.cleaned_data['password']
# )
# user.first_name = form.cleaned_data['first_name']
# user.last_name = form.cleaned_data['last_name']
# user.phone_number = form.cleaned_data['phone_number']
# user.save()
# messages.success(request, 'Thank you !! you have successfully registr your School on MeritBell.com')
# # Login the user
# # login(request, user)

# # redirect to accounts page:
# return HttpResponseRedirect('http://127.0.0.1:8000/register/')

# # No post data availabe, let's just show the page.
# else:
# form = RegisterForm()

# return render(request, template, {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('login')


def admission_informationvarn(request):
    # print("hello form is sucessfully submit")
    academic_year = request.POST["academic_year"]

    academic_start = request.POST['academic_start']
    academic_end = request.POST['academic_end']
    online_admission_application = request.POST['online_admission_application']
    Admission_page_url = request.POST['Admission_page_url']
    Facility_to_pay_admission_online = request.POST['Facility_to_pay_admission_online']
    Admission_open = request.POST['Admission_open']
    academic_contactpersonname = request.POST['academic_contactpersonname']
    academic_contactpersonmob = request.POST['academic_contactpersonmob']
    academic_contactpersonemail = request.POST['academic_contactpersonemail']
    admission_informationvarn = admission_infonn(academic_year=academic_year, academic_start=academic_start,
                                                 academic_end=academic_end,
                                                 online_admission_application=online_admission_application,
                                                 Admission_page_url=Admission_page_url,
                                                 Facility_to_pay_admission_online=Facility_to_pay_admission_online,
                                                 Admission_open=Admission_open,
                                                 academic_contactpersonname=academic_contactpersonname,
                                                 academic_contactpersonmob=academic_contactpersonmob,
                                                 academic_contactpersonemail=academic_contactpersonemail)

    admission_informationvarn.save()
    messages.success(request, 'save has been done')
    return render(request, "dashboard.html")


####################################aminities facility######################
def Facility(request):
    Activity_center = request.POST["Activity_center"]
    Computer_Labs = request.POST["Computer_Labs"]
    Library = request.POST["Library"]
    Laboratories = request.POST["Laboratories"]
    Canteen_Cafteria = request.POST["Canteen_Cafteria"]
    Transport_facilities = request.POST["Transport_facilities"]
    Sports_facilities = request.POST["Sports_facilities"]

    Medical_Facility = request.POST["Medical_Facility"]
    Lockers = request.POST["Lockers"]
    CCTV = request.POST["CCTV"]
    Audotorium_Seminar_Hall = request.POST["Audotorium_Seminar_Hall"]

    Gymnasiumn = request.POST["Gymnasiumn"]
    Play_Ground = request.POST["Play_Ground"]
    Drinking_Water = request.POST["Drinking_Water"]
    Music_Dance = request.POST["Music_Dance"]

    Stationary_Shop = request.POST["Stationary_Shop"]
    Wifi = request.POST["Wifi"]
    Car_Parking = request.POST["Car_Parking"]
    Bike_Cycle_Parking = request.POST["Bike_Cycle_Parking"]

    Security = request.POST["Security"]
    Guard = request.POST["Guard"]
    Fire_Extinguihev = request.POST["Fire_Extinguihev"]
    Hygienic = request.POST["Hygienic"]
    Washroom = request.POST["Washroom"]
    Hostel = request.POST["Hostel"]
    Swimming_Pool_Splash_Pool = request.POST["Swimming_Pool_Splash_Pool"]
    Others = request.POST["Others"]
    Facilities_Amenities_wsabi = request.POST["Facilities_Amenities_wsabi"]
    campusimages = request.POST["campusimages"]
    campusVideo = request.POST["campusVideo"]
    campus360 = request.POST["campus360"]
    Saftey = request.POST["Saftey"]
    conteen = request.POST["conteen"]
    Parking = request.POST["Parking"]
    facilitiesandinfra = request.POST["facilitiesandinfra"]
    youtubeurl1 = request.POST["youtubeurl1"]
    youtubeurl2 = request.POST["youtubeurl2"]
    youtubeurl3 = request.POST["youtubeurl3"]
    youtubeurl4 = request.POST["youtubeurl4"]
    txtEditor14 = request.POST["txtEditor14"]
    txtEditor15 = request.POST["txtEditor15"]
    txtEditor16 = request.POST["txtEditor16"]

    Facilityvarn = Facility_info(
        Activity_center=Activity_center,
        Computer_Labs=Computer_Labs,
        Library=Library,
        Laboratories=Laboratories,
        Canteen_Cafteria=Canteen_Cafteria,
        Transport_facilities=Transport_facilities,
        Sports_facilities=Sports_facilities,
        Medical_Facility=Medical_Facility,
        Lockers=Lockers,
        CCTV=CCTV,
        Audotorium_Seminar_Hall=Audotorium_Seminar_Hall,
        Gymnasiumn=Gymnasiumn,
        Play_Ground=Play_Ground,
        Drinking_Water=Drinking_Water,
        Music_Dance=Music_Dance,
        Stationary_Shop=Stationary_Shop,
        Wifi=Wifi,
        Car_Parking=Car_Parking,
        Bike_Cycle_Parking=Bike_Cycle_Parking,
        Security=Security,
        Guard=Guard,
        Fire_Extinguihev=Fire_Extinguihev,
        Hygienic=Hygienic,
        Washroom=Washroom,
        Hostel=Hostel,
        Swimming_Pool_Splash_Pool=Swimming_Pool_Splash_Pool,
        Others=Others,
        Facilities_Amenities_wsabi=Facilities_Amenities_wsabi,
        campusimages=campusimages,
        campusVideo=campusVideo,
        campus360=campus360,
        Saftey=Saftey,
        conteen=conteen,
        Parking=Parking,
        facilitiesandinfra=facilitiesandinfra,
        youtubeurl1=youtubeurl1,
        youtubeurl2=youtubeurl2,
        youtubeurl3=youtubeurl3,
        youtubeurl4=youtubeurl4,
        txtEditor14=txtEditor14,
        txtEditor15=txtEditor15,
        txtEditor16=txtEditor16,

    )
    Facilityvarn.save()
    return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/#admission-eligi')


######################END#########aminities facility######################

def Admission_document_eligibility(request):
    School_Admission_Details_and_Procedure = request.POST["School_Admission_Details_and_Procedure"]
    # academic_year = request.POST["academic_year"]
    Admission_Eligibility_Criteria = request.POST["Admission_Eligibility_Criteria"]
    Documents_Required_for_Admission = request.POST["Documents_Required_for_Admission"]
    Age_Creteria = request.POST["Age_Creteria"]
    Lyco_Arts = request.POST["Lyco_Arts"]
    Lyco_Science = request.POST["Lyco_Science"]
    Lyco_Commerce = request.POST["Lyco_Commerce"]
    Mcoe_Arts = request.POST["Mcoe_Arts"]
    Mcoe_Science = request.POST["Mcoe_Science"]
    Mcoe_Commerce = request.POST["Mcoe_Commerce"]
    Admission_document_eligibilityvarn = Admission_document_eligibility_info(
        School_Admission_Details_and_Procedure=School_Admission_Details_and_Procedure,
        # academic_year=academic_year,
        Admission_Eligibility_Criteria=Admission_Eligibility_Criteria,
        Documents_Required_for_Admission=Documents_Required_for_Admission,
        # Age_Creteria=Age_Creteria,
        Lyco_Arts=Lyco_Arts,
        Lyco_Science=Lyco_Science,
        Lyco_Commerce=Lyco_Commerce,
        Mcoe_Arts=Mcoe_Arts,
        Mcoe_Science=Mcoe_Science,
        Mcoe_Commerce=Mcoe_Commerce
    )
    Admission_document_eligibilityvarn.save()
    # return render(request, "dashboard.html")
    return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/#admission-eligi')


#############################################Basic_information######################
def Basic_information(request):
    users = Basic_informationinfo.objects.all();
        #############################PAGINATION############################
    # page = request.GET.get('page', 1)

    # paginator = Paginator(users,2)
    # try:
    #     dests = paginator.page(page)
    # except PageNotAnInteger:
    #     dests = paginator.page(1)
    # except EmptyPage:
    #     dests = paginator.page(paginator.num_pages)
    ################################################################
    p = users[len(users) - 1].Basic_information_school_logo

    if request.method == "POST" and 'Basic_information_school_logo' in request.FILES:
     if request.method == "POST" and 'Basic_information_school_upload_brochure' in request.FILES:
      if request.method == "POST" and 'Basic_information_school_cover_img' in request.FILES:
         Basic_information_school_logo = Basic_informationinfo.objects.all()
         Basic_information_school_name = request.POST["Basic_information_school_name"]
         Basic_information_school_short_name = request.POST["Basic_information_school_short_name"]
         date = request.POST["date"]
         Basic_information_tag_line_of_school = request.POST["Basic_information_tag_line_of_school"]
         Basic_information_url = request.POST["Basic_information_url"]
         #Basic_information_school_logo = request.POST["Basic_information_school_logo"]
         Basic_information_school_logo = request.FILES['Basic_information_school_logo'];
         Basic_information_school_trusty_socity = request.POST["Basic_information_school_trusty_socity"]
         #Basic_information_school_cover_img = request.POST["Basic_information_school_cover_img"]
         Basic_information_school_cover_img = request.FILES['Basic_information_school_cover_img'];
         #Basic_information_school_upload_brochure = request.POST["Basic_information_school_upload_brochure"]
         Basic_information_school_upload_brochure = request.FILES['Basic_information_school_upload_brochure'];
         Basic_informationvar = Basic_informationinfo(
             Basic_information_school_name=Basic_information_school_name,
             Basic_information_school_short_name=Basic_information_school_short_name,
             date=date,
             Basic_information_tag_line_of_school=Basic_information_tag_line_of_school,
             Basic_information_url=Basic_information_url,
             Basic_information_school_logo=Basic_information_school_logo,
             Basic_information_school_trusty_socity=Basic_information_school_trusty_socity,
             Basic_information_school_cover_img=Basic_information_school_cover_img,
             Basic_information_school_upload_brochure=Basic_information_school_upload_brochure,
        )
         Basic_informationvar.save()
         messages.success(request, 'Updated successfully!')
        #  from django.http import HttpResponseRedirect
         return HttpResponseRedirect('http://mithlesh.pythonanywhere.com/School_dashboard/#basic_information')
         #return render(request, 'School_dashboard.html', {'dests': dests })


##########################################END----Basic_information######################
# ############################################Awards_Recognition###############
def Awards_Recognition(request):
    awards_National_Ranking = request.POST["awards_National_Ranking"]
    awards_Ranking_Body = request.POST["awards_Ranking_Body"]
    awards_uploadimages = request.POST["awards_uploadimages"]
    awards_State_Ranking = request.POST["awards_State_Ranking"]
    awards_Ranking_Body1 = request.POST["awards_Ranking_Body1"]
    awards_uploadimages1 = request.POST["awards_uploadimages1"]
    write_sometings_about_ranking = request.POST["write_sometings_about_ranking"]
    write_somethings_about_sport_awards = request.POST["write_somethings_about_sport_awards"]
    upload_images_and_others_Awards = request.POST["upload_images_and_others_Awards"]
    Awards_Recognitionvar = Awards_Recognitioninfo(
        awards_National_Ranking=awards_National_Ranking,
        awards_Ranking_Body=awards_Ranking_Body,
        awards_uploadimages=awards_uploadimages,
        awards_State_Ranking=awards_State_Ranking,
        awards_Ranking_Body1=awards_Ranking_Body1,
        awards_uploadimages1=awards_uploadimages1,
        write_sometings_about_ranking=write_sometings_about_ranking,
        write_somethings_about_sport_awards=write_somethings_about_sport_awards,
        upload_images_and_others_Awards=upload_images_and_others_Awards,
    )
    Awards_Recognitionvar.save()
    messages.success(request, 'Updated successfully!')
    # return render(request, "http://127.0.0.1:8000/dashboard/#Awards-Recognition")
    return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/#Awards-Recognition')


# fee structure section----------------------------------------------------#
def fee_Scructure(request):
    admission_fee_classwise = request.POST["admission_fee_classwise"]
    admission_fee_security = request.POST["admission_fee_security"]
    admission_fee_other = request.POST["admission_fee_other"]
    application_register_admission_fee_classwise = request.POST["application_register_admission_fee_classwise"]
    application_register_Transpotation_admission_fee_other = request.POST[
        "application_register_Transpotation_admission_fee_other"]
    application_register_fee_for_day_school = request.POST["application_register_fee_for_day_school"]
    india_Admission_Application_fee = request.POST["india_Admission_Application_fee"]
    india_Security_deposite_fees = request.POST["india_Security_deposite_fees"]
    india_Extra_fees = request.POST["india_Security_deposite_fees"]
    india_Yearly_fees = request.POST["india_Yearly_fees"]
    Admission_Application_fee_international = request.POST["Admission_Application_fee_international"]
    Security_deposite_fees_international = request.POST["Security_deposite_fees_international"]
    Extra_fees_international = request.POST["Extra_fees_international"]
    Yearly_fees_international = request.POST["Yearly_fees_international"]
    Estimated_annualfees_class_Wise_international = request.POST["Yearly_fees_international"]
    fee_Scructurevar = fee_structureinfo(
        admission_fee_classwise=admission_fee_classwise,
        admission_fee_security=admission_fee_security,
        admission_fee_other=admission_fee_other,
        application_register_admission_fee_classwise=application_register_admission_fee_classwise,
        application_register_Transpotation_admission_fee_other=application_register_Transpotation_admission_fee_other,
        application_register_fee_for_day_school=application_register_fee_for_day_school,
        india_Admission_Application_fee=india_Admission_Application_fee,
        india_Security_deposite_fees=india_Security_deposite_fees,
        india_Extra_fees=india_Extra_fees,
        india_Yearly_fees=india_Yearly_fees,
        Admission_Application_fee_international=Admission_Application_fee_international,
        Security_deposite_fees_international=Security_deposite_fees_international,
        Extra_fees_international=Extra_fees_international,
        Yearly_fees_international=Yearly_fees_international,
        Estimated_annualfees_class_Wise_international=Estimated_annualfees_class_Wise_international
    )

    fee_Scructurevar.save()
    messages.success(request, 'Updated successfully!')
    return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/#fee_structure_for_day_school')


# end fee structure section------------------------------------------------#

def Hostel_Accomodation(request):
    hostel_Boys = request.POST["hostel_Boys"]
    hostel_Girls = request.POST["hostel_Girls"]
    hostel_boys_Boys_Girls = request.POST["hostel_boys_Boys_Girls"]
    hostel_total_no = request.POST["hostel_total_no"]
    hostel_total_no_boys_yes = request.POST["hostel_total_no_boys_yes"]
    hostel_total_no_boys_no = request.POST["hostel_total_no_boys_no"]
    hostel_total_no_boys_no_ac = request.POST["hostel_total_no_boys_no_ac"]
    hostel_total_no_boys_no_non_ac = request.POST["hostel_total_no_boys_no_non_ac"]
    Hostel_in_campus = request.POST["Hostel_in_campus"]
    Hostel_out_campus = request.POST["Hostel_out_campus"]
    booking_facility_avalilable_from = request.POST["booking_facility_avalilable_from"]
    booking_facility_avalilable_to = request.POST["booking_facility_avalilable_to"]
    Hostel_Accomodationvar = Hostel_Accomodationinfo(
        hostel_Boys=hostel_Boys,
        hostel_Girls=hostel_Girls,
        hostel_boys_Boys_Girls=hostel_boys_Boys_Girls,
        hostel_total_no=hostel_total_no,
        hostel_total_no_boys_yes=hostel_total_no_boys_yes,
        hostel_total_no_boys_no=hostel_total_no_boys_no,
        hostel_total_no_boys_no_ac=hostel_total_no_boys_no_ac,
        hostel_total_no_boys_no_non_ac=hostel_total_no_boys_no_non_ac,
        Hostel_in_campus=Hostel_in_campus,
        Hostel_out_campus=Hostel_out_campus,
        booking_facility_avalilable_from=booking_facility_avalilable_from,
        booking_facility_avalilable_to=booking_facility_avalilable_to

    )
    Hostel_Accomodationvar.save()

    messages.success(request, 'Updated successfully!')
    return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/#Hostel-Accomodation')


# #################################dashboard.html###########SPORTS AND EXTRA-CURRICULAR ACTIVITES###############

def Sports_curricular(request):
    outdoors_sports_cricket = request.POST["outdoors_sports_cricket"]
    outdoors_sports_Football = request.POST["outdoors_sports_Football"]
    outdoors_sportsHockey = request.POST["outdoors_sportsHockey"]
    outdoors_sports_Others = request.POST["outdoors_sports_Others"]
    indoor_sports = request.POST["indoor_sports"]
    indoor_Carrom = request.POST["indoor_Carrom"]
    indoor_Tennis = request.POST["indoor_Tennis"]
    indoor_Boxing = request.POST["indoor_Boxing"]
    indoor_Others = request.POST["indoor_Others"]
    Kids_play_Area = request.POST["Kids_play_Area"]
    Toy_Room = request.POST["Toy_Room"]
    Cricket_Ground = request.POST["Cricket_Ground"]
    Swimming_pool_flash = request.POST["Swimming_pool_flash"]
    sports_facilities_Others = request.POST["sports_facilities_Others"]
    indore_outdoor_pic = request.POST["indore_outdoor_pic"]
    pic_facilities = request.POST["pic_facilities"]
    sports_and_extra_cirrvar = Sports_curricularinfo(
        outdoors_sports_cricket=outdoors_sports_cricket,
        outdoors_sports_Football=outdoors_sports_Football,
        outdoors_sportsHockey=outdoors_sportsHockey,
        outdoors_sports_Others=outdoors_sports_Others,
        indoor_sports=indoor_sports,
        indoor_Carrom=indoor_Carrom,
        indoor_Tennis=indoor_Tennis,
        indoor_Boxing=indoor_Boxing,
        indoor_Others=indoor_Others,
        Kids_play_Area=Kids_play_Area,
        Toy_Room=Toy_Room,
        Cricket_Ground=Cricket_Ground,
        Swimming_pool_flash=Swimming_pool_flash,
        sports_facilities_Others=sports_facilities_Others,
        indore_outdoor_pic=indore_outdoor_pic,
        pic_facilities=pic_facilities
    )
    sports_and_extra_cirrvar.save()
    messages.success(request, 'Updated successfully!')
    return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/#Sports-exta')
    # return render(request, "dashboard.html")


def create_myClass(request):
    # create a dictionary
    context = {
        "data": [1, 2, 3],
    }

    messages.success(request, 'Updated successfully!')
    # return response
    return render(request, "dashboard.html", context)

# def create_myClass(request):
#     context = {
#           }
#     # completed = request.POST.get('completed')
#     completed = request.POST.get('completed', '') == 'on'
#     completed1 = request.POST.get('completed1', '') == 'on'
#     completed2= request.POST.get('completed2', '') == 'on'
#     toSave = myClass(completed=completed, completed1=completed1, completed2=completed2)
#     toSave.save()
#     return render(request, "dashboard.html")




####################################menu-page###############################################
def popular_states_school(request):
        return render(request, 'popular_states_school.html');
def profile(request):
     #data = Customer.objects.get(user__id=request.user.id)
    return render(request, 'profile.html');


from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

def edit_profile(request):
    context = {}
    data = Customer.objects.get(user__id=request.user.id)

    context["data"]=data
    if request.method=="POST":

       fn = request.POST["first_name"]

       ln = request.POST["last_name"]
       un = request.POST["username"]
       ph = request.POST["phone_number"]
       lo = request.POST["location"]
       em = request.POST["email"]
       usr = User.objects.get(id=request.user.id)
       usr.first_name = fn
       usr.last_name = ln
       usr.username = un
       usr.email = em
       usr.save()

       data.phone_number = ph
       data.location = lo

       data.save()
       context["status"] = "changes Save sucessfully"
    return render(request, 'edit_profile.html',context);

# def admin_contact(request):
#       return render(request, 'admin_contact.html');
@login_required
def admin_contact(request):
   if request.method=="POST":
      email1 = 'mithkr.mith24@gmail.com'
      email = request.POST["email"]
      adminname = request.POST["adminname"]
      con = request.POST["con"]
      city = request.POST["city"]
      des = request.POST["des"]

      subject = 'Enquire'
    #   subject1 = 'Thank you for contact us we will get you soon'

      message = f'You get new mail From: {adminname},{email},{con},{city},{des} .'
    #   message2 = f'You get new mail From: {email} .'

      email_from = settings.EMAIL_HOST_USER
      recipient_list = [email1,]
      send_mail( subject, message, email_from, recipient_list )
   return render(request, 'admin_contact.html');


def schoolsp(request):
    dests = Basic_informationinfo.objects.all()

    return render(request, 'schoolsp.html',{'dests': dests});

def schools_details(request, pk):
    pagepage = get_object_or_404(Basic_informationinfo, pk=pk)


    return render(request, 'schools_details.html',{'pagepagep':pagepage});

def collagep(request):
    dests = Col_Basic_informationinfo.objects.all()

    return render(request, 'collagep.html',{'dests': dests});
    # colettt = Col_Basic_informationinfo.objects.all()
    # return render(request, 'collagep.html',{'coleeq':coleeq});

def add_college(request):
        return render(request, 'add_college.html');
##############################ENDmenu-page##################################################
def main_register_form(request):
   return render(request,"main_register_form.html")

####################################menu-page###############################################
def contactaddress(request):
    optradioaddr = request.POST["optradioaddr"]
    addrcountry = request.POST["addrcountry"]
    addrstate = request.POST["addrstate"]
    addrDistrict = request.POST["addrDistrict"]
    addrmain_toen_area = request.POST["addrmain_toen_area"]
    addrsub_area = request.POST["addrsub_area"]
    addrlanmark = request.POST["addrlanmark"]
    addr_addres = request.POST["addr_addres"]
    addr_pincode = request.POST["addr_pincode"]
    addr_location = request.POST["addr_location"]
    addr_name_fap = request.POST["addr_name_fap"]
    addr_name_fap_distance = request.POST["addr_name_fap_distance"]
    addr_name_fap_time = request.POST["addr_name_fap_time"]
    addr_name_fap_latidue = request.POST["addr_name_fap_latidue"]
    addr_name_fap_longatitide = request.POST["addr_name_fap_longatitide"]
    addr_name_rail_name1 = request.POST["addr_name_rail_name1"]
    addr_name_rail_distance = request.POST["addr_name_rail_distance"]
    addr_name_rail_time = request.POST["addr_name_rail_time"]
    addr_name_rail_name2 = request.POST["addr_name_rail_name2"]
    addr_name_rail_distance2 = request.POST["addr_name_rail_distance2"]
    addr_name_rail_time2 = request.POST["addr_name_rail_time2"]
    addr_name_bus_name = request.POST["addr_name_bus_name"]
    addr_name_bus_distancr = request.POST["addr_name_bus_distancr"]
    addr_name_bus_time = request.POST["addr_name_bus_time"]
    addr_nus_nof = request.POST["addr_nus_nof"]
    addr_nus_to_railway = request.POST["addr_nus_to_railway"]
    addr_nus_to_school = request.POST["addr_nus_to_school"]
    addr_contact_name = request.POST["addr_contact_name"]
    addr_contact_mobno = request.POST["addr_contact_mobno"]
    addr_contact_email = request.POST["addr_contact_email"]
    addr_contact_designation = request.POST["addr_contact_designation"]
    addr_contact_principal_name = request.POST["addr_contact_principal_name"]
    addr_contact_principal_mobno = request.POST["addr_contact_principal_mobno"]
    addr_contact_principal_email = request.POST["addr_contact_principal_email"]
    addr_contact_principal_mobhs = request.POST["addr_contact_principal_mobhs"]
    addr_chairman_dir_name = request.POST["addr_chairman_dir_name"]
    addr_chairman_dir_mobno = request.POST["addr_chairman_dir_mobno"]
    addr_chairman_dir_email = request.POST["addr_chairman_dir_email"]
    addr_chairman_dir_hideshow = request.POST["addr_chairman_dir_hideshow"]
    addr_official_name = request.POST["addr_official_name"]
    addr_official_email = request.POST["addr_official_email"]
    addr_official_fax = request.POST["addr_official_fax"]
    schooldescription = request.POST["schooldescription"]
    schooldescription_title = request.POST["schooldescription_title"]
    schooldescription_title_topic = request.POST["schooldescription_title_topic"]


    contactaddressnvar = contactaddressinfo(
        optradioaddr=optradioaddr,
        addrcountry=addrcountry,
        addrstate=addrstate,
        addrDistrict=addrDistrict,
        addrmain_toen_area=addrmain_toen_area,
        addrsub_area=addrsub_area,
        addrlanmark=addrlanmark,
        addr_addres=addr_addres,
        addr_pincode=addr_pincode,
        addr_location=addr_location,
        addr_name_fap=addr_name_fap,
        addr_name_fap_distance=addr_name_fap_distance,
        addr_name_fap_time=addr_name_fap_time,
        addr_name_fap_latidue=addr_name_fap_latidue,
        addr_name_fap_longatitide=addr_name_fap_longatitide,
        addr_name_rail_name1=addr_name_rail_name1,
        addr_name_rail_distance=addr_name_rail_distance,
        addr_name_rail_time=addr_name_rail_time,
        addr_name_rail_name2=addr_name_rail_name2,
        addr_name_rail_distance2=addr_name_rail_distance2,
        addr_name_rail_time2=addr_name_rail_time2,
        addr_name_bus_name=addr_name_bus_name,
        addr_name_bus_distancr=addr_name_bus_distancr,
        addr_name_bus_time=addr_name_bus_time,
        addr_nus_nof=addr_nus_nof,
        addr_nus_to_railway=addr_nus_to_railway,
        addr_nus_to_school=addr_nus_to_school,
        addr_contact_name=addr_contact_name,
        addr_contact_mobno=addr_contact_mobno,
        addr_contact_email=addr_contact_email,
        addr_contact_designation=addr_contact_designation,
        addr_contact_principal_name=addr_contact_principal_name,
        addr_contact_principal_mobno=addr_contact_principal_mobno,
        addr_contact_principal_email=addr_contact_principal_email,
        addr_contact_principal_mobhs=addr_contact_principal_mobhs,
        addr_chairman_dir_name=addr_chairman_dir_name,
        addr_chairman_dir_mobno=addr_chairman_dir_mobno,
        addr_chairman_dir_email=addr_chairman_dir_email,
        addr_chairman_dir_hideshow=addr_chairman_dir_hideshow,
        addr_official_name=addr_official_name,
        addr_official_email=addr_official_email,
        addr_official_fax=addr_official_fax,
        schooldescription=schooldescription,
        schooldescription_title=schooldescription_title,
        schooldescription_title_topic=schooldescription_title_topic,
        # detailse = models.ForeignKey(to=Basic_informationinfo, on_delete=CASCADE, blank=True, null=True, default=''),



    )
    contactaddressnvar.save()
    return render(request, 'School_dashboard.html');

@login_required
def change_pass(request):
    if request.method == 'POST':
       form = PasswordChangeForm(request.user, request.POST)
       if form.is_valid():
            v = form.save()
            update_session_auth_hash(request,v)
            return HttpResponse("Pawssword Change !")

    else:
        form = PasswordChangeForm(request.user)

    params = {
        'form':form,
        }

    return render(request, 'change_pass.html', params)




def College_Basic_information(request):

    # p = users1[len(users1) - 1].Basic_information_colleges_logo
    if request.method == "POST" and 'Basic_information_colleges_logo' in request.FILES:
     if request.method == "POST" and 'Basic_information_colleges_upload_brochure' in request.FILES:
      if request.method == "POST" and 'Basic_information_colleges_cover_img' in request.FILES:


         Basic_information_colleges_name = request.POST["Basic_information_colleges_name"]
         Basic_information_colleges_short_name = request.POST["Basic_information_colleges_short_name"]
         date = request.POST["date"]
         Basic_information_tag_line_of_colleges = request.POST["Basic_information_tag_line_of_colleges"]
         Basic_information_colleges_url = request.POST["Basic_information_colleges_url"]
         #Basic_information_colleges_logo = request.POST["Basic_information_colleges_logo"]
         Basic_information_colleges_logo = request.FILES['Basic_information_colleges_logo'];
         Basic_information_colleges_trusty_socity = request.POST["Basic_information_colleges_trusty_socity"]
         #Basic_information_colleges_cover_img = request.POST["Basic_information_colleges_cover_img"]
         Basic_information_colleges_cover_img = request.FILES['Basic_information_colleges_cover_img'];
         #Basic_information_colleges_upload_brochure = request.POST["Basic_information_colleges_upload_brochure"]
         #Basic_information_colleges_upload_brochure = request.POST["Basic_information_colleges_upload_brochure"]
         Basic_information_colleges_upload_brochure = request.FILES['Basic_information_colleges_upload_brochure'];
         Col_Basic_informationvar = Col_Basic_informationinfo(
                 Basic_information_colleges_name=Basic_information_colleges_name,
                 Basic_information_colleges_short_name=Basic_information_colleges_short_name,
                 date=date,
                 Basic_information_tag_line_of_colleges=Basic_information_tag_line_of_colleges,
                 Basic_information_colleges_url=Basic_information_colleges_url,
                 Basic_information_colleges_logo=Basic_information_colleges_logo,
                 Basic_information_colleges_trusty_socity=Basic_information_colleges_trusty_socity,
                 Basic_information_colleges_cover_img=Basic_information_colleges_cover_img,
                 Basic_information_colleges_upload_brochure=Basic_information_colleges_upload_brochure,
         )
    Col_Basic_informationvar.save()
    messages.success(request, 'Updated successfully!')
    return HttpResponseRedirect('http://mithlesh.pythonanywhere.com/Collage_dashboard/#basic-infolink')












