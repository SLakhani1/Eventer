from django.urls import path, include
from . import views
# from django.views.generic import TemplateView

# app_name = 'eventerapp'

urlpatterns = [
	# path('', TemplateView.as_view(template_name="login.html")),
    path('', views.login_page, name='login_page'),
	path('accounts/', include('allauth.urls')),
	path('logout/', views.logout_view, name='logout_view'),
	# path('authorize/', views.authorize_view, name='authorize'),
	# path('wait/', views.waiting_view, name='wait'),
	path('dashboard/', views.dashboard_view, name='dashboard'),
]