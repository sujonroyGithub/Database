from django.contrib import admin
from home.models import Contact
from home.models import Help
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','title','salary','email','phone','address','presentaddress','desc','agree','date') 
class HelpAdmin(admin.ModelAdmin):
    list_display=('name','email','message','date') 
# Register your models here.
admin.site.register(Contact,ContactAdmin)
admin.site.register(Help,HelpAdmin)
