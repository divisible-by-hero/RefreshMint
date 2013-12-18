from django.db import models
from localflavor.us.us_states import CONTIGUOUS_STATES

# This may be abstracted later into "core"


class Address(models.Model):
    street1 = models.CharField(max_length=250)
    street2 = models.CharField(max_length=250, required=False)
    state = models.CharField(choices=CONTIGUOUS_STATES)
    zip_code = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return self.street1


class Event(models.Model):
    title = models.CharField(max_length=250)
    start = models.DateTimeField()
    description = models.TextField()
    address = models.ForeignKey(Address, blank=True, null=True)
    image = models.ImageField(upload_to='events/event')

    def __unicode__(self):
        return self.title


class RSVP(models.Model):
    event = models.ForeignKey(Event, blank=True, null=True)
    

