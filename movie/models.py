from django.db import models

# Create your models here.
class CensorInfo(models.Model):
    rating=models.CharField(max_length=10)
    cirtified_by=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.cirtified_by


class movie_info(models.Model):
    Title=models.CharField(max_length=250)
    Year=models.IntegerField(null=True) # Allow blank input in forms
    Summary=models.TextField(null=True)# Allow blank input in forms
    img=models.ImageField(upload_to='images/',null=True,blank=True) # Allow blank image field
    Censor_detail=models.OneToOneField(
        CensorInfo,on_delete=models.SET_NULL,
        related_name='movie',null=True
        )

    def __str__(self):
        return self.Title  # Human-readable representation of the model