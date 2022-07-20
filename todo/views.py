from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView
from . import forms
from . import models
# Create your views here.

class CP(CreateView):
  template_name = 'todo/index2.html'
  form_class = forms.MainForm2
  success_url = '/index_new/'
  
  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    context['choice'] = models.TestModel.objects.all()
    return context
    pass


    

def index(request): 
  if request.method == 'POST':
    mainform = forms.MainForm(request.POST)
    if mainform.is_valid():
      s = {'name':mainform.cleaned_data['name'],'comment':mainform.cleaned_data['comment']}
    nam = mainform.cleaned_data['name']
    com = mainform.cleaned_data['comment']
    comment_db =  models.Comment.objects.create(name = nam, comment = com) 
  else:
      s = {'name':'Vasya','comment':'LOH'}
      
  all_com = models.Comment.objects.in_bulk()
 
  mainform = forms.MainForm(s)
  content = {'my_text':'hello_world', 'main_form':mainform, 'comments':all_com}
  return render(request, 'todo/index.html', content)


def data_out(request):
  if request.method == "POST":
    frm = forms.ChoiceForm(request.POST)
    if frm.is_valid():
      return HttpResponse(frm.cleaned_data)
    return HttpResponse(request.POST)
  else: 
    db = models.Comment.objects.all()
    frm = forms.ChoiceForm()
    content = {'records':db, 'frm':frm}
    return render(request, 'todo/out_data.html', content)