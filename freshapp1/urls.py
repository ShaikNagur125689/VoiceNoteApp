from django.urls import path
from .views import home, upload_voice_note, register, custom_logout, user_login,delete_voicenote


urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_voice_note, name='upload_voice_note'),
    path('register/', register, name='register'),
    path('logout/', custom_logout, name='logout'),  # ✅ Custom logout
    path("login/", user_login, name="login"),
    path('voicenote/delete/<int:pk>/', delete_voicenote, name='delete_voicenote'),
]
