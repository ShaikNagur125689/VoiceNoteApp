import os
from django.core.exceptions import ValidationError

def validate_audio_file(file):
    ext=os.path.splitext(file.name)[1].lower()
    valid_extensions=['.mp3', '.wav', '.m4a', '.ogg']
    if ext not in valid_extensions:
        raise ValidationError(f"Unsupported file type: {ext} Only audio files are alllowed. Please upload an audio file.")