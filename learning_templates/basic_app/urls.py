from django.conf.urls import url
from basic_app import views



#TEMPLATE TAGGING
app_name='basic_app'      #tell django to look under basic_app and find the url that matches
                         


urlpatterns=[
    url(r'^basic/$',views.basic,name='basic'),
    url(r'^other/$',views.other,name='other'),
    url(r'^relative/$',views.relative,name='relative'),
]
