from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, CommentForm
import pdb

# Create your views here.

def main(request):
    posts = Post.objects
    return render(request, 'main_event.html', {'posts': posts})

def show(request, post_id):
    post = get_object_or_404(Post, pk = post_id )
    return render(request, 'show.html', {'post': post})


def new(request):
    return render(request, 'new.html')

def postcreate(request):
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('main')
    else:
        form = PostForm()
        return render(request, 'new.html', {'form':form})
    
def commentcreate(request, post_id) :
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('show', post_id=post.pk)
    else:
        form = CommentForm()
        return render(request, 'show.html', {'form':form, 'post':post})
    
    