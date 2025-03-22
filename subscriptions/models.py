from django.db import models

# Create your models here.

from accounts.models import User
from discussions.models import Discussion  

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscriptions")
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name="subscribers")
    created_at = models.DateTimeField(auto_now_add=True)  

