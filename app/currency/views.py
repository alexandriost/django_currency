# from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django_filters.views import FilterView

from currency.filters import RateFilter, ContactUsFilter, SourceFilter
from currency.forms import RateForm, ContactUsForm, SourceForm
from currency.models import Rate, ContactUs, Source


class RateListView(FilterView):
    queryset = Rate.objects.all().select_related('source')
    template_name = 'rates_list.html'
    paginate_by = 10
    filterset_class = RateFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_pagination'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items() if key != 'page'
        )
        return context


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


class ContactUsListView(FilterView):
    template_name = 'contactus_list.html'
    queryset = ContactUs.objects.all()
    paginate_by = 5
    model = ContactUs
    filterset_class = ContactUsFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_pagination'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items() if key != 'page'
        )
        return context


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
        # recipient = settings.DEFAULT_FROM_EMAIL
        message = f'''
        Request from: {self.object.name}.
        Reply to email: {self.object.email}.
        Subject: {self.object.subject},
        Body: {self.object.message}
        '''

        from currency.tasks import send_mail
        # from datetime import datetime, timedelta
        # send_mail.delay(subject, message)
        # send_mail.apply_async(args=[subject, message])
        send_mail.apply_async(
            kwargs={'subject': subject, 'message': message},
            # eta=datetime.now() + timedelta(seconds=20)
            # countdown=20
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_mail()
        return redirect


class ContactUsUpdateView(UpdateView):
    form_class = ContactUsForm
    template_name = 'contactus_update.html'
    success_url = reverse_lazy('currency:contactus-list')
    queryset = ContactUs.objects.all()


class ContactUsDeleteView(DeleteView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_delete.html'
    success_url = reverse_lazy('currency:contactus-list')


class ContactUsDetailView(DetailView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_details.html'


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'sources_list.html'
    paginate_by = 10
    filterset_class = SourceFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_pagination'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items() if key != 'page'
        )
        return context


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
