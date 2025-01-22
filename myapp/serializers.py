from rest_framework import serializers
from .models import GeneratedFile


class GeneratedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedFile
        fields = ['id', 'original_image', 'glb_file1', 'glb_file2', 'glb_file3', 'created_at']
