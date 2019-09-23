from django.contrib import admin
from django.urls import path
from webapp.views import index_view, product_detail_view, product_create_view, product_update_view, product_delete_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_view, name="index"),
    path("products/<int:pk>/", product_detail_view, name="product_detail"),
    path("product/add/", product_create_view, name="product_add"),
    path("product/<int:pk>/edit", product_update_view, name="product_update"),
    path('product/<int:pk>/delete', product_delete_view, name="product_delete")
]