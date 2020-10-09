# Generated by Django 3.1.1 on 2020-09-16 08:41

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_customer', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('is_consultancy', models.BooleanField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Admission_document_eligibility_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School_Admission_Details_and_Procedure', models.CharField(max_length=200)),
                ('academic_year', models.CharField(max_length=200)),
                ('Admission_Eligibility_Criteria', models.CharField(max_length=200)),
                ('Documents_Required_for_Admission', models.CharField(max_length=200)),
                ('Lyco_Arts', models.CharField(max_length=200)),
                ('Lyco_Science', models.CharField(max_length=200)),
                ('Lyco_Commerce', models.CharField(max_length=200)),
                ('Mcoe_Arts', models.CharField(max_length=200)),
                ('Mcoe_Science', models.CharField(max_length=200)),
                ('Mcoe_Commerce', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='admission_infonn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(max_length=200)),
                ('academic_start', models.CharField(max_length=200)),
                ('academic_end', models.CharField(max_length=200)),
                ('online_admission_application', models.CharField(max_length=200)),
                ('Admission_page_url', models.CharField(max_length=200)),
                ('Facility_to_pay_admission_online', models.CharField(max_length=200)),
                ('Admission_open', models.CharField(max_length=200)),
                ('academic_contactpersonname', models.CharField(max_length=200)),
                ('academic_contactpersonmob', models.CharField(max_length=200)),
                ('academic_contactpersonemail', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Awards_Recognitioninfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awards_National_Ranking', models.CharField(max_length=200)),
                ('awards_Ranking_Body', models.CharField(max_length=200)),
                ('awards_uploadimages', models.CharField(max_length=200)),
                ('awards_State_Ranking', models.CharField(max_length=200)),
                ('awards_Ranking_Body1', models.CharField(max_length=200)),
                ('awards_uploadimages1', models.CharField(max_length=200)),
                ('write_sometings_about_ranking', models.CharField(max_length=200)),
                ('write_somethings_about_sport_awards', models.CharField(max_length=200)),
                ('upload_images_and_others_Awards', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Basic_informationinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Basic_information_school_name', models.CharField(max_length=200)),
                ('Basic_information_school_short_name', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('Basic_information_tag_line_of_school', models.CharField(max_length=200)),
                ('Basic_information_url', models.CharField(max_length=200)),
                ('Basic_information_school_logo', models.CharField(max_length=200)),
                ('Basic_information_school_trusty_socity', models.CharField(max_length=200)),
                ('Basic_information_school_cover_img', models.CharField(max_length=200)),
                ('Basic_information_school_upload_brochure', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Facility_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_center', models.CharField(max_length=124)),
                ('Computer_Labs', models.CharField(max_length=124)),
                ('Library', models.CharField(max_length=124)),
                ('Laboratories', models.CharField(max_length=124)),
                ('Canteen_Cafteria', models.CharField(max_length=124)),
                ('Transport_facilities', models.CharField(max_length=124)),
                ('Sports_facilities', models.CharField(max_length=124)),
                ('Medical_Facility', models.CharField(max_length=124)),
                ('Lockers', models.CharField(max_length=124)),
                ('CCTV', models.CharField(max_length=124)),
                ('Audotorium_Seminar_Hall', models.CharField(max_length=124)),
                ('Gymnasiumn', models.CharField(max_length=124)),
                ('Play_Ground', models.CharField(max_length=124)),
                ('Drinking_Water', models.CharField(max_length=124)),
                ('Music_Dance', models.CharField(max_length=124)),
                ('Stationary_Shop', models.CharField(max_length=124)),
                ('Wifi', models.CharField(max_length=124)),
                ('Car_Parking', models.CharField(max_length=124)),
                ('Bike_Cycle_Parking', models.CharField(max_length=124)),
                ('Security', models.CharField(max_length=124)),
                ('Guard', models.CharField(max_length=124)),
                ('Fire_Extinguihev', models.CharField(max_length=124)),
                ('Hygienic', models.CharField(max_length=124)),
                ('Washroom', models.CharField(max_length=124)),
                ('Hostel', models.CharField(max_length=124)),
                ('Swimming_Pool_Splash_Pool', models.CharField(max_length=124)),
                ('Others', models.CharField(max_length=124)),
                ('Facilities_Amenities_wsabi', models.CharField(max_length=124)),
                ('campusimages', models.CharField(max_length=124)),
                ('campusVideo', models.CharField(max_length=124)),
                ('campus360', models.CharField(max_length=124)),
                ('Saftey', models.CharField(max_length=124)),
                ('conteen', models.CharField(max_length=124)),
                ('Parking', models.CharField(max_length=124)),
                ('facilitiesandinfra', models.CharField(max_length=124)),
                ('youtubeurl1', models.CharField(max_length=124)),
                ('youtubeurl2', models.CharField(max_length=124)),
                ('youtubeurl3', models.CharField(max_length=124)),
                ('youtubeurl4', models.CharField(max_length=124)),
                ('txtEditor14', models.CharField(max_length=124)),
                ('txtEditor15', models.CharField(max_length=124)),
                ('txtEditor16', models.CharField(max_length=124)),
            ],
        ),
        migrations.CreateModel(
            name='fee_structureinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_fee_classwise', models.CharField(max_length=200)),
                ('admission_fee_security', models.CharField(max_length=200)),
                ('admission_fee_other', models.CharField(max_length=200)),
                ('application_register_admission_fee_classwise', models.CharField(max_length=200)),
                ('application_register_fee_for_day_school', models.CharField(max_length=200)),
                ('application_register_Transpotation_admission_fee_other', models.CharField(max_length=200)),
                ('india_Admission_Application_fee', models.CharField(max_length=200)),
                ('india_Security_deposite_fees', models.CharField(max_length=200)),
                ('india_Extra_fees', models.CharField(max_length=200)),
                ('india_Yearly_fees', models.CharField(max_length=200)),
                ('Yearly_fees_international', models.CharField(max_length=200)),
                ('Admission_Application_fee_international', models.CharField(max_length=200)),
                ('Security_deposite_fees_international', models.CharField(max_length=200)),
                ('Extra_fees_international', models.CharField(max_length=200)),
                ('Estimated_annualfees_class_Wise_international', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel_Accomodationinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel_Boys', models.CharField(blank=True, max_length=200, null=True)),
                ('hostel_Girls', models.CharField(blank=True, max_length=200, null=True)),
                ('hostel_boys_Boys_Girls', models.CharField(blank=True, max_length=200, null=True)),
                ('hostel_total_no', models.CharField(blank=True, max_length=200, null=True)),
                ('hostel_total_no_boys_yes', models.CharField(blank=True, max_length=200, null=True)),
                ('hostel_total_no_boys_no', models.CharField(blank=True, max_length=200, null=True)),
                ('hostel_total_no_boys_no_ac', models.CharField(blank=True, max_length=200, null=True)),
                ('hostel_total_no_boys_no_non_ac', models.CharField(blank=True, max_length=200, null=True)),
                ('Hostel_in_campus', models.CharField(blank=True, max_length=200, null=True)),
                ('Hostel_out_campus', models.CharField(blank=True, max_length=200, null=True)),
                ('booking_facility_avalilable_from', models.CharField(blank=True, max_length=200, null=True)),
                ('booking_facility_avalilable_to', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='myClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(blank=True, default=False)),
                ('completed1', models.BooleanField(blank=True, default=False)),
                ('completed2', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='reg_sign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School_Name', models.CharField(max_length=100)),
                ('Cant_find_your_School', models.CharField(max_length=100)),
                ('Contact_person_Name', models.CharField(max_length=100)),
                ('Designation_at_School', models.CharField(max_length=100)),
                ('Password1', models.CharField(max_length=100)),
                ('Password2', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Mobile_No', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=124)),
            ],
        ),
        migrations.CreateModel(
            name='Sports_curricularinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outdoors_sports_cricket', models.CharField(blank=True, max_length=200, null=True)),
                ('outdoors_sports_Football', models.CharField(blank=True, max_length=200, null=True)),
                ('outdoors_sportsHockey', models.CharField(blank=True, max_length=200, null=True)),
                ('outdoors_sports_Others', models.CharField(blank=True, max_length=200, null=True)),
                ('indoor_sports', models.CharField(blank=True, max_length=200, null=True)),
                ('indoor_Carrom', models.CharField(blank=True, max_length=200, null=True)),
                ('indoor_Tennis', models.CharField(blank=True, max_length=200, null=True)),
                ('indoor_Boxing', models.CharField(blank=True, max_length=200, null=True)),
                ('indoor_Others', models.CharField(blank=True, max_length=200, null=True)),
                ('Kids_play_Area', models.CharField(blank=True, max_length=200, null=True)),
                ('Toy_Room', models.CharField(blank=True, max_length=200, null=True)),
                ('Cricket_Ground', models.CharField(blank=True, max_length=200, null=True)),
                ('Swimming_pool_flash', models.CharField(blank=True, max_length=200, null=True)),
                ('sports_facilities_Others', models.CharField(blank=True, max_length=200, null=True)),
                ('indore_outdoor_pic', models.CharField(blank=True, max_length=200, null=True)),
                ('pic_facilities', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consultancy',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fime1223.user')),
                ('phone_number', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fime1223.user')),
                ('phone_number', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fime1223.user')),
                ('phone_number', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
            ],
        ),
    ]
