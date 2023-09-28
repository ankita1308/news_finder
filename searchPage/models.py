
# Django core imports
from django.db import models

# Local application imports
from users.models import CustomUser


class UserSearchRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    search_query = models.CharField(max_length=100)
    search_results = models.JSONField()
    entry_time = models.DateTimeField(auto_now_add=True)