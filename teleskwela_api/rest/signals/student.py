from django.db.models.signals import post_save
from django.dispatch import receiver

from rest.models import Student
from rest.admin.models import TestModelForm

logger = logging.getLogger(__name__)


@receiver(post_save, sender=TestModelForm)
def post_save_student(sender, instance, *args, **kwargs):
    print("RECEIVER CALLED")
    print("{} - is toggled field".format(instance.toggleAllAwardsField))