from topic_manager.models import Topic, Reply
from user_manager.models import User

def GetTopic(id):
    try:
        return Topic.objects.get(id=id)
    except:
        return None


def GetReply(id):
    try:
        return Reply.objects.get(id=id)
    except:
        return None