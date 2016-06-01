from datetime import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from .models import Post
from .forms import PostForm




def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'list.html', context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'detail.html', context)


def create_view(request):
    # First, determine if the request has POST data. If it does
    # then validate and save the data to the database as a new
    # blog post. If there is no POST data, then, create a new
    # creation form and render it.

    if (request.method == "POST"):
        pform = PostForm(request.POST)
        if pform.is_valid():
            # Save the form but don't commit to the DB yet
            # so that we can do some additional work.
            post = pform.save(commit=False)
            # Get a user model instance for the current user
            # and use it as the author
            user = User.objects.get(username=request.user)
            post.author = user
            # Publish the post "now"
            post.published_date = datetime.now()
            # Save the post to the DB
            post.save()
            # Send the user over to a page to view their new post
            return HttpResponseRedirect(reverse(detail_view, kwargs={'post_id': post.pk}))
            # Well, that bites, the form didn't validate properly.
            # Show it to the user so they can fix it.
            pass
    else:
        pform = PostForm()

    context = {'form': pform}
    return render(request, 'create.html', context)
