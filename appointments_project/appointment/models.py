from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.doctor_name} - {self.date}"

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField(help_text="Experience in years")
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=4.0)  # Rating out of 5
    profile_image = models.ImageField(upload_to='doctor_images/', null=True, blank=True)

    def __str__(self):
        return self.name