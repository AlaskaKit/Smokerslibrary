from django.shortcuts import render
from rest_framework import serializers, viewsets, routers
from lib_web.models import Author, Book
from django.views.generic import TemplateView

# Create your views here.


class AuthorSerializer(serializers.ModelSerializer):
	#books = serializers.SlugRelatedField("name", read_only=True, many=True)
	class Meta:
		model = Author
		fields = "__all__"


class AuthorViewSet(viewsets.ModelViewSet):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer
	
	
class BookSerializer(serializers.ModelSerializer):
	author = AuthorSerializer(read_only=True)
	author_id = serializers.IntegerField(write_only=True)
	class Meta:
		model = Book
		fields = "__all__"


class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	
	
router = routers.DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)

