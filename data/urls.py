
from django.urls import path
import data.views as views



urlpatterns = [
    path('uploader/',views.FileUploader,name='uploader'),

    path('table/',views.table,name='table'),

    path('deletedata/<int:id>/',views.deletefiles,name='delete'),

    path('updatedata/<str:id>/', views.updatefiles,name="update")

]
