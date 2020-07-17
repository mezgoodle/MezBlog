from .forms import CommentForm, EmailPostForm
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
from .models import Post


def PostList(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(posts, 3)  # 3 posts in each page
    page = request.GET.get('page')
    template_name = 'blog/index.html'
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, template_name, {'page': page,
                                           'post_list': post_list
                                           })


def PostDetail(request, slug):
    template_name = 'blog/post_detail.html'
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
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def post_share(request, post_id):
    template_name = 'blog/post_share.html'
    post = get_object_or_404(Post, id=post_id, status=1)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n {cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'admin@mezblog.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, template_name, {'post': post, 'form': form, 'sent': sent})
