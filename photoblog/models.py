from django.db import models
from imagekit.models import ImageModel
import datetime

class Entry(ImageModel):
    title = models.CharField(max_length=300)
    slug = models.SlugField()
    pub_date = models.DateField(default=datetime.datetime.today)
    body = models.TextField(blank=True)
    original_image = models.ImageField(upload_to="storage/photoblog/original")
    num_views = models.PositiveIntegerField(editable=False, default=0)
    published = models.BooleanField(default=True)
    
    def snippet(self):
        return self.body[:50] + ('...' if len(self.body) > 50 else '')
    
    class IKOptions:
        spec_module = 'photoblog.specs'
        cache_dir = 'storage/photoblog/cache'
        image_field = 'original_image'
        save_count_as = 'num_views'
    
