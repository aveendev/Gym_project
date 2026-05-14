from django.db import models
from gym_core.models import Player, Coach
class Schedule(models.Model):
    DAYS_OF_WEEK = [
        ('SAT', 'السبت'),
        ('SUN', 'الأحد'),
        ('MON', 'الاثنين'),
        ('TUE', 'الثلاثاء'),
        ('WED', 'الأربعاء'),
        ('THU', 'الخميس'),
        ('FRI', 'الجمعة'),
    ]
    day = models.CharField(max_length=20, choices=DAYS_OF_WEEK, null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    coach = models.ForeignKey('gym_core.Coach', on_delete=models.SET_NULL,null=True, blank=True)
    players = models.ManyToManyField('gym_core.Player', blank=True )

    def __str__ (self):
        day_name = self.get_day_display() if self.day else "يوم غير محدد"
        time_str = self.start_time.strftime('%I:%M %p') if self.start_time else "--:--"
        return f"موعد الحصة: {day_name} ({time_str})"
    
class Equipment(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="اسم المعدة ",null=False, blank=False)
    quantity = models.PositiveIntegerField(default=0, verbose_name="الكمية المتوفرة ",null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر ",null=False, blank=False)
    last_updated = models.DateTimeField(auto_now=True, verbose_name="آخر تحديث ")
    
    def __str__ (self):
        return f"{self.name} - (الكمية: {self.quantity})"

