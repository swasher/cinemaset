"""
cinemaset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('customuser.urls')),
    url(r'^', include('movie.urls')),

    #TODO deprecated

    # url(r'^accounts/logout/$', auth.views.logout),

    # from django-registartion-redux
    url(r'^accounts/', include('registration.backends.default.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)