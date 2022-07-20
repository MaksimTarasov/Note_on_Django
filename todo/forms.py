from django import forms
from .models import Comment

CH = [(1,1),(2,2),(2,2)]

class MainForm(forms.Form):
    name = forms.CharField(initial='Name')
    comment = forms.CharField(initial='Comment')

class MainForm2(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('name', 'comment')



class ChoiceForm(forms.Form):
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CH,)