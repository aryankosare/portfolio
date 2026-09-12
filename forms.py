from django import forms
from django.forms import inlineformset_factory

from .models import Portfolio, Project, Skill


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = [
            'full_name', 'tagline', 'bio',
            'email', 'phone', 'location',
            'profile_image', 'resume',
            'github_url', 'linkedin_url', 'twitter_url',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'tagline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Full Stack Developer'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Tell visitors about yourself...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City, Country'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/...'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://linkedin.com/in/...'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://twitter.com/...'}),
        }


ProjectFormSet = inlineformset_factory(
    Portfolio,
    Project,
    fields=['title', 'description', 'link', 'image'],
    extra=1,
    can_delete=True,
    widgets={
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project title'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'What did you build?'}),
        'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
        'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    },
)

SkillFormSet = inlineformset_factory(
    Portfolio,
    Skill,
    fields=['name', 'proficiency'],
    extra=1,
    can_delete=True,
    widgets={
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Python'}),
        'proficiency': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
    },
)
