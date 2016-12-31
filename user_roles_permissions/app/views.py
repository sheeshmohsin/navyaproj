import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from app.models import *

# Create your views here.
def user_permissions(request, pk):
	if request.method == 'GET':
		permissions = []
		user = get_object_or_404(User, id=pk)

		for role in user.roles.all():
			permissions.extend(role.permissions.values_list(flat=True))

		return HttpResponse(json.dumps(list(set(permissions))))
	else:
		return HttpResponseNotAllowed('Only GET here')

@csrf_exempt
def check_permission(request):
	if request.method == 'GET':
		user_id = request.GET.get('userid', None)
		permission_id = request.GET.get('permissionid', None)

		if not user_id and not permission_id:
			raise Http404

		user = get_object_or_404(User, id=user_id)
		permission = get_object_or_404(Permission, id=permission_id)

		permissions = []
		for role in user.roles.all():
			permissions.extend(role.permissions.values_list('id', flat=True))
		if permission_id in permissions:
			return HttpResponse(json.dumps(True))
		else:
			return HttpResponse(json.dumps(False))
	else:
		return HttpResponseNotAllowed('Only GET here')


@csrf_exempt
def modify_permission(request, pk):
	if request.method == 'POST':
		permissions = json.loads(request.body).get('permissions', None)
		if not permissions:
			raise Http404
		role = get_object_or_404(Role, id=pk)

		permissions_obj_list = []
		for permission_id in permissions:
			permission = get_object_or_404(Permission, id=permission_id)
			permissions_obj_list.append(permission)
		role.permissions.clear()
		role.permissions.add(*permissions_obj_list)
		return HttpResponse("Ok")
	else:
		return HttpResponseNotAllowed('Only POST here')

@csrf_exempt
def delete_permission(request, pk):
	if request.method == 'DELETE':
		permission = get_object_or_404(Permission, id=pk)
		permission.delete()
		return HttpResponse('ok')
	else:
		return HttpResponseNotAllowed('Only DELETE here')


