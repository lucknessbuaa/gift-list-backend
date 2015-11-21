from django.conf.urls import include, url
from django.contrib import admin

from portal import views as portal_views
import portal.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/article$', portal_views.getArticle),
    url(r'^api/overview$', portal_views.getOverview),
    url(r'^api/rank$', portal_views.getRank),
    url(r'^api/partners$', portal_views.getPartners),
    url(r'^api/cover$', portal_views.getCover),
    url(r'^api/share$', portal_views.getShare),
]
