# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


from akvo.rsr.models import ProjectCondition

from ..serializers import ProjectConditionSerializer
from ..viewsets import PublicProjectViewSet


class ProjectConditionViewSet(PublicProjectViewSet):
    """
    """
    queryset = ProjectCondition.objects.all()
    serializer_class = ProjectConditionSerializer
    filter_fields = ('project', 'type', )

    def get_queryset(self, related_to='project__'):
        return super(ProjectConditionViewSet, self).get_queryset(related_to)
