from django.urls import path
from myapp import views



urlpatterns =[
    path('studentdb/',views.studentdb,name="studentdb"),
    path('savestudent/',views.savestudent,name="savestudent"),
    path('displaydata/',views.displaydata,name="displaydata"),
    path('editpage/<int:dataid>/',views.editpage,name="editpage"),
    path('updatestudent/<int:dataid>/',views.updatestudent,name="updatestudent"),
    path('deletestudent/<int:dataid>/',views.deletestudent,name="deletestudent")


]