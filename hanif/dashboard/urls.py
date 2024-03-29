from django.contrib import admin
from django.urls import path
from .views import dashboard, table_list, delete_table, add_table, dashboard_table

urlpatterns = [
    # Pola URL untuk halaman dashboard tanpa pk
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/table/<int:pk>/', dashboard_table, name='table'),
    path('dashboard/tablelist/<int:pk>/', table_list, name='tablelist'),
    path('dashboard/delete_table/<int:pk>/', delete_table, name='delete_tablelist'),
    path('dashboard/add_table', add_table, name='add_tablelist'),
]
