from django.db import models
from gym_core.models import GymnasticsPlayer,KaratePlayer
from django.core.exceptions import ValidationError

class Subscription(models.Model):
    gymnastics_player = models.ForeignKey('gym_core.GymnasticsPlayer', on_delete=models.PROTECT, null=True, blank=True, related_name='subscriptions')
    karate_player = models.ForeignKey('gym_core.KaratePlayer', on_delete=models.PROTECT, null=True, blank=True, related_name='subscriptions') 
    start_date = models.DateField(null=False, blank=False, verbose_name="تاريخ بدء الاشتراك")
    end_date = models.DateField(null=True, blank=True, verbose_name="تاريخ انتهاء الاشتراك")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name="سعر الاشتراك")
    is_paid = models.BooleanField(default=False, verbose_name="تم الدفع")
    gym = models.ForeignKey('club.Gym',on_delete=models.CASCADE,related_name='subscriptions',null=True,blank=True)
    @property
    def active_player(self):
        return self.gymnastics_player or self.karate_player
    
    
    def clean(self):
        super().clean()
        if bool(self.gymnastics_player) == bool(self.karate_player):
            raise ValidationError("يجب إدخال لاعب واحد فقط (إما جمباز أو كاراتيه)")
        else:
            pass

    def __str__(self):
        player = self.active_player
        player_name = player.full_name if player else "لاعب غير معروف"
        payment_status = "تم الدفع" if self.is_paid else "لم يتم الدفع"
        return f"{player_name} - {payment_status}"