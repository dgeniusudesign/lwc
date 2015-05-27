from django.contrib import admin

# Register your models here.
from .models import Join

class JoinAdmin(admin.ModelAdmin):
  list_display = ['__unicode__','ref_id','friend','timestamp','updated','ip_address',]
  class Meta:
    model = Join

admin.site.register(Join, JoinAdmin)