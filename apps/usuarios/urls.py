from django.urls import path

from apps.usuarios.views import LoginView, LogOutView, NewUserView, RegisterNewUser, UpdateEvent, AddNewEvent, \
    DeleteEvent, ListEvents

urlpatterns = [
    # User
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogOutView.as_view(), name='logout'),
    path('new', NewUserView.as_view(), name='new'),
    path('register', RegisterNewUser.as_view(), name='register'),
    # Calendar
    path('update_event', UpdateEvent.as_view(), name='update_event'),
    path('register_event', AddNewEvent.as_view(), name='register_event'),
    path('delete_event', DeleteEvent.as_view(), name='delete_event'),
    path('list_events', ListEvents.as_view(), name='list_events'),
]