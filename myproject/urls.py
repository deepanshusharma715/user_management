from django.contrib import admin
from django.urls import path
from myapp import views
from django.views.generic import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('', RedirectView.as_view(url='signup/')),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
]

