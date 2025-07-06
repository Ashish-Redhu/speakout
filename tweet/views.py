from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

# 1.
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

# 2.
def tweet_create(request):
    if request.method == 'POST': # This will run when user submit the form.
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False) # This creates a Tweet object but doesn't save it to the database yet.
            tweet.user = request.user  # Assuming you have user authentication
            tweet.save()
            return redirect('tweet_list')  # Redirect to the tweet list after saving
    else: # This will run when user first open the form.
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

# 3.
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)  # We will take out the tweet whose primaryKey = tweeId. Also ensure the tweet belongs to the logged-in user
    if request.method == 'POST': # This will run when user submit the form to edit an existing tweet.
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False) 
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else: # This will run when user first open the form to edit an existing tweet.
        form = TweetForm(instance=tweet) # Pre-populate the form with the existing tweet data
    return render(request, 'tweet_form.html', {'form': form})

# 4.
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)  # Ensure the tweet belongs to the logged-in user
    if request.method == 'POST':  # This will run when user confirm to delete the tweet.
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})  # Render a confirmation page before deletion
