# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from akvo.rsr.reports import FORMATS, REPORTS


@api_view(['GET'])
def reports(request):
    """
    A view for displaying all report information, sorted by title.
    """
    return Response({
        'count': len(REPORTS),
        'results': sorted(REPORTS, key=lambda k: k['title'])
    })


@api_view(['GET'])
def report_formats(request):
    """
    A view for displaying all report format information.
    """
    return Response({
        'count': len(FORMATS),
        'results': FORMATS
    })
