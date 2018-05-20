from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users_profile import views as profile_views

urlpatterns = [
    url(r'^$', profile_views.home, name='home'),
    url(r'^settings/password/$', profile_views.password, name='password'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
]
