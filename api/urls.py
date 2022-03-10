from django.urls import re_path
from api.sample.sample_views import sampleView

urlpatterns = [
    re_path('sample', sampleView),
]

