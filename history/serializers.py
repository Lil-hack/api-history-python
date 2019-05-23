from django.contrib.auth.models import User
from rest_framework import serializers

from history.models import History


class HistorySerializer(serializers.HyperlinkedModelSerializer):



    class Meta:
        model = History
        fields = ('uuid', 'created',  'user_uuid', 'video_uuid','url_search_foto','url_find_foto')



