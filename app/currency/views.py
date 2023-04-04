from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from currency.forms import RateForm, SourceForm
from currency.models import Rate, ContactUs, Source


class RateListView(ListView):
    queryset = Rate.objects.all().select_related('source')
    template_name = 'rates_list.html'


class RateDetailView(LoginRequiredMixin, DetailView):
    queryset = Rate.objects.all()
    template_name = 'rates_details.html'


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rates_create.html'
    success_url = reverse_lazy('currency:rate-list')


class RateUpdateView(UserPassesTestMixin, UpdateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    template_name = 'rates_update.html'
    success_url = reverse_lazy('currency:rate-list')

    def test_func(self):
        return self.request.user.is_superuser


class RateDeleteView(UserPassesTestMixin, DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rates_delete.html'
    success_url = reverse_lazy('currency:rate-list')

    def test_func(self):
        return self.request.user.is_superuser


class ContactUsCreateView(CreateView):
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('index')
    model = ContactUs
    fields = (
        'name',
        'email',
        'subject',
        'message'
    )

    def _send_mail(self):
        subject = 'User ContactUs'
        recipient = settings.DEFAULT_FROM_EMAIL
        message = f'''
        Request from: {self.object.name}.
        Reply to email: {self.object.email}.
        Subject: {self.object.subject},
        Body: {self.object.message}
        '''

        from django.core.mail import send_mail
        send_mail(
            subject,
            message,
            recipient,
            [recipient],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_mail()
        return redirect


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'sources_list.html'


class SourceDetailView(DetailView):
    queryset = Source.objects.all()
    template_name = 'sources_details.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    template_name = 'sources_create.html'
    success_url = reverse_lazy('currency:sources-list')


class SourceUpdateView(UpdateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    template_name = 'sources_update.html'
    success_url = reverse_lazy('currency:sources-list')


class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    template_name = 'sources_delete.html'
    success_url = reverse_lazy('currency:sources-list')


class IndexView(TemplateView):
    template_name = 'index.html'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(id=self.request.user.id)
    #     return queryset
