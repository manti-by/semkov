from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.documents import urls as wagtaildocs_urls

from api.resources import (
    ContactResource,
    AdsResource,
    RegisterResource,
    LoginResource,
    LogoutResource,
)
from search import views as search_views

urlpatterns = [
    url(r"^django/", admin.site.urls),
    url(r"^dashboard/", include(wagtailadmin_urls)),
    url(r"^documents/", include(wagtaildocs_urls)),
    url(r"^search/$", search_views.search, name="search"),
    url(r"^api/contact/?$", ContactResource.as_view(), name="api-contact"),
    url(r"^api/ads/?$", AdsResource.as_view(), name="api-ads"),
    url(r"^api/register/?$", RegisterResource.as_view(), name="api-register"),
    url(r"^api/login/?$", LoginResource.as_view(), name="api-login"),
    url(r"^api/logout/?$", LogoutResource.as_view(), name="api-logout"),
    url(r"^sitemap\.xml$", sitemap),
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r"", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
