from django.urls import path

from . import views

app_name = 'calenderapp'


urlpatterns = [
    path('calender/', views.CalendarViewNew.as_view(), name='calendar'),
    path('calenders/', views.CalendarView.as_view(), name='calendars'),
    path('event/new/', views.create_event, name='event_new'),
    path(
        'event/edit/<int:pk>/', views.EventEdit.as_view(), name='event_edit'
    ),
    path(
        'event/<int:event_id>/details/', views.event_details,
        name='event-detail'
    ),
    path(
        'add_eventmember/<int:event_id>', views.add_eventmember,
        name='add_eventmember'
    ),
    path(
        'event/<int:pk>/remove', views.EventMemberDeleteView.as_view(),
        name="remove_event"
    ),
    path('password/', views.change_password, name='changepassowrd'),
     path('changepass/', views.changepass, name='passwordchange'),
]
