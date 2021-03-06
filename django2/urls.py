"""django2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from restraunt.views import list_of_restraunts, restlistview, restdetailview, restformcreateview,restform
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^login/$', LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
    url(r'^restraunts_list/(?P<rest_id>\w+)$', restdetailview.as_view()),
    url(r'^restraunt/create/$', restformcreateview.as_view()),

    # url(r'^restraunts_list/(?P<pk>\w+)$', restdetailview.as_view()),
    # url(r'^restraunts_list/(?P<slug>\w+)$', restlistview.as_view()),


    url(r'^restraunts_list/$', restlistview.as_view())
]
