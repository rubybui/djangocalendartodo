from django.db import models


"""declaring the Event model in cal/models.py:"""
#an event needs to have a title (not more than 200 chars in length), a description field, start time and end time.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

