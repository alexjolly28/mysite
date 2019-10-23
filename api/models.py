from django.db import models
from tastypie.resources import ModelResource
from polls.models import Movie


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name='home'

