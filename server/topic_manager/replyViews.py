from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common import SessionUtils, CommonEnum, ModelUtils
from common.ResponseUtils import EnumResponse
from topic_manager.models import Topic, Reply


@require_http_methods(['POST'])
def get_topic_replies(request):
    response = EnumResponse()

    topicId = request.POST.get("id")
    # 检测输入完整
    if not topicId:
        response.setStatus(CommonEnum.ErrorResponse.INCOMPLETE_DATA)
        return response.getResponse()

    topic = ModelUtils.GetTopic(topicId)
    # 检测主题是否存在
    if not topic:
        response.setStatus(CommonEnum.ErrorResponse.TOPIC_NOT_EXIST)
        return response.getResponse()

    # 过滤主题下所有回复
    try:
        replies = Reply.objects.filter(topic=topic)
        result = []
        for r in replies:
            avatarPath = r.author.avatar.path if r.author.avatar is None else ""
            reply = {"id": r.id, "article": r.article, "author": r.author.username, "floor": r.floor, "avatar": avatarPath}
            result.append(reply)
        response.setResult(result)
    except Exception as error:
        response.setStatus(CommonEnum.ErrorResponse.OPERATION_FAIL)
        print(error)

    return response.getResponse()



@require_http_methods(['POST'])
def create_new_reply(request):
    response = EnumResponse()

    # 检测是否登录
    if not SessionUtils.IsLogin(request):
        response.setStatus(CommonEnum.ErrorResponse.NOT_LOGIN)
        return response.getResponse()

    topicId = request.POST.get("id")
    reply = request.POST.get("reply")
    # 检测输入是否完整
    if not topicId or not reply or len(reply) == 0:
        response.setStatus(CommonEnum.ErrorResponse.INCOMPLETE_DATA)
        return response.getResponse()

    user = SessionUtils.GetUser(request)
    topic = ModelUtils.GetTopic(topicId)
    # 检测主题是否存在
    if not topic:
        response.setStatus(CommonEnum.ErrorResponse.TOPIC_NOT_EXIST)
        return response.getResponse()

    reply = str(reply).replace(r'\n', '<br/>').replace(r'\r\n', '<br/>').replace(' ', '&nbsp;')

    try:
        # 新回复楼层自动+1
        newFloor = topic.currentfloor + 1
        Reply.objects.create(article=reply, author=user, topic=topic, floor=newFloor)
        topic.currentfloor = newFloor
        topic.save()
    except:
        response.setStatus(CommonEnum.ErrorResponse.OPERATION_FAIL)

    return response.getResponse()