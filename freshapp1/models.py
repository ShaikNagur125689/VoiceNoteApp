from django.db import models
from django.contrib.auth.models import User
from .validators import validate_audio_file 

class VoiceNote(models.Model):
    title = models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    audio=models.FileField(upload_to='voic_notes/',validators=[validate_audio_file])
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title