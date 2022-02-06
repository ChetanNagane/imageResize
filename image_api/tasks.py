from django_rq import job
from .models import record
from PIL import Image
from django.conf import settings


@job
def imageResize(id):
    small = (140, 140)
    records = record.objects.get(id=id)
    media_url = settings.MEDIA_URL
    try:
        image = Image.open(records.image)
        image.thumbnail(small, Image.LANCZOS)
        image.save(media_url[1:] + str(records.image))
    except Exception as e: print(e)