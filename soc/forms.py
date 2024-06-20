from django import forms
from datetime import datetime

class IncidentForm(forms.Form):
    date_created = forms.DateTimeField(
        initial=datetime.now,
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control flatpickr',  # Adding the flatpickr class for JS initialization
                'placeholder': 'Select Date and Time'
            }
        )
    )
    severity = forms.ChoiceField(
        choices=[
            ('High', 'High'),
            ('Medium', 'Medium'),
            ('Low', 'Low')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    details = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False
    )

class AlertForm(forms.Form):
    date_created = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control flatpickr',
                'placeholder': 'Select Date and Time'
            }
        ),
        initial=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        required=False
    )
    priority = forms.ChoiceField(
        choices=[
            ('High', 'High'),
            ('Medium', 'Medium'),
            ('Low', 'Low')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False
    )
    emails = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email(s)'}),
        required=False
    )
