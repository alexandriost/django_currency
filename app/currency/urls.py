from django.urls import path
from currency.views import (
    RateListView, RateDetailView, RateCreateView, RateUpdateView, RateDeleteView,
    ContactUsCreateView,
    SourceListView, SourceDetailView, SourceCreateView, SourceUpdateView, SourceDeleteView,
)

app_name = 'currency'

urlpatterns = [
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),

    path('contact-us/create/', ContactUsCreateView.as_view(), name='contact-us-create'),

    path('sources/list/', SourceListView.as_view(), name='sources-list'),
    path('sources/<int:pk>/', SourceDetailView.as_view(), name='sources-details'),
    path('sources/create/', SourceCreateView.as_view(), name='sources-create'),
    path('sources/<int:pk>/update/', SourceUpdateView.as_view(), name='sources-update'),
    path('sources/<int:pk>/delete/', SourceDeleteView.as_view(), name='sources-delete'),
]
