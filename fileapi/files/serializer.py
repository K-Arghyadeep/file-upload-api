from rest_framework import serializers
from .models import UploadedFile
from .validate import validate_file

class UploadedFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True, validators=[validate_file])

    class Meta:
        model = UploadedFile
        filefields = ["id", "file", "original_name", "file_size", "file_type", "uploaded_at"]
        read_only_fields = ["original_name", "file_size", "file_type", "uploaded_at"]


    def create(self, validated_data):
        upload = validated_data("file")
        validated_data["original_name"] = upload.name
        validated_data["file_size"] = upload.file_size
        validated_data["file_type"] = upload.content_type
        return super().create(validated_data)
