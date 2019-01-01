"""mywebsite URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from posts import views
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^posts/', include('posts.urls')),
    # url(r'^posts/$', views.index, name='index'),# この書き方だと、新しいアプリができた時にimport viewsがかぶってしまう。だからよくない。
    url(r'^admin/', admin.site.urls),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^posts/about/$', views.about, name='about'),
    # url(r'', RedirectView.as_view(url='/posts/'), name='redirect_to_index')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
               static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#staticなファイルについては、setting.pyのMEDIA_URLと、MEDIA_ROOTを見てねー
