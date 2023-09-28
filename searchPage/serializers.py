# Third party imports
from rest_framework import serializers

# Local application imports
from .models import UserSearchRecord


class UserHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSearchRecord
        fields = ['user', 'search_results', 'search_query']