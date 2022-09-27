
from django.urls import include, path

from rest_framework import routers


from api_v1.views import get_token_view, QuoteView, ChangeRatingPlus, ChangeRatingMinus

# router = routers.DefaultRouter()
# router.register('quotes', QuoteViewSet)

app_name = 'api_v1'

urlpatterns = [

    # path('', include(router.urls)),
    path('quotes/', QuoteView.as_view(),name="QuoteView"),
    path('quotes/<int:pk>/',QuoteView.as_view(),name="QuoteView"),
    path('get_token/', get_token_view, name='get_token_view'),
    path('quotes/<int:pk>/plus/', ChangeRatingPlus.as_view(), name='ChangeRatingPlus'),
    path('quotes/<int:pk>/minus/', ChangeRatingMinus.as_view(), name='ChangeRatingMinus'),

]
