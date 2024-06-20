from django import forms
from datetime import datetime

class IncidentForm(forms.Form):
    date_created = forms.DateTimeField(
        initial=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control flatpickr',  # Adding the flatpickr class for JS initialization
                'placeholder': 'Select Date and Time'
            }
        )
    )
    severity = forms.ChoiceField(
        choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    details = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False
    )
