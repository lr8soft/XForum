from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common import SessionUtils, CommonEnum, ModelUtils
from common.ResponseUtils import EnumResponse
from topic_manager.models import Topic, Reply


# Create your views here.
@require_http_methods(['POST'])
def create_new_topic(request):
    response = EnumResponse()
    # 检测是否登录
    if not SessionUtils.IsLogin(request):
        response.setResult(CommonEnum.ErrorResponse.NOT_LOGIN)
        return response.getResponse()

    title = request.POST.get("title")
    article = request.POST.get("article")
    # 检测输入是否完整
    if not title or not article:
        response.setResult(CommonEnum.ErrorResponse.INCOMPLETE_DATA)
        return response.getResponse()

    user = SessionUtils.GetUser(request)

    try:
        newTopic = Topic.objects.create(title=title, author=user)
        firstReply = Reply.objects.create(article=article, author=user, topic=newTopic, floor=1)
    except:
        response.setResult(CommonEnum.ErrorResponse.OPERATION_FAIL)

    return response.getResponse()