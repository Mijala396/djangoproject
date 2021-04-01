
from django.urls import path,include
from . import views
from searchtutor.views import(
        registration_view,
)
app_name = "tutor"



urlpatterns = [
        path('home', views.homePageView),
        path('account/register', views.TutorregCreate.as_view()),
        path('account/register1', views.StudentregCreate.as_view()),
        path('subject/register', views.SubjectCreate.as_view()),
        path('subject/search', views.SubjectListView.as_view()),
        path('register', registration_view,name="register"),
        
]





