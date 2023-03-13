from django.contrib import admin
import ks_students.models

# Register your models here.
admin.site.register(ks_students.models.Student)
admin.site.register(ks_students.models.Profile)
admin.site.register(ks_students.models.Interaction)
admin.site.register(ks_students.models.Status)
admin.site.register(ks_students.models.InteractionType)