# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

from akvo.rest.serializers.rsr_serializer import BaseRSRSerializer
from akvo.rsr.models import IndicatorPeriodActualDimension, IndicatorPeriodTargetDimension

from rest_framework import serializers


class IndicatorPeriodActualDimensionSerializer(BaseRSRSerializer):

    period_unicode = serializers.Field(source='period')

    class Meta:
        model = IndicatorPeriodActualDimension


class IndicatorPeriodTargetDimensionSerializer(BaseRSRSerializer):

    period_unicode = serializers.Field(source='period')

    class Meta:
        model = IndicatorPeriodTargetDimension
