from django.conf.urls import url
from nesting.views import Identity_view, Identity_nest_list_view
from . import views

urlpatterns = [
url(r'^$', Identity_view.as_view(), name = 'nesting'),
url(r'^Identity-nest/$', Identity_nest_list_view.as_view(), name = 'Identity_nest_list')
]
