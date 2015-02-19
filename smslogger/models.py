from django.db import models
from django.utils.translation import ugettext as _


class OutgoingManager(models.Manager):
    '''
    A custom manager for LoggedMessage that limits query sets to
    outgoing messages only.
    '''

    def get_query_set(self):
        return super(OutgoingManager, self).get_query_set() \
                .filter(direction=LoggedMessage.DIRECTION_OUTGOING)


class IncomingManager(models.Manager):
    '''
    A custom manager for LoggedMessage that limits query sets to
    incoming messages only.
    '''

    def get_query_set(self):
        return super(IncomingManager, self).get_query_set() \
                        .filter(direction=LoggedMessage.DIRECTION_INCOMING)


class LoggedMessage(models.Model):
    '''
    LoggedMessage model with the following fields:
        date        - date of the message
        direction   - DIRECTION_INCOMING or DIRECTION_OUTGOING
        text        - text of the message
        identity    - identity (ie. phone number) of the message (a string)
        status      - stores message status, (success, error, parse_error, etc)
        response_to - recursive foreignkey to self. Only used for outgoing
                      messages. Points to the LoggedMessage to which the
                      outgoing message is a response.
    Besides the default manager (objects) this model has to custom managers
    for your convenience:
        LoggedMessage.incoming.all()
        LoggedMessage.outgoing.all()
    '''

    class Meta:
        '''
        Django Meta class to set the translatable verbose_names and to create
        permissions. The can_view permission is used by rapidsms to determine
        whether a user can see the tab. can_respond determines if a user
        can respond to a message from the log view.
        '''
        verbose_name = _(u"logged message")
        verbose_name = _(u"logged messages")
        ordering = ['-date', 'direction']
        permissions = (
            ("can_view", _(u"Can view")),
            ("can_respond", _(u"Can respond")),
        )

    DIRECTION_INCOMING = 'I'
    DIRECTION_OUTGOING = 'O'

    DIRECTION_CHOICES = (
        (DIRECTION_INCOMING, _(u"Incoming")),
        (DIRECTION_OUTGOING, _(u"Outgoing")))


    STATUS_SUCCESS = 'success'
    #Outgoing STATUS types:
    STATUS_WARNING = 'warning'
    STATUS_ERROR = 'error'
    STATUS_INFO = 'info'
    STATUS_ALERT = 'alert'
    STATUS_REMINDER = 'reminder'
    STATUS_LOGGER_RESPONSE = 'from_logger'
    STATUS_SYSTEM_ERROR = 'system_error'
    STATUS_PENDING = 'pending'

    #Incoming STATUS types:
    STATUS_MIXED = 'mixed'
    STATUS_PARSE_ERRROR = 'parse_error'
    STATUS_BAD_VALUE = 'bad_value'
    STATUS_INAPPLICABLE = 'inapplicable'
    STATUS_NOT_ALLOWED = 'not_allowed'

    STATUS_CHOICES = (
        (STATUS_SUCCESS, _(u"Success")),
        (STATUS_PENDING, _(u"Pending")),
        (STATUS_WARNING, _(u"Warning")),
        (STATUS_ERROR, _(u"Error")),
        (STATUS_INFO, _(u"Info")),
        (STATUS_ALERT, _(u"Alert")),
        (STATUS_REMINDER, _(u"Reminder")),
        (STATUS_LOGGER_RESPONSE, _(u"Response from logger")),
        (STATUS_SYSTEM_ERROR, _(u"System error")),

        (STATUS_MIXED, _(u"Mixed")),
        (STATUS_PARSE_ERRROR, _(u"Parse Error")),
        (STATUS_BAD_VALUE, _(u"Bad Value")),
        (STATUS_INAPPLICABLE, _(u"Inapplicable")),
        (STATUS_NOT_ALLOWED, _(u"Not Allowed")))

    date = models.DateTimeField(_(u"date"), auto_now_add=True)
    direction = models.CharField(_(u"type"), max_length=1,
                                 choices=DIRECTION_CHOICES,
                                 default=DIRECTION_OUTGOING)
    text = models.TextField(_(u"text"))
    identity = models.CharField(_(u"identity"), max_length=100)
    status = models.CharField(_(u"status"), max_length=32,
                              choices=STATUS_CHOICES, blank=True, null=True)

    response_to = models.ForeignKey('self', verbose_name=_(u"response to"),
                                    related_name='response', blank=True,
                                    null=True)

    #Setup a default manager
    objects = models.Manager()

    # Setup custom managers.  These allow you to do:
    #    LoggedMessage.incoming.all()
    # or
    #    LoggedMessage.outgoing.all()
    incoming = IncomingManager()
    outgoing = OutgoingManager()

    def is_incoming(self):
        '''
        Returns true if this is the log of an incoming message, else false
        '''
        return self.direction == self.DIRECTION_INCOMING

    def __unicode__(self):
        return  u"%(direction)s - %(ident)s - %(text)s" % \
                 {'direction': self.get_direction_display(),
                  'ident': self.identity,
                  'text': self.text}
