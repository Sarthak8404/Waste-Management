from django.db import models
from django.contrib.auth.models import User

class WasteCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Waste Categories"

class WasteRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('scheduled', 'Scheduled'),
        ('collected', 'Collected'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(WasteCategory, on_delete=models.CASCADE)
    description = models.TextField()
    address = models.TextField()
    quantity = models.CharField(max_length=50, help_text="e.g., 2 bags, 10kg")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_date = models.DateField(null=True, blank=True)
    collected_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.category.name} - {self.status}"
    
    class Meta:
        ordering = ['-created_at']

class CollectionSchedule(models.Model):
    area = models.CharField(max_length=200)
    day_of_week = models.CharField(max_length=20)
    time_slot = models.CharField(max_length=50)
    waste_types = models.ManyToManyField(WasteCategory)
    
    def __str__(self):
        return f"{self.area} - {self.day_of_week}"