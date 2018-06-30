from karikatura.models import ImageModel
from .serializers import karikaturaSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.utils.urls import replace_query_param,remove_query_param
from django.http import JsonResponse

class StandardResultsSetPagination(PageNumberPagination):
	"""
	პაგინაცია, გადატვირთUლია ზოგიერთი მეთოდი და
	მორგებულია არსებულ სტრუქტურასთან
	"""
	page_size =4 
	page_size_query_param = 'page_size'
	max_page_size = 500



	def get_paginated_response(self, data):
		return Response({
			'pagination': {
				'next': self.get_next_link(),
				'previous': self.get_previous_link(),
				'pages': [replace_query_param(self.request.get_full_path(),self.page_query_param,number) for number in self.page.paginator.page_range],
				'current_page':self.page.number,
			},
			'data': data
		})
	def get_next_link(self):
		if not self.page.has_next():
			return None
		url = self.request.get_full_path()
		page_number = self.page.next_page_number()
		return replace_query_param(url, self.page_query_param, page_number)

	def get_previous_link(self):
		if not self.page.has_previous():
			return None
		url = self.request.get_full_path()
		page_number = self.page.previous_page_number()
		if page_number == 1:
			return remove_query_param(url, self.page_query_param)
		return replace_query_param(url, self.page_query_param, page_number)




class KarikaturebiRestView(generics.ListAPIView):
	serializer_class = karikaturaSerializer
	pagination_class = StandardResultsSetPagination
	def get_queryset(self):
		return ImageModel.objects.all()



def set_name(request):
	if request.method == "POST":
		ImageModel.objects.filter(
			id=request.POST.get("pk")
		).update(
			name=request.POST.get("name")
		)
		return JsonResponse({"answer": True})