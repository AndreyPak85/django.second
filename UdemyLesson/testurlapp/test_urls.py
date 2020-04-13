from django.conf.urls import url
from testurlapp import views


urlpatterns = [


    url(r'^user/(\d{2})/(\d{4})/$', views.home, name='home'),

]
