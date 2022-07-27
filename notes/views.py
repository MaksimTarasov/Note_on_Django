from django.shortcuts import render, redirect
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
  СОздание записи в блокноте
  """
  if request.method == 'POST':
    mainform = forms.MainForm(request.POST)
    if mainform.is_valid():
      #s = {'name':mainform.cleaned_data['name'],'comment':mainform.cleaned_data['comment']}
      print(mainform.cleaned_data['autor_of_note'])
      autor = models.Autor.objects.get(name = mainform.cleaned_data['autor_of_note'])
      title = mainform.cleaned_data['title_of_note']
      note = mainform.cleaned_data['note_text']
      
        # autor_of_note = models.ForeignKey(Autor, on_delete=models.CASCADE)
        # title_of_note = models.CharField(max_length=100)
        # date_of_note = models.DateField(auto_now_add = True)
        # note_text = models.CharField(max_length=255)
      comment_db =  models.Notes.objects.create(autor_of_note = autor, 
                                               title_of_note = title,
                                               note_text = note)
      return redirect('/notes')
  else:
    default_note = models.Notes.objects.get(id=1)
    #Создаем форму с дефолтной записью, id=1
    create_form = forms.MainForm(instance = default_note)
    content = {'create_form':create_form}
    return render(request, 'notes/create_note.html', content)