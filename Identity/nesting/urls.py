from django.conf.urls import url
from nesting.views import Identity_view
from . import views

urlpatterns = [
url(r'^$', Identity_view.as_view(), name = 'nesting')
]
