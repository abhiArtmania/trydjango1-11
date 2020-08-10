from django.conf.urls import url

from .views import (
    SearchSchoolListView,
    SearchSchoolDetailView,
    School_createView
)

urlpatterns = [
    url(r'^$',SearchSchoolListView.as_view(), name='list'),
    url(r'^create/$',School_createView.as_view(), name='create'), # 'as_view' is only if 'School_createView' will be of class type
    url(r'^(?P<slug>[\w-]+)/$',SearchSchoolDetailView.as_view(), name='detail')
]
