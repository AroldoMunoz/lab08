from rest_framework import serializers
from .models import Time

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        # fields = ('id', 'title', 'description', 'done')
        fields = '__all__'
       