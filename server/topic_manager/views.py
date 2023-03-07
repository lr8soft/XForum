from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common import SessionUtils, CommonEnum, ModelUtils
from common.ResponseUtils import EnumResponse
from topic_manager.models import Topic, Reply
from django.utils.timezone import localtime


# Create your views here.
@require_http_methods(['POST'])
def create_new_topic(request):
    response = EnumResponse()
    # 检测是否登录
    if not SessionUtils.IsLogin(request):
        response.setResponseValue(CommonEnum.ErrorResponse.NOT_LOGIN)
        return response.getResponse()

    title = request.POST.get("title")
    article = request.POST.get("article")
    # 检测输入是否完整
    if not title or not article:
        response.setResponseValue(CommonEnum.ErrorResponse.INCOMPLETE_DATA)
        return response.getResponse()

    user = SessionUtils.GetUser(request)

    try:
        newTopic = Topic.objects.create(title=title, author=user, currentfloor=1, repliesCount=1)
        firstReply = Reply.objects.create(article=article, author=user, topic=newTopic, floor=1)
    except:
        response.setResponseValue(CommonEnum.ErrorResponse.OPERATION_FAIL)

    return response.getResponse()


@require_http_methods(['POST'])
def get_all_topics(request):
    response = EnumResponse()

    try:
        topics = Topic.objects.all()
        result = []
        for t in topics:
            info = {}
            info["id"] = t.id
            info["title"] = t.title
            info["author"] = t.author.username
            info["repliesCount"] = t.repliesCount
            info["date"] = localtime(t.date).strftime("%Y-%m-%d %H:%I:%S")
            result.append(info)
        response.setResult(result)
    except Exception as e:
        response.setResponseValue(CommonEnum.ErrorResponse.OPERATION_FAIL)
        print(e)

    return response.getResponse()
