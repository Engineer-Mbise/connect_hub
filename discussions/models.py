from django.db import models

# Create your models here.

class Module(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Discussion(models.Model):
    title = models.CharField(max_length=255)
    #created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    jitsi_meet_url = models.URLField(blank=True, null=True)  # Jitsi meeting link
    is_live = models.BooleanField(default=False)  # Track if discussion is live

    def __str__(self):
        return self.title

