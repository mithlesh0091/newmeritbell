from django.contrib import admin

# Register your models here.


# Register your models here.
from fime1223.models import School
admin.site.register(School)


from .models import admission_infonn
admin.site.register(admission_infonn)

from .models import Admission_document_eligibility_info
admin.site.register(Admission_document_eligibility_info)

from .models import Awards_Recognitioninfo
admin.site.register(Awards_Recognitioninfo)

from .models import fee_structureinfo
admin.site.register(fee_structureinfo)

from .models import Sports_curricularinfo
admin.site.register(Sports_curricularinfo)
from .models import Basic_informationinfo
admin.site.register(Basic_informationinfo)


from .models import contactaddressinfo
admin.site.register(contactaddressinfo)

# from django.contrib import admin
# from .models import User, Customer, Employee

# admin.site.register(User)
# admin.site.register(Customer)
# admin.site.register(Employee)
