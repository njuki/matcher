from smslogger.models import LoggedMessage

def get_pending():
    try:
        results = LoggedMessage.outgoing.filter(status=LoggedMessage.STATUS_PENDING)
        if results.count() == 0:
            results = false
    except:
        results =  false

    return results
