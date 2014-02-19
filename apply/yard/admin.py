from django.contrib import admin

from yard.models import Skill, Portal, Company, Application, Profile

# Register your models here.
admin.site.register(Skill)
admin.site.register(Portal)
admin.site.register(Company)
admin.site.register(Application)
admin.site.register(Profile)