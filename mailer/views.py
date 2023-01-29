from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import *
from .models import *
from django.urls import reverse_lazy


class HomeListView(ListView):
    template_name = 'home.html'
    model = Report

    def get_queryset(self):
        return Report.objects.filter(user_id=self.request.user.id)


class DistributionListView(ListView):
    model = Distribution

    def get_queryset(self):
        return Distribution.objects.filter(user_id=self.request.user.id)


class DistributionCreateView(CreateView):
    form_class = DistributionForm
    template_name = 'mailer/distribution_form.html'
    success_url = reverse_lazy('mailer:manage')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(DistributionCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class DistributionUpdateView(UpdateView):
    form_class = DistributionForm
    model = Distribution
    success_url = reverse_lazy('mailer:manage')
    Distribution.status = 'created'

    def get_form_kwargs(self):
        kwargs = super(DistributionUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class DistributionDeleteView(DeleteView):
    model = Distribution
    success_url = reverse_lazy('mailer:manage')


class DistributionDetailView(DetailView):
    model = Distribution
    success_url = reverse_lazy('mailer:manage')


class MessageListView(ListView):
    model = Message

    def get_queryset(self):
        return Message.objects.filter(user_id=self.request.user.id)


class MessageCreateView(CreateView, ):
    form_class = MessageForm
    template_name = 'mailer/message_form.html'
    success_url = reverse_lazy('mailer:messages')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    form_class = MessageForm
    model = Message
    success_url = reverse_lazy('mailer:messages')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailer:messages')


class MessageDetailView(DetailView):
    model = Message
    success_url = reverse_lazy('mailer:messages')


class RecipientListView(ListView):
    model = Recipient

    def get_queryset(self):
        return Recipient.objects.filter(user_id=self.request.user.id)


class RecipientCreateView(CreateView):
    model = Recipient
    fields = ('address',)
    success_url = reverse_lazy('mailer:recipients')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class RecipientUpdateView(UpdateView):
    fields = ('address',)
    model = Recipient
    success_url = reverse_lazy('mailer:recipients')


class RecipientDeleteView(DeleteView):
    model = Recipient
    success_url = reverse_lazy('mailer:recipients')


class RecipientDetailView(DetailView):
    model = Recipient
    success_url = reverse_lazy('mailer:recipients')
