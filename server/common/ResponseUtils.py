# -*- coding: utf-8 -*-

from common.CommonEnum import ErrorResponse
from django.http import JsonResponse


class EnumResponse:
	def __init__(self, result: ErrorResponse = ErrorResponse.OPERATION_SUCCESS):
		self.response = {"status": result.value}

	def setResult(self, result: ErrorResponse):
		self.response["status"] = result.value

	def setValue(self, key, value):
		self.response[key] = value

	def getResponse(self):
		return JsonResponse(self.response)
