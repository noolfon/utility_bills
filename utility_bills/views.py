from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from utility_bills.forms import PaymentsForm
from utility_bills.models import Payments
from django.contrib.auth.models import User
from utility_bills.utils import sum_pays

__all__ = (
    'PaymentsDetailView', 'PaymentsCreateView', 'PaymentsUpdateView',
    'PaymentsDeleteView', 'PaymentsListView',
)


class PaymentsListView(ListView):
    paginate_by = 12
    model = Payments
    template_name = 'utility_bills/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Payments.objects.filter(current_user_id=self.request.user.id)
        context['sum_pay'] = sum_pays(qs)
        return context

    def get_queryset(self):
        return Payments.objects.filter(current_user_id=self.request.user.id)


class PaymentsDetailView(DetailView):
    # детальное отображение
    queryset = Payments.objects.all()
    template_name = 'utility_bills/detail.html'


class PaymentsCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    # модель скоторой работает форма(куда добавит записи)
    model = Payments
    # передадать форму из класса форм на страничку
    form_class = PaymentsForm
    # шаблон отображения
    template_name = 'utility_bills/create.html'
    # адресс редиректа
    success_url = reverse_lazy('utility_bills:home')
    # передача сообщений о успешном создании
    success_message = "Запись успешно добавлена!"

    def form_valid(self, form):
        # Мы используем ModelForm, а его метод save() возвращает инстанс
        # модели, связанный с формой. Аргумент commit=False говорит о том, что
        # записывать модель в базу рановато.
        instance = form.save(commit=False)
        # Теперь, когда у нас есть не сохранённая модель, можно ей чего-нибудь
        # накрутить. Например, заполнить внешний ключ на auth.User.
        instance.current_user = User.objects.get(id=self.request.user.id)
        # А теперь можно сохранить в базу
        instance.save()
        return super().form_valid(form)





class PaymentsUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Payments
    form_class = PaymentsForm
    template_name = 'utility_bills/update.html'
    success_url = reverse_lazy('utility_bills:home')
    success_message = "Запись успешно изменена!"


    def current_url(self):
        current_url = self.request.get_full_path()
        return current_url


class PaymentsDeleteView(LoginRequiredMixin, DeleteView):
    model = Payments
    form_class = PaymentsForm
    template_name = 'utility_bills/delete.html'
    success_url = reverse_lazy('utility_bills:home')

    # после переопределения этого метода не показывает страничку с подтверждением
    def get(self, request, *args, **kwargs):
        messages.success(request, 'Запись успешно удалена!')
        return self.post(request, *args, **kwargs)
