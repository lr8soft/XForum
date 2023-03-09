from django.urls import path

from . import topicViews, replyViews

urlpatterns = [
    path("create_new_topic", topicViews.create_new_topic),
    path("get_pagination_topics", topicViews.get_pagination_topics),

    path("get_pagination_topic_replies", replyViews.get_pagination_topic_replies),
    path("create_new_reply", replyViews.create_new_reply),

]