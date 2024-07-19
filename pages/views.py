from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView

from info.models import PostModel
from offers.models import CarModel, ServicesImageModel
from pages.forms import ContactModelForm
from pages.models import ContactInfoModel, ContactImageModel, HomeImageModel


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['bg_image'] = HomeImageModel.objects.last()
        context['cars'] = CarModel.objects.order_by('-pk')[:10]
        context['services'] = ServicesImageModel.objects.all()
        context['posts'] = PostModel.objects.order_by('-pk')[:3]

        return context


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm
    success_url = '/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['bg_image'] = ContactImageModel.objects.all()
        context['info'] = ContactInfoModel.objects.all()

        return context

    def form_valid(self, form):
        obj = form.save()
        text = (f'You have received a letter from user!\n'
                f'Name: {obj.first_name} {obj.last_name}\n'
                f'Email: {obj.email}\nMessage: {obj.message}')
        send_mail(
            'Notification',
            text,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
        )
        return redirect(self.success_url)
