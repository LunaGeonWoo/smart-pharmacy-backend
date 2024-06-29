from django.contrib import admin
from .models import Diagnose, Query


@admin.register(Diagnose)
class DiagnoseAdmin(admin.ModelAdmin):
    pass


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    pass
