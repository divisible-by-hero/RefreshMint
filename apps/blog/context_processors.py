from .models import Post

def blog_months(request):

    return { 'blog_months' : Post.objects.dates('published_date', 'month', order='DESC') }
