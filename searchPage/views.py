from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response

# Local application imports
from users.models import CustomUser
from searchPage.models import UserSearchRecord
from searchPage.utils import get_newsapi_results
from searchPage.serializers import UserHistorySerializer
from datetime import date
import pytz


# Create your views here.
class SearchPage(APIView):
    def get(self, request, query):
        user = CustomUser.objects.get(email=request.user.email)
        data = []
        # Convert the response to JSON format and pretty print it
        if user:
            user_exists = UserSearchRecord.objects.filter(user=user)
            if user_exists:
                try:
                    UserSearchRecord.objects.get(user=user, search_query=query)
                    for record in user_exists:
                        dt = record.entry_time
                        formatted_date = dt.strftime('%Y-%m-%d')
                        if formatted_date != date.today().strftime('%Y-%m-%d'):
                            response = get_newsapi_results(query)
                            response_json = response.json()
                            record.search_results = response_json
                            record.save()
                            your_timezone = pytz.timezone('Asia/Kolkata')  # e.g., 'Asia/Kolkata'
                            timezone.activate(your_timezone)
                            record.entry_time = timezone.now()
                            record.save()
                            timezone.deactivate()
                            data.append(response_json['articles'])

                        data.append(record.search_results['articles'])

                except ObjectDoesNotExist as e:
                    for record in user_exists:
                        data.append(record.search_results['articles'])

                    response = get_newsapi_results(query)
                    response_json = response.json()
                    serializer = UserHistorySerializer(data={
                        'user': user.id,
                        'search_results': response_json,
                        'search_query': query
                    })
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)

                    data.insert(0, response_json['articles'])

            else:
                response = get_newsapi_results(query)
                response_json = response.json()
                serializer = UserHistorySerializer(data={
                    'user': user.id,
                    'search_results': response_json,
                    'search_query': query
                })
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
                data.append(response_json["articles"])

        return data
