from django.db import models

# Create your models here.
class Autor(models.Model):
  """
    Класс описывает автора 
    name - Имя автора
    nic_name - nic автора
    avatar - аватарка автора
  """
  class Meta:
    ordering = ['-name']

  name = models.CharField(verbose_name='Имя Фамилия', max_length=200)
  nic_name = models.CharField(verbose_name='Ник', max_length=200)
  avatar = models.CharField(verbose_name='Аватарка', max_length=200)

  def __str__(self):
    return f'{self.name}'

class Notes(models.Model):
  """
    Класс описывает запись в блокноте
  """
  class Meta:
    ordering =['-date_of_note']
  autor_of_note = models.ForeignKey(Autor, on_delete=models.CASCADE)
  title_of_note = models.CharField(max_length=100)
  date_of_note = models.DateField(auto_now_add = True)
  note_text = models.CharField(max_length=255)

  def __str__(self):
    return f'{self.title_of_note}'

  
  
  