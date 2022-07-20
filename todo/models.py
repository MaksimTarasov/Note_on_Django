from django.db import models

# Create your models here.
class Comment(models.Model):
  name = models.CharField(max_length=20)
  comment = models.CharField(max_length=200)
  def __str__(self):
    return f'{self.name} - {self.comment}'
  
  def create_answer(self)->str:
    answer = (self.comment).split('.')[0]
    return answer
    
  def return_title(self):
    return self.create_answer()
    
  def get_url(self):
    return self.id
    

    
    
    


class TestModel(models.Model):
  KIND = (('a','aaa'),('b','bbb'))
  K_COM = (('a','abvgd'), ('e', 'eprst'))
  name2 = models.CharField(max_length=1, choices=KIND)
  comment2 = models.CharField(max_length=1, choices=K_COM)
  def __str__(self):
    return f'{self.name2} : {self.comment2}'