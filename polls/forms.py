from .models import Questions, Choices
from django import forms

class CreatePollsForm(forms.ModelForm):
    SELECT_CATEGORY = (
        ('Public', 'Public'),
        ('Private', 'Private'),
    )

    quiz = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Type your question/poll here ...', 'class': 'mb-2'}),
        label='Poll/Question',
    )
    category = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_CATEGORY,
        help_text='Indicate whether this is a public or private poll.'
    )
    close_voting = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'type': 'checkbox'}),
        help_text='Select this if you wish to close this poll.'
    )

    class Meta:
        model = Questions
        fields = '__all__'

class EditPollsForm(forms.ModelForm):
    SELECT_CATEGORY = (
        ('Public', 'Public'),
        ('Private', 'Private'),
    )

    quiz = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Type your question/poll here ...', 'class': 'mb-2'}),
        label='Poll/Question',
    )
    category = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_CATEGORY,
        help_text='Indicate whether this is a public or private poll.'
    )
    close_voting = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'type': 'checkbox'}),
        help_text='Select this if you wish to close this poll.'
    )

    class Meta:
        model = Questions
        fields = '__all__'

class CreateMultipleChoicesForm(forms.ModelForm):
    choice = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Create choice for your poll ...', 'class': 'mb-2'}),
        label='Poll/Question',
    )

    class Meta:
        model = Choices
        fields = '__all__'

class VotingForm(forms.ModelForm):
    choice = forms.BooleanField(
        widget=forms.RadioSelect(attrs={'type': 'radio', 'class': 'mb-2'}),
    )

    class Meta:
        model = Choices
        fields = ['choice']