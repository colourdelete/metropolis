from rest_framework import serializers
from .tag import TagSerializer
from ... import models


class OrganizationSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='username', queryset=models.User.objects.all())
    supervisors = serializers.SlugRelatedField(slug_field='username', many=True, queryset=models.User.objects.all())
    execs = serializers.SlugRelatedField(slug_field='username', many=True, queryset=models.User.objects.all())

    tags = TagSerializer(many=True)

    class Meta:
        model = models.Organization
        fields = '__all__'
