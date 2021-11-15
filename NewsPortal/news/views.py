# from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView  #
from .models import New, Category
from datetime import datetime

from django.views import View
from django.core.paginator import Paginator

from django.shortcuts import render
from .filters import F #Фильтр
from .forms import NewForm #формы
 
class News(ListView):
    model = New #модель, объекты которой мы будем выводить
    template_name = 'news.html'  # имя шаблона, в котором будет лежать HTML
    context_object_name = 'news'  
    queryset = New.objects.order_by('-id')
    ordering = ['-date_pub']
    paginate_by = 1 # поставим постраничный вывод в один элемент
    # form_class = NewForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словаря и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['filter'] = F(self.request.GET, queryset=self.get_queryset())
        return context


class NewDetailView(DetailView):
    # model = New # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'new_detail.html'  # название шаблона будет product.html
    # context_object_name = 'new'  # название объекта. в нём будет
    queryset = New.objects.all()


class NewCreateView(CreateView):
    template_name = 'new_add.html'
    form_class = NewForm

def news_list(request):
    f = F(request.GET, queryset=New.objects.all())
    return render(request, 'fil.html', {'filter': f})


class NewUpdateView(UpdateView):
    template_name = 'new_edit.html'
    form_class = NewForm
 
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return New.objects.get(pk=id)
 
 
class NewDeleteView(DeleteView):
    template_name = 'new_delete.html'
    queryset = New.objects.all()
    success_url = '/news/'