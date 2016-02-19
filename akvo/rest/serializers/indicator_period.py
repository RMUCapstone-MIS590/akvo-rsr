# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

from rest_framework import serializers

from akvo.rest.serializers.rsr_serializer import BaseRSRSerializer
from akvo.rest.serializers.indicator_period_data import IndicatorPeriodDataFrameworkSerializer
from akvo.rsr.models import IndicatorPeriod


class IndicatorPeriodSerializer(BaseRSRSerializer):

    parent_period = serializers.Field(source='parent_period.pk')

    class Meta:
        model = IndicatorPeriod


class IndicatorPeriodFrameworkSerializer(BaseRSRSerializer):

    data = IndicatorPeriodDataFrameworkSerializer(many=True, required=False, allow_add_remove=True)
    parent_period = serializers.Field(source='parent_period.pk')

    class Meta:
        model = IndicatorPeriod
