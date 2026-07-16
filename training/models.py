from django.db import models
from gym_core.models import *
from django.core.exceptions import ValidationError
class Schedule(models.Model):
    DAYS_OF_WEEK = [
        ('SAT', 'السبت'),
        ('SUN', 'الأحد'),
        ('MON', 'الاثنين'),
        ('TUE', 'الثلاثاء'),
        ('WED', 'الأربعاء'),
        ('THU', 'الخميس'),
        ('FRI', 'الجمعة'),]
    day = models.CharField(max_length=20, choices=DAYS_OF_WEEK, null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    gymnastics_coach = models.ForeignKey('gym_core.GymnasticsCoach', on_delete=models.SET_NULL, null=True, blank=True, related_name='schedules')
    karate_coach = models.ForeignKey('gym_core.KarateCoach', on_delete=models.SET_NULL, null=True, blank=True, related_name='schedules')
    gymnastics_players = models.ManyToManyField('gym_core.GymnasticsPlayer', blank=True, related_name='schedules')
    karate_players = models.ManyToManyField('gym_core.KaratePlayer', blank=True, related_name='schedules')
    gym = models.ForeignKey('club.Gym',on_delete=models.CASCADE,related_name='schedules',null=True,blank=True)
    @property
    def active_coach(self):
        return self.gymnastics_coach or self.karate_coach
    
    def clean(self):
        super().clean()
        if bool(self.gymnastics_coach) == bool(self.karate_coach):
            raise ValidationError('يجب اختيار مدرب واحد فقط (إما جمباز أو كاراتيه)')
        else:
            pass
   
    def __str__ (self):
        day_name = self.get_day_display() if self.day else "يوم غير محدد"
        time_str = self.start_time.strftime('%I:%M %p') if self.start_time else "--:--"
        coach_name = self.active_coach.full_name if self.active_coach else "بدون مدرب"
        return f"موعد الحصة: {day_name} ({time_str} - المدرب: {coach_name})"
    

class Equipment(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="اسم المعدة ",null=False, blank=False)
    quantity = models.PositiveIntegerField(default=0, verbose_name="الكمية المتوفرة ",null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر ",null=False, blank=False)
    last_updated = models.DateTimeField(auto_now=True, verbose_name="آخر تحديث ")
    gym = models.ForeignKey('club.Gym',on_delete=models.CASCADE,related_name='equipments',null=True,blank=True)
    
    def __str__ (self):
        return f"{self.name} - (الكمية: {self.quantity})"

