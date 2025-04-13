# from django.shortcuts import render
# from allauth.account.views import SignupView,LoginView
# from django.views.generic import TemplateView
# from django.shortcuts import redirect
# from .forms import *



# class CustomSignupView(SignupView):
#     template_name = 'html/auth/signup.html'  
  
    
    
    
# class CustomLoginView(LoginView):
#     template_name = 'html/auth/login.html'
#     form_class = LoginForm()

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#         # Add any custom context variables here if needed
#         # context['custom_variable'] = 'some value'
#     #     return context
    
# class AddInterest(TemplateView):
#     template_name = 'html/auth/add_interest.html'

#     def get(self, request, *args, **kwargs):
#         form = InterestForm()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = InterestForm(request.POST)
#         if form.is_valid():
#             interests = form.cleaned_data['interests']
#             user = request.user  # Access the logged-in user
#             user.interest.set(interests)  # Update the user's interests
#             user.save()
#             return redirect('/blog/')  # Redirect to a success page or user's profile
#         return render(request, self.template_name, {'form': form})