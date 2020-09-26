from django.core.management.base import BaseCommand, CommandError
from django.http import JsonResponse
from rest_framework.views import APIView
from api.views import TypeAndColorPost
from api.models import ShoeType
from api.serializers import ShoeTypeSerializer, ShoeColorSerializer


class Command(BaseCommand):
    help = 'Submit shoe type and color'
    
    STYLES = [{'style': 'sneaker'}, {'style': 'boot'}, {'style': 'sandal'}, {'style': 'dress'}, {'style': 'other'}]

    COLORS = [{'color_name': 'Red'}, {'color_name': 'Orange'}, {'color_name': 'Yellow'}, {'color_name': 'Green'}, {'color_name': 'Blue'}, {'color_name': 'Indigo'}, {'color_name': 'Violet'}, {'color_name': 'White'}, {'color_name': 'Black'}]
    
    def handle(self, *args, **options):
        for shoestyle in self.STYLES:
            TypeAndColorPost.shoeType(APIView, shoestyle)
        
        for shoecolor in self.COLORS:
            TypeAndColorPost.shoeColor(APIView, shoecolor)
