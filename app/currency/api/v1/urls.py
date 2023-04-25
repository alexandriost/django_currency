from django.urls import path
from rest_framework.routers import DefaultRouter

from currency.api.v1.views import RateViewSet, SourceViewSet, ContactUsViewSet

# from currency.api.views import RateApiView, RateDetailApiView


app_name = 'api-currency'

router = DefaultRouter()
router.register(r'rates', RateViewSet, basename='rates')
router.register(r'sources', SourceViewSet, basename='sources')
router.register(r'contacts-us', ContactUsViewSet, basename='contacts-us')

urlpatterns = [
    # path('rates/', RateApiView.as_view(), name='rates'),
    # path('rates/<int:pk>/', RateDetailApiView.as_view(), name='rates-detail')

]

urlpatterns += router.urls