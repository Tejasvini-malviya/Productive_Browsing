from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import *
from .forms import *
from django.http import JsonResponse

# Create your views here.

@login_required
def dashboard(request):
    usage_logs = UsageLog.objects.filter(user=request.user)
    restricted_sites = RestrictedSite.objects.filter(user=request.user)
    time_limits = TimeLimit.objects.filter(user=request.user)
    context = {
        'usage_logs': usage_logs,
        'restricted_sites': restricted_sites,
        'time_limits': time_limits,
    }
    return render(request, 'dashboard.html', context)

@login_required
def add_restricted_site(request):
    if request.method == 'POST':
        form = RestrictedSiteForm(request.POST)
        if form.is_valid():
            restricted_site = form.save(commit=False)
            restricted_site.user = request.user
            restricted_site.save()
            return redirect('/')
    else:
        form = RestrictedSiteForm()
    return render(request, 'add_restricted_site.html', {'form': form})

@login_required
def delete_restricted_site(request, site_id):
    restricted_site = RestrictedSite.objects.get(id=site_id, user=request.user)
    if restricted_site:
        restricted_site.delete()
    return redirect('/')

@login_required
def add_time_limit(request):
    if request.method == 'POST':
        form = TimeLimitForm(request.POST)
        if form.is_valid():
            time_limit = form.save(commit=False)
            time_limit.user = request.user
            time_limit.save()
            return redirect('/')
    else:
        form = TimeLimitForm()
    return render(request, 'add_time_limit.html', {'form': form})

@login_required
def delete_time_limit(request, limit_id):
    time_limit = TimeLimit.objects.get(id=limit_id, user=request.user)
    if time_limit:
        time_limit.delete()
    return redirect('/')

class AllUrlsDataView(View):
    def get(self, request):
        all_urls_data = list(UsageLog.objects.values('url', 'time_spent', 'visit_date', 'active_time', 'idle_time'))
        return JsonResponse({'data': all_urls_data})