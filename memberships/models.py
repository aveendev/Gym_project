from django.db import models
# from gym_core.models import Player

class Subscription(models.Model):
    # player = models.ForeignKey('gym_core.Player',on_delete=models.CASCADE,related_name='subscriptions', null=False, blank=False)
    start_date = models.DateField(null=False, blank=False, verbose_name="تاريخ بدء الاشتراك ")
    end_date = models.DateField(null=True , blank=True, verbose_name="تاريخ انتهاء الاشتراك ")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name="سعر الاشتراك ")
    is_paid = models.BooleanField(default=False, verbose_name=" تم الدفع ", null=False, blank=False)

    # def __str__ (self):
    #     training = self.player.get_training_type_display()
    #     payment_status = " تم الدفع " if self.is_paid else " لم يتم الدفع "
    #     return f"{self.player.full_name} - {training} - {payment_status}"
