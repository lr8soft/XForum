from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.utils.timezone import localtime
from django.core.paginator import Paginator

from common import SessionUtils, CommonEnum, ModelUtils
from common.ResponseUtils import EnumResponse
from core import settings
from topic_manager.models import Topic, Reply


# Create your views here.
@require_http_methods(['POST'])
def create_new_topic(request):
    response = EnumResponse()
    # 检测是否登录
    if not SessionUtils.IsLogin(request):
        response.setStatus(CommonEnum.ErrorResponse.NOT_LOGIN)
        return response.getResponse()

    title = request.POST.get("title")
    article = request.POST.get("article")
    # 检测输入是否完整
    if not title or not article:
        response.setStatus(CommonEnum.ErrorResponse.INCOMPLETE_DATA)
        return response.getResponse()

    user = SessionUtils.GetUser(request)

    try:
        newTopic = Topic.objects.create(title=title, author=user, currentfloor=1, repliesCount=1)
        firstReply = Reply.objects.create(article=article, author=user, topic=newTopic, floor=1)
    except Exception as error:
        response.setStatus(CommonEnum.ErrorResponse.OPERATION_FAIL)
        print(error)

    return response.getResponse()


@require_http_methods(['POST'])
def get_pagination_topics(request):
    response = EnumResponse()
    # 页码默认是1
    pageNum = request.POST.get("pageNum")
    # 检测输入完整
    if not pageNum or not pageNum.isdigit():
        response.setStatus(CommonEnum.ErrorResponse.INCOMPLETE_DATA)
        return response.getResponse()

    pageNum = int(pageNum)

    try:
        paginator = Paginator(Topic.objects.all(), settings.PAGINATOR_ITEM_PER_PAGE)
        pageCount = paginator.num_pages
        # 检测页码是否超出范围,[1,n]
        if pageNum < 1 or pageNum > pageCount:
            response.setStatus(CommonEnum.ErrorResponse.PAGE_OUT_OF_RANGE)
            return response.getResponse()

        result = {}
        result["pageCount"] = pageCount
        result["pageItemCount"] = settings.PAGINATOR_ITEM_PER_PAGE
        # 读指定页的所有内容
        page = paginator.page(pageNum)
        pageTopics = []
        for topic in page:
            info = {"id": topic.id, "title": topic.title, "author": topic.author.username, "repliesCount": topic.repliesCount,
                    "date": topic.date}
            pageTopics.append(info)

        result["topics"] = pageTopics
        response.setResult(result)

    except Exception as error:
        response.setStatus(CommonEnum.ErrorResponse.OPERATION_FAIL)
        print("get_pagination_topics ERROR:" + error.__str__())

    return response.getResponse()


@require_http_methods(['POST'])
def delete_topic(request):
    response = EnumResponse()
    # 检测是否登录
    if not SessionUtils.IsLogin(request):
        response.setStatus(CommonEnum.ErrorResponse.NOT_LOGIN)
        return response.getResponse()
    # 检测输入完整
    topicId = request.POST.get("id")
    if not topicId:
        response.setStatus(CommonEnum.ErrorResponse.INCOMPLETE_DATA)
        return response.getResponse()
    # 主题是否存在
    topic = ModelUtils.GetTopic(topicId)
    if not topic:
        response.setStatus(CommonEnum.ErrorResponse.TOPIC_NOT_EXIST)
        return response.getResponse()

    currentUser = SessionUtils.GetUser(request)
    # 只有主题作者才能删除
    if topic.author == currentUser:
        topic.delete()
    else:
        response.setStatus(CommonEnum.ErrorResponse.PERMISSION_DENIED)
    return response.getResponse()
