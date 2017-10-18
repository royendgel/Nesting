from django.conf.urls import url
from nesting.views import Identity_view, Identity_nest_list_view, Symptoms_document_view, Medical_History_nest_view
from . import views

urlpatterns = [
                    url(r'^$', Identity_view.as_view(), name = 'nesting'),
                    url(r'^Identity-nest/$', Identity_nest_list_view.as_view(), name = 'Identity_nest_list'),
                    url(r'^Symptoms-document/(?P<pk>\d+)', Symptoms_document_view.as_view(), name = 'Symptoms_nest_list'),
                    url(r'^Symptom-view/(?P<pk>\d+)', Medical_History_nest_view.as_view(), name = 'Medical_History_nest')
]
