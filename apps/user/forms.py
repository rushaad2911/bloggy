# users/forms.py
from allauth.account.forms import LoginForm, SignupForm
from django import forms
from .models import Interest,BlogUser


# class CustomLoginForm(LoginForm):
#     username = forms.CharField(label="Email or Username")

class CustomSignupForm(SignupForm):
    interests = forms.ModelMultipleChoiceField(queryset=Interest.objects.all(), required=True)

    def save(self, request):
        user = super().save(request)
        user.save()
        return user
