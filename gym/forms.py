from django import forms
from .models import Client, Trainer

class ClientForm(forms.ModelForm):
    trainer = forms.ModelChoiceField(
        queryset=Trainer.objects.all(),
        required=False,
        empty_label="Без тренера",
        label="Виберіть тренера",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Client
        fields = ['full_name', 'phone', 'sub_type', 'trainer', 'photo', 'is_active']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_type': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# НОВА ФОРМА ДЛЯ ТРЕНЕРА
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'specialization', 'rating', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }