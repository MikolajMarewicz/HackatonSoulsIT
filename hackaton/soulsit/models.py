from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from PIL import Image

class Project(models.Model):
    project_name = models.CharField(max_length=30)
    project_budget = models.CharField(max_length=30)
    project_category = models.CharField(max_length=254)
    project_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_foto = models.CharField(max_length=100)
    project_users = models.CharField(max_length=100)
    project_creation_date = models.DateTimeField(auto_now_add=True)
    project_details = models.CharField(max_length=100)


    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed
    
     # Override the save method of the model
    def save(self):
        super().save()

        img = Image.open(self.image.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image