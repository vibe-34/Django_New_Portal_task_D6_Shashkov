from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Record
from .filters import RecordFilter
from .forms import RecordForm


class NewsList(ListView):                   # Класс, который наследуется от ListView
    model = Record                          # Указываем модель, объекты которой мы будем выводить
    ordering = ['-data']                    # Поле, которое будет использоваться для сортировки объектов
    template_name = 'news/news_home.html'   # Указываем имя шаблона. С инструкциями о том, как показать объекты юзеру
    context_object_name = 'record'          # Имя списка содержит все объекты. Его указать, для обр.к объектам в html
    paginate_by = 10                        # указываем количество записей на странице


class SearchList(ListView):
    model = Record
    ordering = ['-data']
    template_name = 'news/search.html'
    context_object_name = 'record'
    paginate_by = 10

    def get_filter(self):
        return RecordFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs  # Возвращает get_filter в который мы применяя qs для получения queryset

    def get_context_data(self, *args, **kwargs):  # для работы в шаблоне, переназначаем метод get_context_data
        return {**super().get_context_data(*args, **kwargs), 'filter': self.get_filter(), }
        # переменная filter будет использоваться в шаблоне


class NewsId(DetailView):
    model = Record
    template_name = 'news/news_id.html'
    context_object_name = 'record'


class NewsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_record',)
    form_class = RecordForm
    model = Record
    template_name = 'news/create.html'
    success_url = '/news/'              # после публикации новой записи, нас перенаправляют на страницу всех публикаций


class NewsUpdataView(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_record',)
    form_class = RecordForm             # Для формы обновления, используем уже созданный класс RecordForm из form.py
    model = Record
    template_name = 'news/create.html'
    success_url = '/news/'


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_record',)
    model = Record
    template_name = 'news/news_delete.html'
    success_url = '/news/'
