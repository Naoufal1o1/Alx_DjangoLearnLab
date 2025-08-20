from django.urls import path
from .views import NotificationListView, mark_all_read

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notifications'),
    path('notifications/mark-read/', mark_all_read, name='notifications-mark-read'),
]
