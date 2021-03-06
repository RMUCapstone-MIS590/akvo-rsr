# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

from rest_framework import serializers

from akvo.rest.serializers.rsr_serializer import BaseRSRSerializer
from akvo.rest.serializers.user import UserDetailsSerializer
from akvo.rsr.models import IndicatorPeriodData, IndicatorPeriodDataComment


class IndicatorPeriodDataCommentSerializer(BaseRSRSerializer):

    user_details = UserDetailsSerializer(source='user', required=False)

    class Meta:
        model = IndicatorPeriodDataComment


class IndicatorPeriodDataSerializer(BaseRSRSerializer):

    user_details = UserDetailsSerializer(source='user', required=False)
    status_display = serializers.Field(source='status_display')
    photo_url = serializers.Field(source='photo_url')
    file_url = serializers.Field(source='file_url')

    class Meta:
        model = IndicatorPeriodData


class IndicatorPeriodDataFrameworkSerializer(BaseRSRSerializer):

    comments = IndicatorPeriodDataCommentSerializer(many=True, required=False,
                                                    allow_add_remove=True)
    user_details = UserDetailsSerializer(source='user', required=False)
    status_display = serializers.Field(source='status_display')
    photo_url = serializers.Field(source='photo_url')
    file_url = serializers.Field(source='file_url')

    class Meta:
        model = IndicatorPeriodData
