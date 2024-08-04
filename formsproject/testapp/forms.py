from django import forms
class StudentForm(forms.Form):
    def clean_name(self):
        print('Validating name field')
        inputname = self.cleaned_data['name']
        if len(inputname) < 4:
            raise forms.ValidationError('The minimum number of characters in the name field should be 4')
        return inputname



    name = forms.CharField()
    marks = forms.IntegerField()
    rollno = forms.IntegerField()
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Password(Again)', widget=forms.PasswordInput)

