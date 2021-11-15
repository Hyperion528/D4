from django.forms import ModelForm, BooleanField
from .models import New
 
 
# Создаём модельную форму
class NewForm(ModelForm):
    check_box = BooleanField(label='Подтвердить')  # добавляем галочку, или же true-false поле

    class Meta:
        model = New
        fields = ['name', 'description', 'category', 'author']