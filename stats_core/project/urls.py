from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

import stats_core.accounts.urls
import stats_core.blocks.urls
import stats_core.comments.urls
import stats_core.config.urls
import stats_core.recipes.urls
from stats_core.authentication.views.login import LoginView

API_PREFIX = 'api/'

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view(), name='login'),
    path(API_PREFIX, include(stats_core.accounts.urls)),
    path(API_PREFIX, include(stats_core.blocks.urls)),
    path(API_PREFIX, include(stats_core.config.urls)),
    path(API_PREFIX, include(stats_core.comments.urls)),
    path(API_PREFIX, include(stats_core.recipes.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
