from django.contrib import admin
from user.models import User, Military_User, Counselor_User

# Register your models here.
admin.site.register(User)
admin.site.register(Military_User)
admin.site.register(Counselor_User)