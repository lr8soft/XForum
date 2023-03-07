from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common import CommonEnum, SessionUtils
from common.Encryptor import Encryptor
from common.ResponseUtils import EnumResponse
from user_manager.models import User


# Create your views here.
@require_http_methods(['POST'])
def regist(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    nickname = request.POST.get('nickname')
    email = request.POST.get('email')

    response = EnumResponse()

    if not username or not password or not nickname or not email:
        print(username, password, nickname, email)
        response.setResponseValue(CommonEnum.ErrorResponse.INCOMPLETE_CERTIFICATE)
        return response.getResponse()

    # check user exist
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = None

    if user is None:
        password = Encryptor.md5_encrypt(password)
        user = User.objects.create(
            username=username,
            password=password,
            nickname=nickname,
            email=email
        )
    else:
        response.setResponseValue(CommonEnum.ErrorResponse.USER_EXISTED)

    return response.getResponse()


@require_http_methods(['POST'])
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    response = EnumResponse()
    if not username or not password:
        response.setResponseValue(CommonEnum.ErrorResponse.INCOMPLETE_CERTIFICATE)
        return response.getResponse()

    # check user exist
    try:
        user = User.objects.get(username=username, password=Encryptor.md5_encrypt(password))
    except User.DoesNotExist:
        user = None

    if user:
        SessionUtils.SetIsLogin(request, True, user.username)
    else:
        response.setResponseValue(CommonEnum.ErrorResponse.WRONG_CERTIFICATE)

    return response.getResponse()


@require_http_methods(['POST'])
def logout(request):
    SessionUtils.SetIsLogin(request, False)
    response = EnumResponse()
    return response.getResponse()
