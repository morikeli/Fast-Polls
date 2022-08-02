from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Question, Choice
from django import forms


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        
        self.fields['username'].label = 'Enter your name'
        self.error_messages['invalid_login'] = 'Invalid Credentials. Username & password may be case-sensitive'

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your first name...'}), required=True, label='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your surname ...'}), required=True, label='')
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email address ...'}), required=True, label='')
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

class SetQuestionsForm(forms.ModelForm):
    question_text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a question ...'}), label='')
    
    class Meta:
        model = Question
        fields = ['question_text']

class SetMultipleChoices(forms.ModelForm):
    option = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter choice ... '}), label='', required=True)
    
    class Meta:
        model = Choice
        fields = ['question', 'option']
