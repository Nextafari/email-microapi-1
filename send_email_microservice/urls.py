"""send_email_microservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
		https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
		1. Add an import:  from my_app import views
		2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
		1. Add an import:  from other_app.views import Home
		2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
		1. Import the include() function: from django.urls import include, path
		2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
# from rest_framework_swagger.views import get_swagger_view

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view, SwaggerUIRenderer
from drf_yasg import openapi

# schema_view = get_swagger_view(title="Send Email Docs")
SwaggerUIRenderer.template = 'drf-yasg.html'

schema_view = get_schema_view(
	openapi.Info(
		title="Send Mail API",
		default_version='v1',
		description="A simple service for sending emails.",
	),
	url='https://email.microapi.dev/v1/',
	public=True,
	permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/documentation/', schema_view.as_view(), {'format': '.json'}, name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('v1/', include('api.urls')),
    path('v1/', include('awsmail.urls')),
    path('v1/', include('aws_sns.urls')),
	path('v1/', include('registration.urls')),
	path('v1/', include('confirmation.urls')),
	path('v1/', include('invitation.urls')),
	path('v1/', include('newsletter.urls')),
	path('v1/', include('send_certificate.urls')),
	path('v1/bouncy/', include('django_bouncy.urls')),
    # path('v1/', include('Greetings_mail.urls')),
]
