from django.contrib import admin

# Register your models here.
from ROBOWEB.adm.models import Phrase


@admin.register(Phrase)
class TaskPhrase(admin.ModelAdmin):
    list_display = ('phrase',)