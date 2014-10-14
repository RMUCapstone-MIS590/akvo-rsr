# -*- coding: utf-8 -*-

"""Akvo RSR is covered by the GNU Affero General Public License.
See more details in the license.txt file located at the root folder of the
Akvo RSR module. For additional details on the GNU license please
see < http://www.gnu.org/licenses/agpl.html >.
"""

import json

from akvo.rsr.forms import PasswordForm, ProfileForm, UserOrganisationForm
from akvo.rsr.models import Project, User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext


@login_required
def my_details(request):
    context = RequestContext(request)

    profileForm = ProfileForm(
        initial={
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name
        }
    )
    organisationForm = UserOrganisationForm()

    return render_to_response(
        'myrsr/my_details.html',
        {
            'profileform': profileForm,
            'organisationform': organisationForm
        },
        context_instance=context
    )


@login_required
def password_change(request):
    context = RequestContext(request)
    form = PasswordForm(request.user)
    return render_to_response('myrsr/password_change.html', {'form': form}, context_instance=context)


@login_required
def my_updates(request):
    context = RequestContext(request)
    return render_to_response('myrsr/my_updates.html', context_instance=context)


@login_required
def my_projects(request):
    context = {'projects': Project.objects.published()}
    return render(request, 'myrsr/my_projects.html', context)


@login_required
def user_management(request):
    context = {'users': User.objects.all()}
    return render(request, 'myrsr/user_management.html', context)