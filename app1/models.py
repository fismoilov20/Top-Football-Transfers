from django.db import models

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=60)
    logo = models.FileField(blank=True, null=True)
    country = models.CharField(max_length=60)
    def __str__(self) -> str:
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    transfer_value = models.PositiveSmallIntegerField()
    def __str__(self) -> str:
        return self.name

class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    from_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="transferfrom")
    to_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="transferto")
    transfer_fee = models.PositiveSmallIntegerField()
    transfer_fee_by_tft = models.PositiveSmallIntegerField()
    season = models.CharField(max_length=20, null=True, blank=True)
    def __str__(self) -> str:
        return f"{self.player}, {self.from_club} to {self.to_club}"

