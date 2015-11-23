from django.conf.urls import include, url
from django.contrib import admin

from portal import views as portal_views
import portal.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/config$', portal_views.getConfig),
    url(r'^api/data$', portal_views.getData),
]
