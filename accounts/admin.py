from django.contrib import admin

from accounts.models import Account
from app.models import CV, Contacts, Experience, Education

# Register your models here.
admin.site.register(Account)
admin.site.register(CV)
admin.site.register(Contacts)
admin.site.register(Experience)
admin.site.register(Education)
