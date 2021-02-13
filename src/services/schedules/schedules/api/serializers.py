from rest_framework import serializers
from api.models import Subject

#class SubjectSerializer(serializers.Serializer):
#    name = serializers.CharField(required=True, allow_blank=False, max_length=200)
#
#    def create(self, validate_data):
#        return Subject.objects.create(**validate_data)
#
#    def update(self, instance, validate_data):
#        instance.name = validate_data.get('name', instance.name)
#        instance.save()
#        return instance

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id','name']