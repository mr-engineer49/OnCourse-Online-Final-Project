from decimal import Decimal
from collections.abc import Iterable

from django.db import models
# from payments.models import BasePayment  # Commented out due to missing module
from courses.models import Course, Enrollment
from users.models import CustomUser

class Payment(models.Model):  # Changed to inherit from models.Model
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='payments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payments', null=True, blank=True, default=None)

    def __str__(self):
        return "Payment of {} for {} for {}".format(self.get_total_amount(), self.user, self.course)
