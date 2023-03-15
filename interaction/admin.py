from django.contrib import admin
import interaction.models

# Register your models here.
admin.site.register(interaction.models.Interaction)
admin.site.register(interaction.models.Status)
admin.site.register(interaction.models.InteractionType)