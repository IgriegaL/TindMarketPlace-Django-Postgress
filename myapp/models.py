from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    TEMAS_CHOICES = (
        ('Deporte', 'Deporte'),
        ('Aire Libre', 'Aire Libre'),
        ('VideoJuegos', 'VideoJuegos'),
        ('Ofimatica', 'Ofimatica'),
        ('Vacaciones', 'Vacaciones'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    tema = models.CharField(max_length=255, choices=TEMAS_CHOICES, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username
