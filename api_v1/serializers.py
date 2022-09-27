from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.migrations import serializer
from rest_framework import serializers

from api_v1.models import Quote


class QuoteSerializers(serializers.ModelSerializer):
    class Meta:
        model=Quote
        fields=['text','name','email','rate','status']
        read_only_fields = ['rate']

# class QuoteRaitinsSerializers(serializers.ModelSerializer):
#     rate=serializers.IntegerField(write_only=True,validators=[MinValueValidator(-1), MaxValueValidator(1)])
#     class Meta:
#         model=Quote
#         fields=['rate']






