from django.urls import path
from utility_bills.views import *


urlpatterns = [

    path('', PaymentsListView.as_view(), name='home'),
    path('detail/<int:pk>', PaymentsDetailView.as_view(), name='detail'),
    path('update/<int:pk>', PaymentsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PaymentsDeleteView.as_view(), name='delete'),
    path('add/', PaymentsCreateView.as_view(), name='create'),

]
