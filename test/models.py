from django.db import models
from django.urls import reverse

# Create your models here.

class Test(models.Model):
    title = models.CharField('Название Теста', max_length=255)
    pub_date = models.DateField('Дата публикации')
    description = models.TextField()
    question = models.ManyToManyField('test.Question', verbose_name='Вопросы')
    image = models.ImageField('Фото',upload_to='question/image/')
    
    def get_absolute_url(self):
        return reverse('show',kwargs={'id':self.pk})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_description = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_choice')
    choice_text = models.CharField(max_length=200)
    pr = models.BooleanField('Правильно',default=False)
    
    def __str__(self):
        return self.choice_text
    
    
class Person(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(verbose_name='Электронный аддрес')
    test = models.ForeignKey('test.Test', on_delete=models.CASCADE)
    point = models.IntegerField(default=0)
    result = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Учасник'
        verbose_name_plural = 'Учасники'
    