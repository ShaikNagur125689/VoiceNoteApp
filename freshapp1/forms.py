from django import forms
from .models import VoiceNote
from django.contrib.auth.models import User

class VoiceNoteForm(forms.ModelForm):
    class Meta:
        model = VoiceNote
        fields = ['title', 'audio']  # Ensure these fields exist in VoiceNote model

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # ✅ Hash the password correctly
        if commit:
            user.save()
        return user
