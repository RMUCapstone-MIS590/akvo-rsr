# -*- coding: utf-8 -*-
"""Akvo RSR is covered by the GNU Affero General Public License.
See more details in the license.txt file located at the root folder of the Akvo RSR module.
For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.
"""

from akvo.rest.serializers.rsr_serializer import BaseRSRSerializer
from akvo.rsr.models import (OrganisationDocument, OrganisationDocumentCategory,
                             OrganisationDocumentCountry)


class OrganisationDocumentCategorySerializer(BaseRSRSerializer):

    class Meta:
        model = OrganisationDocumentCategory


class OrganisationDocumentCountrySerializer(BaseRSRSerializer):

    class Meta:
        model = OrganisationDocumentCountry


class OrganisationDocumentSerializer(BaseRSRSerializer):

    categories = OrganisationDocumentCategorySerializer(
        source='categories', many=True, required=False, allow_add_remove=True
    )
    countries = OrganisationDocumentCountrySerializer(
        source='countries', many=True, required=False, allow_add_remove=True
    )

    class Meta:
        model = OrganisationDocument
