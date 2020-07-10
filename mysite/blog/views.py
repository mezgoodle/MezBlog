from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from .models import Post


def PostList(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    return render(request, template_name, {'post_list': posts})


def PostDetail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render (request, template_name, {'post': post,
                                            'comments': comments,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form})