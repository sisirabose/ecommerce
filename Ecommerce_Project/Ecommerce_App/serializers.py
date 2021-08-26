from rest_framework import serializers
from .models import customer_table,prodtable
class sign_serializer(serializers.ModelSerializer):
    class Meta:
        model=customer_table
        fields='__all__'


class prod_serializer(serializers.ModelSerializer):
    class Meta:
        model=prodtable
        fields='__all__'        