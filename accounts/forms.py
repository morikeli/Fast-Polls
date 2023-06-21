from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User


SELECT_GENDER = (
    (None, '-- Select your gender --'),
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        self.error_messages['invalid_login'] = 'INVALID CREDENTIALS!!! \
        Enter correct name (first name and last name -> separate first name and last name with a space!) and password. \
        Name and password maybe case-senstitive.'



class SignupForm(UserCreationForm):
    """ This form is used by users to create an account. """
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'autocomplete': True}),
        required=True,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'autocomplete': True}),
        required=True,
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'autocomplete': True}),
        required=True,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'type': 'email', 'class': 'mb-2'}),
        required=True,
    )
    gender = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_GENDER,
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'gender', 'password1', 'password2']


class EditProfileForm(forms.ModelForm):
    """ This form allow users to edit their profile. """
    phone_no = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'number', 'class': 'mb-2', 'minlength': 10, 'maxlength': 10, 'placeholder': 'Enter your mobile number'}),
        help_text='Enter your number without your country code'
    )
    profile_pic = forms.ImageField(
        widget=forms.FileInput(attrs={'type': 'file', 'accept': '.jpg, .jpeg, .png'}),
    )

    class Meta:
        model = User
        fields = [
            'phone_no', 'profile_pic',
        ]
