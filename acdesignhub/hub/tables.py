import django_tables2 as tables

from .models import Design

class DesignTable(tables.Table):
    class Meta:
        model = Design
