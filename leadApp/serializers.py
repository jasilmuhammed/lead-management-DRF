from rest_framework import serializers
from leadApp.models import Lead

class LeadSerializers(serializers.ModelSerializer):
    class Meta:
        model=Lead
        fields="__all__"
        read_only_fields=["id","added_date"]