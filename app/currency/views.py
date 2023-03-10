from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm


class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rates_list.html'


class RateDetailView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rates_details.html'


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rates_create.html'
    success_url = reverse_lazy('currency:rate-list')


class RateUpdateView(UpdateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    template_name = 'rates_update.html'
    success_url = reverse_lazy('currency:rate-list')


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rates_delete.html'
    success_url = reverse_lazy('currency:rate-list')


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
        recipient = 'support@example.com'
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


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('index')
    # model = get_user_model()  # User
    queryset = get_user_model().objects.all()
    fields = (
        'first_name',
        'last_name'
    )

    def get_object(self, queryset=None):
        return self.request.user

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(id=self.request.user.id)
    #     return queryset