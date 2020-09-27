from django.core.management.base import BaseCommand, CommandError
from django.http import JsonResponse
from rest_framework.views import APIView
from api.views import TypeAndColorPost
from api.models import ShoeType, ShoeColor
from api.serializers import ShoeTypeSerializer, ShoeColorSerializer

# help from Ruben Espino

class Command(BaseCommand):
    help = 'Submit shoe type and color'
    

    
    def handle(self, *args, **options):
        STYLES = ['sneaker', 'boot', 'sandal', 'dress', 'other']
        COLORS = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'White', 'Black']
        
        for shoestyle in STYLES:
            ShoeType.objects.create(style=shoestyle)
        
        for shoecolor in COLORS:
            ShoeColor.objects.create(color_name=shoecolor)
