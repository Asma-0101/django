# forms.py
from django import forms
from .models import Journal
from bootstrap_datepicker.widgets import DatePicker

class DateInput(forms.DateInput):
    input_type='date'

class JournalForm(forms.Form):

    day_type_choices = [
    ("Happy Happy", "happy"),
    ("Sad", "sad"),
    ("Meh", "moderate"),
    ("Angry aaghhh", "angry")
]
    title = forms.CharField(max_length=100)
    day_type = forms.ChoiceField(choices= day_type_choices, widget=forms.Select)

    day_date = forms.DateField(widget=DateInput)
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    day_rate = forms.IntegerField(max_value=5, min_value=1)
    privacy_check = forms.BooleanField(required=True)
    # class Meta:
    #     model = Journal
    #     fields = ['title', 'day_type', 'day_date','description', 'day_rate', 'privacy_check'] 

# class SaveJournalForm(forms.ModelForm):
    # class Meta:
    #     model = Journal

