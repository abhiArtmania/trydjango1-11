from django.conf.urls import url

from .views import (
    SearchSchoolListView,
    SearchSchoolDetailView,
    School_createView,
    School_updateView
)

urlpatterns = [
    url(r'^create/$',School_createView.as_view(), name='create'), # 'as_view' is only if 'School_createView' will be of class type
    url(r'^(?P<slug>[\w-]+)/$',School_updateView.as_view(), name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$',School_updateView.as_view(), name='edit')
    url(r'^$',SearchSchoolListView.as_view(), name='list')
]
