"""UdemyLesson URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
#from teststaticapp import views
#from firstapp import views
from django.conf.urls.static import static
from django.conf import settings
#from teststaticapp import views
#from validformapp import views
from authapp import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^test_app/', include('testurlapp.test_urls')),
    #url(r'^$', views.home),
    url(r'^$', views.home, name='home'),
    #url(r'^(?P<pizza_id>\d+)/$', views.pizza_detail, name='pizza_detail'),
    #url(r'formpage/', views.form_page, name='form-page'),
    #url(r'authapp/login/$', views.LoginView.as_view(template_name=template_name), name='login'),
    url(r'authapp/login/$', LoginView.as_view(), {'template_name': 'authapp/login.html'}, name='authapp-login'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
