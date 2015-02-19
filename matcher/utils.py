from matcher.models import Users, JobSeekers


def getCurrentUser(userid):
    try:
        user = Users.objects.all().get(authid=userid)
    except:
        user = None
    return user
    