from django.shortcuts import render
from . import models, forms
# Create your views here.
def index(request):
  """
  Вывод списка записей
  """
  notes_list = models.Notes.objects.all()
  content = {'notes':'notes', 'notes_list':notes_list}
  return render(request, 'notes/index.html', content)

def create_note(request):
  """
  СОздание 
  """
  if request.method == 'POST':
    pass
    #mainform = forms.MainForm(request.POST)
    # if mainform.is_valid():
    #   s = {'name':mainform.cleaned_data['name'],'comment':mainform.cleaned_data['comment']}
    # nam = mainform.cleaned_data['name']
    # com = mainform.cleaned_data['comment']
    # comment_db =  models.Comment.objects.create(name = nam, comment = com) 
  else:
    create_form = forms.MainForm()
    content = {'create_form':create_form}
    return render(request, 'notes/create_note.html', content)