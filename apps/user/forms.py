# users/forms.py
from allauth.account.forms import LoginForm, SignupForm
from django import forms
from .models import Interest,BlogUser



class CustomSignupForm(SignupForm):
    interest = forms.ModelMultipleChoiceField(queryset=Interest.objects.all(), 
                                               widget=forms.CheckboxSelectMultiple,
                                               required=True)

    def save(self, request):
        user = super().save(request)
        user.interest.set(self.cleaned_data['interest'])
        user.save()
        return user






