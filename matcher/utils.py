from functools import wraps
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from matcher.models import Users, JobSeekers

def is_employee_nocompany(view_func):
    @wraps(view_func)
    def decorated_function(request, *args, **kwargs):
        muser = Users.objects.all().get(authid=request.user.pk)
        if not (muser.usertype == Users.EMPLOYEE):
            return redirect('/matcher/home')
        if (muser.companyid):
            return redirect('/matcher/home')
        return view_func(request, *args, **kwargs)

    return decorated_function

def employee_profilecomplete(view_func):
    @wraps(view_func)
    def decorated_function(request, *args, **kwargs):
        muser = Users.objects.all().get(authid=request.user.pk)
        if not (muser.usertype == Users.EMPLOYEE):
            return redirect('/matcher/home')
        if (muser.profilecompleted == 2):
            return redirect('/matcher/home')
        if not (muser.companyid):
            return redirect('/matcher/home')
        return view_func(request, *args, **kwargs)

    return decorated_function


#Edit company that he owns
def company_owner(view_func):
    @wraps(view_func)
    def decorated_function(request, *args, **kwargs):
        muser = Users.objects.all().get(authid=request.user.pk)
        if not (muser.usertype == Users.EMPLOYEE):
            return redirect('/matcher/home')
        return view_func(request, *args, **kwargs)

    return decorated_function

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


def getCurrentUser(userid):
    try:
        user = Users.objects.get(authid=userid)
    except:
        user = None
    return user
    