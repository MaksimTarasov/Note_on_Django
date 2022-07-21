from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _
from .models import Notes

class MainForm(ModelForm):
  class Meta:
    model = Notes
    # Будут выводиться втом порядке в котором указанны
    fields = ['autor_of_note', 'title_of_note', 'note_text']
    widgets = {'note_text':Textarea(attrs={'cols': 80, 'rows': 20})}
    labels = {'autor_of_note': _('Авторрр'), 
              'title_of_note':'Тема заметка', 
              'note_text':'Заметка'}
    # help_texts = {'autor_of_note':'Выбери автора)', 
    #               'title_of_note':'Тут нужно указать тему заметки', 
    #               'note_text':'Тут напиши заметку'}
    error_messages = {
            'note_text': {
                'max_length': "This writer's name is too long.",
              }
            }
    # verbose_names = {
    #    'autor_of_note':'Выбери автора)', 
    #    'title_of_note':'Тут нужно указать тему заметки', 
    #    'note_text':'Тут напиши заметку'
    #  }