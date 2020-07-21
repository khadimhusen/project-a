
from django.shortcuts import render, get_object_or_404,redirect
from .models import Feed ,FeedComment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def detail(request, slug):
    feed = get_object_or_404(Feed, slug=slug)
    comments = FeedComment.objects.filter(feed=feed)
    return render(request, 'main/detail.html', {'feed': feed,'comments':comments})

def tags(request, slug=None):
    feeds = Feed.objects.filter(tags__slug=slug)
    return render(request, 'main/find-jobs.html', {'feeds': feeds})



@login_required
def findjobs(request):

    feed = Feed.objects.all()
    comments = FeedComment.objects.filter(feed=feed)
    paginator = Paginator(feed, 3)
    page_number = request.GET.get('page')
    # feeds = paginator.get_page(page_number)
    try:
        feeds = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        feeds = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        feeds = paginator.page(paginator.num_pages)

    return render(request, 'main/find-jobs.html', {'feeds': feeds,'comments':comments})


def feedComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user= request.user
        feedId = request.POST.get("feedId")
        feed = Feed.objects.get(sno=feedId)

        comment = FeedComment(comment=comment,
                              user=user,
                              feed=feed)
        comment.save()
        messages.success(request,"Your comment has been posted successfully.")
    return redirect(f"/feed/{feed.slug}")
