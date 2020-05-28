from django.urls import path
from partyou.registration.views import SignUpCreateView, ProfileUpdate, EmailUpdate

urlpatterns = [
    path('signup/', SignUpCreateView.as_view(), name="signup"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
]
