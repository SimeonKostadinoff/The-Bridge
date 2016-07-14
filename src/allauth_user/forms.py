from allauth.account.forms import SignupForm, LoginForm
from django import forms

class SignupFormOverride(SignupForm):
    first_name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    #email = forms.EmailField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    def __init__(self, *args, **kwargs):
        super(SignupFormOverride, self).__init__(*args, **kwargs)
        self.fields['email'].label = ''
        self.fields['email'].widget = forms.TextInput(attrs={'type': 'email', 'placeholder': 'Email'})
        self.fields['password1'].label = ''
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password2'].label = ''
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Re-enter password'})

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        #user.email = self.cleaned_data['email']
        user.save()

class LoginFormOverride(LoginForm):
    def __init__(self, *args, **kwargs):
        super(LoginFormOverride, self).__init__(*args, **kwargs)
        self.fields['login'].label = ''
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'email', 'placeholder': 'Email'})
        self.fields['password'].label = ''
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['remember'].label = 'Remember me'