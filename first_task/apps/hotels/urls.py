from django.urls import path, include
from . import view

app_name = 'hotels'

urlpatterns = [
    path('', view.hotels, name='hotels'),
    path('<int:hotel_id>/', include([
        path('', view.hotel, name='hotel'),
        path('<int:id>/', view.room, name='room'),  # это id, не room_id
    ]))
]
