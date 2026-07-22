from pathlib import Path
import filetype
# import pylibmagic
# import magic
from django.core import serializers

ALLOWED_TYPES = {"image/jpeg", "image/png", "application/pdf"}
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".pdf"}

def validate_file(self, value):
    # detected = magic.from_buffer(value.read(2048), mime=True)
    # value.seek(0)
    # if detected not in ALLOWED_TYPES:
    #     raise serializers.ValidationError(f"Type {value.content_type} not allowed.")
    if value.size > 10 * 1024 * 1024:
        raise serializers.ValidationError("File exceeds 10MB limit.")
    ext = Path(value.name).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise serializers.ValidationError(f"Extension {ext} not allowed.")
    if value.content_type not in ALLOWED_TYPES:
        raise serializers.ValidationError(f"Type {value.content_type} not allowed.")
    return value