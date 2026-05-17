from django.db import models

# Create your models here.
class Coach(models.Model):
    level_choices = [
        ('a','A'),
        ('b','B'),
        ('c','C'),
        ('d','D'),
    ]

    full_name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=10 , null=False,blank=False)
    training_level = models.CharField(max_length=20,choices=level_choices,null=False,blank=False)
    gym = models.ForeignKey('club.Gym',on_delete=models.CASCADE,related_name='%(app_label)s_%(class)s_coaches',null=True,blank=True)

    class Meta:
        abstract= True

    def __str__(self):
        return f"{self.full_name}"
    
class GymnasticsCoach(Coach):
    pass
class KarateCoach(Coach):
    pass



class Player(models.Model):

    training_type_choices = [
        ('group','Group'),
        ('private','Private'),
    ]
    full_name = models.CharField(max_length=100, null=False, blank=False)
    father_name = models.CharField(max_length=100, null=False, blank=False)
    mother_name = models.CharField(max_length=100, null=False, blank=False)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=10 , null=False,blank=False)
    training_type = models.CharField(max_length=20,choices=training_type_choices,default='group')
    weight = models.DecimalField(max_digits=5,decimal_places=2,null=False,blank=False )
    gym = models.ForeignKey('club.Gym',on_delete=models.CASCADE,related_name='%(app_label)s_%(class)s_players',null=True,blank=True)
    

    class Meta:
        abstract= True

    def __str__(self):
        return f"{self.full_name}"
    
class GymnasticsPlayer(Player):
    gymnastics_coach = models.ForeignKey(GymnasticsCoach,on_delete=models.PROTECT,related_name='g_players')
    
class KaratePlayer(Player):
    karate_coach = models.ForeignKey(KarateCoach,on_delete=models.PROTECT,related_name='k_players')
    
    

