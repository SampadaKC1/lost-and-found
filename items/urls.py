from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("report/", views.report_item, name="report_item"),
    path("item/<int:item_id>/", views.item_detail, name="item_detail"),
    path("my-items/", views.my_items, name="my_items"),

    path("item/<int:item_id>/edit/", views.edit_item, name="edit_item"),
    path("item/<int:item_id>/delete/", views.delete_item, name="delete_item"),
]