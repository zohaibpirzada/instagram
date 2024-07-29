from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Profile, UserPost, Post_comment
from .forms import UserRegisterForm, UserProfileEditForm, ProfileImagePic, CreatePost, Post_comment_form



def index(request):
    if request.user.is_authenticated:
        following = request.user.profile.follow.all()
        user = request.user
        following_post = UserPost.objects.filter(user__profile__in=following).order_by('-created_date')
        context = {"following_post" : following_post, "following" : following}
        return render(request, 'index.html', context)
    else:
        return redirect('login')
def user_logout(request):
    logout(request)
    return redirect('index')
def user_login(request):
    if request.user.is_authenticated:
        messages.success(request, 'You are already login!!')
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user != None:
                login(request, user)
                messages.success(request, f'{username} was Successfully login!! Welcome')
                return redirect('index')
            else:
                messages.success(request, f'{username} Not Found!! Please Try Again')        
        return render(request, 'login.html')
    
def User_Profile(request, username):
    if request.user.is_authenticated:
        user_profile = get_object_or_404(Profile,user__username=username)
        profiles = Profile.objects.exclude(user_id=user_profile.user.id).order_by('?')[:3]
        current_user = request.user.username
        if current_user == user_profile.user.username:
            post = UserPost.objects.filter(user=user_profile.user).order_by('-created_date')
        else:
            post = UserPost.objects.filter(post_status='Public',user=user_profile.user).order_by('-created_date')
        return render(request, 'profile.html', {"profile" : user_profile, "user_profiles" : profiles, "post" : post})
    else:
        messages.success(request, 'You will must be logged!!')
        return redirect('index')        
    
def follow(request, username):
    if request.user.is_authenticated:
        user = Profile.objects.get(user__username=username)
        request.user.profile.follow.add(user)
        request.user.profile.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.success(request, 'You will must be logged!!')
        return redirect('index')        
def unfollow(request, username):
    if request.user.is_authenticated:
        user = Profile.objects.get(user__username=username)
        request.user.profile.follow.remove(user)
        request.user.profile.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.success(request, 'You will must be logged!!')
        return redirect('index')
    
def user_register(request):
    if request.user.is_authenticated:
        messages.success(request, 'You are already loggin!!')
        return redirect('index')
    else:
        if request.method == 'POST':
            form = UserRegisterForm(data=request.POST)
            if form.is_valid():
                form.save()
                username = request.POST['username']
                password = request.POST['password1']
                user = authenticate(request, username=username, password=password)
                login(request, user)
                messages.success(request, f'{username} was Successfully Register!!')
                return redirect('index')
        else:
            form = UserRegisterForm()
        return render(request, 'register.html', {"form" : form})
    

def User_Profile_Edit(request):
    if request.user.is_authenticated:
        current_user = get_object_or_404(User,id=request.user.id)
        current_user_profile = get_object_or_404(Profile, user__id=request.user.id)
        if request.method == 'POST':
            form = UserProfileEditForm(request.POST or None, instance=current_user)
            image_form = ProfileImagePic(request.POST or None, request.FILES or None, instance=current_user_profile)
            if form.is_valid() and image_form.is_valid():
                form.save()
                image_form.save()
                messages.success(request, f'{request.user.username} Profile Updated!!')
                return redirect('profile', username=request.user.username)
        else:
            form = UserProfileEditForm(instance=current_user)
            image_form = ProfileImagePic(instance=current_user_profile)
        context = {"form" : form, "image_form" : image_form}
        return render(request, 'edit.html', context)
    else:
        messages.success(request, 'You will must be logged!!')
        return redirect('index')
    
def create_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':  
            form = CreatePost(request.POST or None, request.FILES or None)  
            if form.is_valid():  
                post =form.save(commit=False)  
                post.user = request.user
                post.save()  
                return redirect('profile', username = request.user.username)
        else:  
            form = CreatePost()  
        return render(request, 'create.html', {'form': form})  
    else:
        messages.success(request, 'You will must be logged!!')
        return redirect('index')
    
def post_page(request, post_title):    
    current_post = get_object_or_404(UserPost,id=post_title)
    if request.user.id == current_post.user.id:
        if current_post.post_status == 'Public' or 'Private':
            if request.method == 'POST':
                form = Post_comment_form(request.POST or None)
                if form.is_valid():
                    send =form.save(commit=False)
                    send.post = current_post
                    send.user = request.user
                    send.save()
                    return redirect(request.META.get('HTTP_REFERER'))
            else:
                form = Post_comment_form()
        
            current_post_coment = Post_comment.objects.filter(post__id=current_post.id).order_by('-id')
            context = {'comment' : current_post_coment,'current_post' : current_post, "form" : form}
            return render(request, 'post_page.html', context)
    elif request.user.id != current_post.user.id:
        if current_post.post_status == 'Public':
            if request.method == 'POST':
                form = Post_comment_form(request.POST or None)
                if form.is_valid():
                    send =form.save(commit=False)
                    send.post = current_post
                    send.user = request.user
                    send.save()
                    return redirect(request.META.get('HTTP_REFERER'))
            else:
                form = Post_comment_form()
        
            current_post_coment = Post_comment.objects.filter(post__id=current_post.id).order_by('-id')
            context = {'comment' : current_post_coment,'current_post' : current_post, "form" : form}
            return render(request, 'post_page.html', context)
        elif current_post.post_status == 'Private':
            messages.success(request, 'This post has been private!!')
            return redirect('profile', username=current_post.user.username)
        

def like_post(request, post_title):
    if request.user.is_authenticated:
        post = get_object_or_404(UserPost, id=post_title)
        current_user = request.user
        post.like.add(current_user)
        post.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.success(request, 'You will must be logged!!')
        return redirect('index')

def unlike_post(request, post_title):
    if request.user.is_authenticated:
        post = get_object_or_404(UserPost, id=post_title)
        current_user = request.user
        post.like.remove(current_user)
        post.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.success(request, 'You will must be logged!!')
        return redirect('index')

def delete_post(request, post_id):
    if request.user.is_authenticated:
        current_post = get_object_or_404(UserPost, id=post_id)
        if request.user.id == current_post.user.id:
            current_post.delete()
            messages.success(request, 'Your post has been deleted!!')
            return redirect('profile', username=request.user.username)
        else:
            messages.success(request, 'This is not your post!!')
            return redirect('profile', username=request.user.username)

    else:
        messages.success(request, 'You will must be logged!!')
        return redirect('index')
    
def edit_post(request, edit_post_id):
    if request.user.is_authenticated:
        edit = get_object_or_404(UserPost, id=edit_post_id)
        if request.user.id == edit.user.id:
            if request.method == 'POST':
                form = CreatePost(request.POST or None, request.FILES or None, instance=edit)
                if form.is_valid:
                    form.user = request.user
                    form.save()
                    messages.success(request, 'Post Has Been Edited!!')
                    return redirect('post_page', post_title=edit.id)
            else:
                form = CreatePost(instance=edit)
            return render(request, 'edit_post.html', {"edit" : edit, "form" : form})
        else:
            messages.success(request, 'This is not your post!!')
            return redirect('profile', username=request.user.username)
    else:
        messages.success(request, 'You will must be logged!!')
        return redirect('index')
    
def Explore(request):
    post = UserPost.objects.filter(post_status='Public').exclude(user__id=request.user.id).order_by('?')
    profiles = Profile.objects.exclude(user_id=request.user.id).order_by('?')[:3]
    return render(request, 'explore.html', {"post" : post, "profiles" : profiles})

def search(request):
    user_profiles = Profile.objects.exclude(user__id=request.user.id).order_by("?")
    if request.method == 'GET':
        search_value = request.GET.get('search')
        if search_value != None:
            user_profiles = Profile.objects.filter(user__username__icontains=search_value).exclude(user__id=request.user.id).order_by("?")
        elif search_value == None:
            search_value = ''

    return render(request, 'search.html', {"user_profiles" : user_profiles, "search_value" : search_value})