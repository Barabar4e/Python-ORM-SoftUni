from django.urls import reverse_lazy
from django.views import generic as views

from my_music.common.profile_helpers import get_profile


class DetailProfileView(views.DetailView):
	template_name = "profiles/profile-details.html"

	def get_object(self, queryset=None):
		return get_profile()


class DeleteProfileView(views.DeleteView):
	template_name = "profiles/profile-delete.html"
	success_url = reverse_lazy("index")

	def get_object(self, queryset=None):
		return get_profile()
