
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),                # URL for admin page
    path('home/', TemplateView.as_view(template_name='account/index.html'), name='home'),  # View home.html page
    path('accounts/', include('allauth.urls')),     # predefined URLs provided by allauth library

]
