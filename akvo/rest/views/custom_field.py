# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


from akvo.rsr.models import OrganisationCustomField, ProjectCustomField

from ..serializers import OrganisationCustomFieldSerializer, ProjectCustomFieldSerializer
from ..viewsets import BaseRSRViewSet, PublicProjectViewSet


class OrganisationCustomFieldViewSet(BaseRSRViewSet):
    """
    """
    queryset = OrganisationCustomField.objects.all()
    serializer_class = OrganisationCustomFieldSerializer
    filter_fields = ('organisation', 'name', 'max_characters', 'section', )


class ProjectCustomFieldViewSet(PublicProjectViewSet):
    """
    """
    queryset = ProjectCustomField.objects.all()
    serializer_class = ProjectCustomFieldSerializer
    filter_fields = ('project', 'name', 'max_characters', 'section', )

    def get_queryset(self, related_to='project__'):
        return super(ProjectCustomFieldViewSet, self).get_queryset(related_to)
