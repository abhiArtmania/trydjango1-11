from django.conf.urls import url

from .views import (
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView
)

urlpatterns = [
    url(r'^create/$',ItemCreateView.as_view(), name='create'), # 'as_view' is only if 'School_createView' will be of class type
    url(r'^(?P<pk>\d+)/$',ItemDetailView.as_view(), name='detail'),
    url(r'^$',ItemListView.as_view(), name='list')
]
