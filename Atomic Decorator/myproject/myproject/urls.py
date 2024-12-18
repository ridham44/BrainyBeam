from django.urls import path
from myapp.views import SaveDataView, home_view

urlpatterns = [
    path('', home_view, name='home'),  # Add a dedicated home view
    path('class-view/', SaveDataView.as_view(), name='class_view'),
]
