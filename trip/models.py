from django.db import models
from user_accounts.models import CustomUser 
from django.utils import timezone

class Trip(models.Model):
    
    AREA_CHOICES = [
        ('Golan','GO' ),
        ('Galil','GA' ),
        ('Negev','NEG' ),
        ('Jerusalem','JRU'),
        ('Tel Aviv','TA'),
    ]


    title = models.CharField(max_length = 200)
    guide = models.ForeignKey(CustomUser,to_field='username',on_delete= models.DO_NOTHING)
    date  = models.DateField()
    # thumbnail = models.ImageField() # needs the pillow lib to work. idk. 
    area = models.CharField(max_length=10,choices=AREA_CHOICES, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

