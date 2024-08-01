import asyncio

from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, TemplateView, DetailView, FormView

from projectclubs.settings import admin_chat_id
from .models import *
from .forms import *
from .tbot_utils import send_message_to_user
from django.http import Http404

from .utils import *


# Вывод всех клубов.
class ListClubsView(ListView):
    model = ClubModel
    template_name = 'collab/all_clubs.html'
    context_object_name = 'all_clubs'
    extra_context = {
        'title': 'Клубы',
        'menu_slug': 'all_clubs'
    }


# Детальное отображение клуба, подробная информация о нем.
class DetailClubView(DetailView):
    template_name = 'collab/detail_club.html'
    model = ClubModel
    context_object_name = 'club'

    # Даем в контекст под ключом club объект модели ClubModel под текущим слагом.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получение клуба по слагу
        context['club'] = get_club_by_slug(self.kwargs['slug'])
        return context


# Создание клуба.
class CreateClubView(CreateView):
    model = ClubModel
    template_name = 'collab/create_club.html'
    form_class = ClubModelForm
    success_url = reverse_lazy('collab:all_clubs')
    extra_context = {
        'title': 'Создать клуб',
        'menu_slug': 'create_club'
    }

    # Устанавливаем значение текущего пользователя для поля author.
    # Устанавливаем значение для слага на основе имени.
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.name)
        return super().form_valid(form)


# Профиль пользователя
class ProfileUser(TemplateView):
    template_name = 'collab/profile_user.html'

    extra_context = {
        'title': 'Личный кабинет',
        'menu_slug': 'profile_user'
    }

    # В контекс передает временный код для подтверждения Telegram аккаунта (код создается при регистрации пользователя).
    # В контекс передаем список клубов пользователя(где он является автором).
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['telegram_verif_code'] = self.request.user.telegram_verif_code

        # получение клуба на основе того, является ли текущий пользователь автором.
        context['my_clubs'] = ClubModel.objects.filter(author=self.request.user)

        return context


# Добавление пользователя в клуб при нажатии на кнопку.
def join_club_view(request, slug):
    # Получение клуба на основе слага
    club = get_club_by_slug(slug)
    club.request_team.add(request.user)

    # Отправляем уведомление о подаче заявки на участие в клубе.
    chat_id = get_author_by_slug(slug).telegram_chat_id
    message = f'Подана заявка на участие пользователем {request.user.username} в клуб {club.name}'
    try:
        send_message_to_user(chat_id, message)
    except:
        raise Http404()

    return redirect('collab:all_clubs')


# Отправка сообщения любому пользователю по pk.
# Дополнительно передается slug клуба, из которого происходит отправка.
class SendMsgView(FormView):
    template_name = 'collab/send_msg.html'
    form_class = SendMsgForm

    def form_valid(self, form):
        message = form.cleaned_data['message']
        message = f"""
        Вам пришло новое сообщение от пользователя {self.request.user} из клуба 
        {get_club_by_slug(self.kwargs['slug'])}.\nСообщение:\n{message}"""

        chat_id = get_user_model().objects.get(pk=self.kwargs['pk']).telegram_chat_id
        try:
            send_message_to_user(chat_id, message)
        except:
            raise Http404()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('collab:detail_club', kwargs={'slug': self.kwargs['slug']})


# Вывод всех заявок на участие в клубе. Только для админов.
class ListRequestTeamView(TemplateView):
    template_name = 'collab/list_confirm_team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Передаем в контекст пользователей, которые подали заявку; клуб, в который подали заявку
        context['request_team'] = get_club_by_slug(self.kwargs['slug']).request_team.all()
        context['club'] = get_club_by_slug(self.kwargs['slug'])
        return context
