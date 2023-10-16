from .models import Questions, Choices
from django import forms

class CreatePollsForm(forms.ModelForm):
    SELECT_CATEGORY = (
        (None, '-- Select category --'),
        ('Art', 'Art'),
        ('Automotive', 'Automotive'),
        ('Business', 'Business'),
        ('Computing', 'Computing'),
        ('Design', 'Design'),
        ('Fashion', 'Fashion'),
        ('Mathematics', 'Mathematics'),
        ('Office', 'Office'),
        ('Politics', 'Politics'),
        ('Science', 'Science'),
        ('Technology', 'Technology'),
        ('Tips', 'Tips'),
        ('Travel', 'Travel'),
    )

    quiz = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Type your question/poll here ...', 'class': 'mb-2',
        }),
        label='Poll/Question',
    )
    category = forms.ChoiceField(widget=forms.Select(attrs={
        'type': 'select', 'class': 'mb-2',
        }),
        choices=SELECT_CATEGORY,
        help_text='Select one option to that is related to the subject of your poll.',
    )
    closing_dt = forms.DateField(widget=forms.DateInput(attrs={
            'type': 'date', 'class': 'mb-0',
        }),
        label='Scheduled closing date',
        help_text='Schedule a closing date for this poll. Once closed, voters will not vote.',
    )
    is_private = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'type': 'checkbox', 'class': 'my-2',
        }),
        required=False,
        help_text='Is this poll private? Leave blank if public.'
    )

    class Meta:
        model = Questions
        fields = ['quiz', 'category', 'closing_dt', 'is_private']

class EditPollsForm(forms.ModelForm):
    SELECT_CATEGORY = (
        (None, '-- Select category --'),
        ('Art', 'Art'),
        ('Automotive', 'Automotive'),
        ('Business', 'Business'),
        ('Computing', 'Computing'),
        ('Design', 'Design'),
        ('Fashion', 'Fashion'),
        ('Mathematics', 'Mathematics'),
        ('Office', 'Office'),
        ('Politics', 'Politics'),
        ('Science', 'Science'),
        ('Technology', 'Technology'),
        ('Tips', 'Tips'),
        ('Travel', 'Travel'),
    )

    quiz = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Type your question/poll here ...', 'class': 'mb-2',
        }),
        label='Poll/Question',
    )
    category = forms.ChoiceField(widget=forms.Select(attrs={
        'type': 'select', 'class': 'mb-2',
        }),
        choices=SELECT_CATEGORY,
        help_text='Select one option to that is related to the subject of your poll.',
    )
    closing_dt = forms.DateField(widget=forms.DateInput(attrs={
            'type': 'date', 'class': 'mb-0',
        }),
        label='Scheduled closing date',
        help_text='Schedule a closing date for this poll. Once closed, voters will not vote.',
    )
    is_private = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'type': 'checkbox', 'class': 'mt-1',
        }),
        required=False,
        help_text='Is this poll private? Leave blank if public.'
    )

    class Meta:
        model = Questions
        fields = ['quiz', 'category', 'closing_dt', 'is_private']


class CreateMultipleChoicesForm(forms.ModelForm):
    choice = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Create choice for your poll ...', 'class': 'mb-2'}),
        label='Add Choice',
    )

    class Meta:
        model = Choices
        fields = '__all__'


class EditMultipleChoicesForm(forms.ModelForm):
    choice = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}),
        label='Poll/Question',
    )

    class Meta:
        model = Choices
        fields = '__all__'

