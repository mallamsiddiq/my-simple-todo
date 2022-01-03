from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    execution_date= models.DateTimeField()

    class Meta:
    	ordering = ['-execution_date']
    def __str__(self):
        return (f"{self.title}, @ {self.execution_date}")
    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.pk})

