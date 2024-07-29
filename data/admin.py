from django.contrib import admin
from .models import Profile, UserPost, Post_comment
from django.contrib.auth.models import Group, User

admin.site.unregister(Group)
admin.site.unregister(User)

# admin.site.register(Profile)
class Profiles(admin.StackedInline):
    model = Profile
    
class UserProfile(admin.ModelAdmin):
    model = User
    fields =['username']
    inlines = [Profiles]

admin.site.register(User, UserProfile)
# admin.site.register(pic)
admin.site.register(UserPost)
admin.site.register(Post_comment)
