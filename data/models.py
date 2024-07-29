from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(User, auto_now=True)
    profile_image = models.ImageField(upload_to='image', null=True, blank=True, default='default.jpg' )
    follow = models.ManyToManyField('self', related_name='following', symmetrical=False, blank=True)
    user_bio = models.CharField(max_length=200, null=False, blank=True)
    user_facebook = models.CharField(max_length=200, null=False, blank=True)
    user_website = models.CharField(max_length=200, null=False, blank=True)
    user_instagram = models.CharField(max_length=200, null=False, blank=True)
    def __str__(self):
        return f"{self.user.username}'s Profile"


POST_STATUS = (
    ('Private' , 'Private'),
    ('Public' , 'Public'),
)

class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=250)
    Title = models.CharField(max_length=250)
    post_image = models.ImageField(upload_to='post_image')
    post_status = models.CharField(max_length=20, choices=POST_STATUS, default='Public')
    like = models.ManyToManyField(User, related_name='post_like', blank=True)

    def __str__(self):
        return f"{self.body[0:20]}... {self.user.username}'s Post"
    
@receiver(post_save, sender=User)
def CreateProfile(sender, instance, created, **kwargs):
    if created:
        new_user = Profile(user=instance)
        new_user.save()
        new_user.follow.set([instance.profile.id])
        new_user.save()

# post_save.connect(CreateProfile ,sender=User)


class Post_comment(models.Model):
    post = models.ForeignKey(UserPost, related_name='comment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    def __str__(self) -> str:
        return f"{self.body[:20]}... {self.user.username}"
