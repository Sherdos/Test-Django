from django.contrib import admin
from test.models import *
from django.utils.safestring import mark_safe
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['question_text']}),('Дополнительно', {'fields':['question_description']})]
    inlines=[ChoiceInline]
    list_display = ('question_text',)
    search_fields = ['question_text']
    
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ['point','test','percent']
    list_display = ('name','result_html','percent')
    fields = ('name','email','test','point','percent',)
    list_filter = ['result',]
    
    def result_html(self,object):
        return mark_safe(f"<progress max='100' value='{object.result}'></progress><p>{object.result}%</p>")
    
    def percent(self, object):
        return mark_safe(f"<p>{object.result}%</p>")
        

admin.site.register(Question, QuestionAdmin)
admin.site.register(Test)
admin.site.register(Person,PersonAdmin)