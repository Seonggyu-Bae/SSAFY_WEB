from django.db import models

# Create your models here.

class Garage(models.Model):
    location = models.TextField(max_length=200)
    capacity = models.IntegerField()
    is_parking_available = models.BooleanField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return f' {self.location}의 주차장은 현재 {self.is_parking_available} 이고 {self.opening_time}부터 {self.closing_time} 까지 영업합니다.'
    