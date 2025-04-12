from django.shortcuts import render
from allauth.account.views import SignupView


# using cstom singup template
class CustomSignupView(SignupView):
    template_name = 'html/auth/signup.html'  