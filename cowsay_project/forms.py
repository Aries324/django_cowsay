from django import forms
# from cowsay_project.models import UserInputText


class UserInputForm(forms.Form):
    text = forms.CharField(max_length=100, label='Enter your text here: ', initial='')
