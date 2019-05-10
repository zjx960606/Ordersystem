from django.conf.urls import url
from . import views
app_name = 'orderapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^registers/$', views.registers, name='registers'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logins/$', views.logins, name='logins'),
    url(r'^loginout/$',views.loginout, name='loginout'),
    url(r'^popular/$', views.popular, name='popular'),
    url(r'^order/$',views.order, name='order'),
    url(r'^orders/$',views.orders, name='orders'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^contacts/$', views.contacts, name='contacts'),
]