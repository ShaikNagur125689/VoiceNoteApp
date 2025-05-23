from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import VoiceNote
from .forms import VoiceNoteForm, UserRegistrationForm
from django.contrib import messages

from .models import VoiceNote
from django.conf import settings

from django.utils import timezone
from django.db.models import Q
from django.http import HttpResponseForbidden



def home(request):
    # Show all voice notes that actually have an audio file
    notes = VoiceNote.objects.all().order_by('-created_at') 
    return render(request, "freshapp1/home.html", {"notes": notes})




def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # ✅ No need to manually hash password
            login(request, user)  # ✅ Auto-login after registration
            return redirect('home')  
    else:
        form = UserRegistrationForm()
    
    return render(request, 'freshapp1/register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()  # Prevent KeyError
        password = request.POST.get("password", "").strip()
        
        

        if not username or not password:
            messages.error(request, "Both username and password are required.")
            return render(request, "freshapp1/login.html")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to home page after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "freshapp1/login.html")

@login_required
def upload_voice_note(request):
    if request.method == "POST":
        form = VoiceNoteForm(request.POST, request.FILES)
        if form.is_valid():
            voice_note = form.save(commit=False)
            voice_note.user = request.user  # ✅ Assign the logged-in user
            voice_note.save()
            return redirect('home')
    else:
        form = VoiceNoteForm()
    
    return render(request, 'freshapp1/upload.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('home')

@login_required
def delete_voicenote(request, pk):
    voicenote = get_object_or_404(VoiceNote, pk=pk)

    # Ensure only the owner can delete
    if voicenote.user != request.user:
            return HttpResponseForbidden("You are not allowed to delete this voice note.")  # or show an error

    # Delete the audio file from storage
    voicenote.audio.delete()  # deletes the actual file
    voicenote.delete()        # deletes the DB record

    return redirect('home')  # or wherever you list voicenotes


