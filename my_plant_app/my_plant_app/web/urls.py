from django.urls import path
from my_plant_app.web.views import index

urlpatterns = (
	path("", index, name='index'),
)
