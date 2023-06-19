from django.db import models
# import uuid

# Create your models here.

class position(models.Model):
    title=models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class employee(models.Model):
    fullname = models.CharField(max_length=254)
    mobile = models.CharField(max_length=12)
    emp_code = models.CharField(max_length=254)
    position = models.ForeignKey(position,on_delete=models.CASCADE)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.fullname  