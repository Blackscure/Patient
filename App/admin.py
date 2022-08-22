from django.contrib import admin
from App.models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'gender', 'create_at']
    search_fields = ['name', 'phon', 'email','gender']
    list_filter = ['gender']
    list_per_page = 10

admin.site.register(Patient, PatientAdmin)
