# -*- coding: utf-8 -*-

from django.http import HttpRequest

from user_manager.models import User


def IsLogin(request: HttpRequest):
	username = request.session.get("username", None)
	is_login = request.session.get("is_login", False)

	if username and is_login:
		return True

	return False

def SetIsLogin(request: HttpRequest, is_login: bool, username: str):
	if is_login:
		request.session["username"] = username
	else:
		request.session.clear()

	request.session["is_login"] = is_login


def GetUserName(request: HttpRequest):
	if IsLogin(request):
		return request.session.get("username", None)
	return None

def GetUser(request: HttpRequest):
	userName = GetUserName(request)
	if userName:
		try:
			return User.objects.get(username=userName)
		except:
			return None

	return None