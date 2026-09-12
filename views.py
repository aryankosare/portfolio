from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PortfolioForm, ProjectFormSet, SkillFormSet
from .models import Portfolio


def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def builder(request):
    """Create or edit the logged-in user's portfolio, projects and skills."""
    portfolio, _created = Portfolio.objects.get_or_create(
        user=request.user,
        defaults={'full_name': request.user.get_full_name() or request.user.username},
    )

    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        project_formset = ProjectFormSet(request.POST, request.FILES, instance=portfolio, prefix='projects')
        skill_formset = SkillFormSet(request.POST, instance=portfolio, prefix='skills')

        if form.is_valid() and project_formset.is_valid() and skill_formset.is_valid():
            form.save()
            project_formset.save()
            skill_formset.save()
            messages.success(request, 'Your portfolio has been saved!')
            return redirect('preview')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = PortfolioForm(instance=portfolio)
        project_formset = ProjectFormSet(instance=portfolio, prefix='projects')
        skill_formset = SkillFormSet(instance=portfolio, prefix='skills')

    return render(request, 'portfolio/builder.html', {
        'form': form,
        'project_formset': project_formset,
        'skill_formset': skill_formset,
        'portfolio': portfolio,
    })


@login_required(login_url='login')
def preview(request):
    """Preview the logged-in user's own portfolio."""
    portfolio = get_object_or_404(Portfolio, user=request.user)
    return render(request, 'portfolio/preview.html', {
        'portfolio': portfolio,
        'is_owner': True,
    })


def public_portfolio(request, slug):
    """Publicly shareable, read-only portfolio page — no login required."""
    portfolio = get_object_or_404(Portfolio, slug=slug)
    return render(request, 'portfolio/preview.html', {
        'portfolio': portfolio,
        'is_owner': request.user.is_authenticated and request.user == portfolio.user,
    })
