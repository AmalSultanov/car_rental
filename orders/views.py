import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView

from offers.models import CarModel, CarsImageModel
from orders.forms import OrderModelForm


class CheckoutCreateView(LoginRequiredMixin, CreateView):
    template_name = 'checkout.html'
    form_class = OrderModelForm

    def get_success_url(self):
        return reverse('orders:checkout',
                       kwargs=self.kwargs) + '#contact-section'

    def form_valid(self, form):
        date_from = self.request.POST.get('date_from')
        date_to = self.request.POST.get('date_to')
        date_from = datetime.datetime.strptime(date_from,
                                               '%d/%m/%Y %H:%M')
        date_to = datetime.datetime.strptime(date_to,
                                             '%d/%m/%Y %H:%M')

        form.instance.date_from = date_from
        form.instance.date_to = date_to
        form.save()

        messages.info(self.request, 'ok')

        return redirect(self.get_success_url())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['bg_image'] = CarsImageModel.objects.all()
        context['car'] = get_object_or_404(CarModel,
                                           pk=self.kwargs.get('pk'))
        return context
