from django.contrib import admin
from .models import Member, GeneralDegreeInfo, MbaInfo

# Register your models here.
admin.site.register(Member)
admin.site.register(GeneralDegreeInfo)
admin.site.register(MbaInfo)
