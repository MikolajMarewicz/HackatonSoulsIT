from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from PIL import Image



    
class Profile(AbstractUser):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.username} Profile' #show how we want it to be displayed
    
     # Override the save method of the model
    # def save(self):
    #     super().save()

    #     img = Image.open(self.image.path) # Open image

    #     # resize image
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size) # Resize image
    #         # img.save(self.image.path) # Save it again and override the larger image

class Project(models.Model):
    project_name = models.CharField(max_length=30)
    project_budget = models.CharField(max_length=30)
    project_category = models.CharField(max_length=254, null=True, blank=True)
    project_owner = models.ForeignKey(Profile, related_name='%(class)s_requests_created', on_delete=models.CASCADE)
    project_foto = models.CharField(max_length=100, null=True, blank=True)
    project_users = models.ManyToManyField(Profile)
    project_creation_date = models.DateTimeField(auto_now_add=True)
    project_details = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.project_name