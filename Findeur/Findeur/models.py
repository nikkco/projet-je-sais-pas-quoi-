from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    gender_choices = (
        ("M","male"),
        ("F","female"),
        ("X","X"),
        )
    gender =models.CharField(max_length = 1,choices= gender_choices) 
    interest_choices = (
        ("M","male"),
        ("F","female"),
        ("X","X"),
        )   
    interest = models.CharField(max_length = 1,choices= interest_choices) 
    longitude = models.FloatField(max_length = 20)
    latitude  = models.FloatField(max_length = 20)
    def __str__(self):
        return self.username

class Like (models.Model) :
    voter = models.ForeignKey("User", on_delete=models.CASCADE,related_name = "vote_donné")
    receiver = models.ForeignKey("User", on_delete=models.CASCADE,related_name = "receiver_du_vote")
    like =  models.BooleanField(default=True)
    def __str__(self):
        return f"{self.voter.username}{'liked' if self.like else 'disliked'}{self.receiver.username}"

class Match (models.Model) :
    user1 = models.ForeignKey("User",  on_delete=models.CASCADE,related_name = 'user1_match')
    user2 =  models.ForeignKey("User",  on_delete=models.CASCADE,related_name = 'user2_match')
    def __str__(self):
        return f"Match entre {self.user1.username} et {self.user2.username}"