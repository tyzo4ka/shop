from django.contrib import admin
from django.urls import path
from webapp.views import index_view
    # entry_create_view, entry_delete_view, entry_update_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_view, name="index"),
    # path("entry/add/", entry_create_view, name="entry_add"),
    # path("entry/<int:pk>/edit", entry_update_view, name="entry_update"),
    # path('entry/<int:pk>/delete', entry_delete_view, name="entry_delete")
]