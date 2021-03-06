# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


from akvo.rsr.models import Organisation

from ..fields import Base64ImageField

from .organisation_budget import (OrganisationCountryBudgetSerializer,
                                  OrganisationTotalBudgetSerializer,
                                  OrganisationRecipientOrgBudgetSerializer,
                                  OrganisationRegionBudgetSerializer,
                                  OrganisationTotalExpenditureSerializer)
from .organisation_document import OrganisationDocumentSerializer
from .organisation_location import (OrganisationLocationSerializer,
                                    OrganisationLocationExtraSerializer)
from .rsr_serializer import BaseRSRSerializer


class OrganisationSerializer(BaseRSRSerializer):

    total_budgets = OrganisationTotalBudgetSerializer(
        source='total_budgets', many=True, required=False, allow_add_remove=True
    )
    recipient_org_budgets = OrganisationRecipientOrgBudgetSerializer(
        source='recipient_org_budgets', many=True, required=False, allow_add_remove=True
    )
    region_budgets = OrganisationRegionBudgetSerializer(
        source='recipient_region_budgets', many=True, required=False, allow_add_remove=True
    )
    country_budgets = OrganisationCountryBudgetSerializer(
        source='recipient_country_budgets', many=True, required=False, allow_add_remove=True
    )
    total_expenditures = OrganisationTotalExpenditureSerializer(
        source='total_expenditures', many=True, required=False, allow_add_remove=True
    )
    documents = OrganisationDocumentSerializer(
        source='documents', many=True, required=False, allow_add_remove=True
    )
    locations = OrganisationLocationSerializer(
        source='locations', many=True, required=False, allow_add_remove=True
    )
    logo = Base64ImageField(required=False, allow_empty_file=True)

    class Meta:
        model = Organisation


class OrganisationExtraSerializer(OrganisationSerializer):

    primary_location = OrganisationLocationExtraSerializer()

    class Meta(OrganisationSerializer.Meta):
        fields = (
            'id',
            'logo',
            'long_name',
            'name',
            'primary_location',
        )


class OrganisationBasicSerializer(BaseRSRSerializer):

    class Meta:
        model = Organisation
        fields = (
            'id',
            'name',
            'long_name',
            'logo'
        )
