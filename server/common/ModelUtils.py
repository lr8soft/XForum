from topic_manager.models import Topic
from user_manager.models import User

def GetTopic(id):
    try:
        return Topic.objects.get(id=id)
    except:
        return None