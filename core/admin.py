from django.contrib import admin
from core.models import *
# Register your models here.

admin.site.register([Story,Recipe,Category,Contact,Tag,Comment,Subscriber,])
