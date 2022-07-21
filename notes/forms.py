from django import forms
from .models import Notes

class MainForm(forms.ModelForm):
  class Meta:
    model = Notes
    fields = ['autor_of_note', 'title_of_note', 'note_text']
