from django import forms
from django.core import validators
class FeedBackForm(forms.Form):








    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])

    def clean_name(self):
        print('Total form validation......')

        print('Validating Name')
        inputname = self.cleaned_data['name']
