from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
  notes_list = models.Notes.objects.all()
  content = {'notes':'notes', 'notes_list':notes_list}
  return render(request, 'notes/index.html', content)

def create_note(request):
  if request.method == 'POST':
    mainform = forms.MainForm(request.POST)
    if mainform.is_valid():
      s = {'name':mainform.cleaned_data['name'],'comment':mainform.cleaned_data['comment']}
    nam = mainform.cleaned_data['name']
    com = mainform.cleaned_data['comment']
    comment_db =  models.Comment.objects.create(name = nam, comment = com) 
  else:
    content = {'create':''}
    return render(request, 'create_notes.html', content)