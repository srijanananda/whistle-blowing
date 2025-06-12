from django.db import models
import uuid
import random
import string

def generate_unique_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

class Complaint(models.Model):
    STATUS_CHOICES = [
        ('yet', 'Yet to see'),
        ('accepted', 'Accepted'),
        ('solved', 'Solved'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='complaint_photos/', blank=True, null=True)
    date_of_incident = models.DateField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    tracking_code = models.CharField(max_length=12, unique=True, editable=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='yet')

    def save(self, *args, **kwargs):
        if not self.tracking_code:
            while True:
                code = generate_unique_code()
                if not Complaint.objects.filter(tracking_code=code).exists():
                    self.tracking_code = code
                    break
        super().save(*args, **kwargs)
