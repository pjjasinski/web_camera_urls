from django.urls import path
from weburls import views

urlpatterns = [
    path('cameras/', views.camera_list),
    path('cameras/<int:pk>/', views.camera_detail),
    path('snapshots/', views.snapshot_list),
    path('snapshots/<int:pk>/', views.snapshot_detail),
]
