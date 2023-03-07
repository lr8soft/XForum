# -*- coding: utf-8 -*-

from enum import Enum


class ErrorResponse(Enum):
	NOT_LOGIN = "not_login"
	INCOMPLETE_CERTIFICATE = "incomplete_certificate"
	WRONG_CERTIFICATE = "wrong_certificate"

	USER_EXISTED = "user_existed"
	USER_NOT_EXIST = "user_not_exist"

	PERMISSION_DENIED = "permission_denied"

	NO_UPLOAD_FILE = "no_upload_file"
	FILE_NOT_EXIST = "file_not_exist"

	INVALID_ARGUMENT = "invalid_argument"
	INCOMPLETE_DATA = "incomplete_data"
	OPERATION_SUCCESS = "operation_success"
	OPERATION_FAIL = "operation_fail"

	TOPIC_NOT_EXIST = "topic_not_exist"
