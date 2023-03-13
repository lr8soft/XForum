from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common import SessionUtils, CommonEnum, ModelUtils
from common.ResponseUtils import EnumResponse
from core import settings
from topic_manager.models import Reply


@require_http_methods(['POST'])
def get_pagination_topic_replies(request):
    response = EnumResponse()
    # 页码默认是1
    pageNum = request.POST.get("pageNum")
    topicId = request.POST.get("id")
    # 检测输入完整
    if not topicId or not pageNum or not pageNum.isdigit():
        response.setStatus(CommonEnum.ErrorResponse.INCOMPLETE_DATA)
        return response.getResponse()

    topic = ModelUtils.GetTopic(topicId)
    # 检测主题是否存在
    if not topic:
        response.setStatus(CommonEnum.ErrorResponse.TOPIC_NOT_EXIST)
        return response.getResponse()

    pageNum = int(pageNum)
    try:
        # 过滤主题下所有回复
        paginator = Paginator(Reply.objects.filter(topic=topic), settings.PAGINATOR_ITEM_PER_PAGE)
        pageCount = paginator.num_pages
        # 检测页码是否超出范围,[1,n]
        if pageNum < 1 or pageNum > pageCount:
            response.setStatus(CommonEnum.ErrorResponse.PAGE_OUT_OF_RANGE)
            return response.getResponse()

        result = {}
        result['author'] = topic.author.username
        result["title"] = topic.title
        result["pageCount"] = pageCount
        result["pageItemCount"] = settings.PAGINATOR_ITEM_PER_PAGE
        # 读指定页的所有内容
        page = paginator.page(pageNum)
        pageReplies = []
        for r in page:
            avatarPath = r.author.avatar.path if r.author.avatar is None else ""
            reply = {"id": r.id, "article": r.article, "author": r.author.username, "floor": r.floor, "avatar": avatarPath}
            pageReplies.append(reply)

        result["replies"] = pageReplies
        response.setResult(result)

    except Exception as error:
        response.setStatus(CommonEnum.ErrorResponse.OPERATION_FAIL)
        print("get_pagination_topics ERROR:" + error.__str__())



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

    try:
        # 新回复楼层自动+1
        newFloor = topic.currentfloor + 1
        Reply.objects.create(article=reply, author=user, topic=topic, floor=newFloor)
        topic.currentfloor = newFloor
        topic.save()
    except:
        response.setStatus(CommonEnum.ErrorResponse.OPERATION_FAIL)

    return response.getResponse()


@require_http_methods(['POST'])
def delete_reply(request):
    response = EnumResponse()
    # 检测是否登录
    if not SessionUtils.IsLogin(request):
        response.setStatus(CommonEnum.ErrorResponse.NOT_LOGIN)
        return response.getResponse()
    # 检测输入完整
    replyId = request.POST.get("id")
    if not replyId:
        response.setStatus(CommonEnum.ErrorResponse.INCOMPLETE_DATA)
        return response.getResponse()
    # 回复是否存在
    reply = ModelUtils.GetReply(replyId)
    if not reply:
        response.setStatus(CommonEnum.ErrorResponse.REPLY_NOT_EXIST)
        return response.getResponse()

    currentUser = SessionUtils.GetUser(request)
    # 只有主题作者或者本人才能删除
    if reply.author == currentUser or reply.topic.author == currentUser:
        reply.delete()
    else:
        response.setStatus(CommonEnum.ErrorResponse.PERMISSION_DENIED)
    return response.getResponse()