from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Url
from django.contrib.auth.decorators import login_required
import shortuuid

@csrf_exempt
@login_required
def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        if original_url:
            url, created = Url.objects.get_or_create(original_url=original_url, user=request.user)
            if created:
                url.short_url = shortuuid.ShortUUID().random(length=6)
                url.save()
            return JsonResponse({'short_url': url.short_url})
        else:
            return JsonResponse({'error': 'Invalid URL'})

@csrf_exempt
def redirect_url(request, short_url):
    url = get_object_or_404(Url, short_url=short_url)
    url.views += 1
    url.save()
    return redirect(url.original_url)

@login_required
def user_urls(request):
    user_urls = Url.objects.filter(user=request.user)
    return render(request, 'url_shortener/user_urls.html', {'user_urls': user_urls})
