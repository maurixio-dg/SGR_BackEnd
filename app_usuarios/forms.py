
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


Usuario = get_user_model()


def grupos_disponibles():
    return Group.objects.filter(
        name__in=[
            'Administrador',
            'Supervisor',
            'Administrativo',
        ]
    ).order_by('name')


class UsuarioCrearForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        label='Correo electrónico'
    )

    grupo = forms.ModelChoiceField(
        queryset=grupos_disponibles(),
        required=True,
        label='Rol del usuario',
        empty_label='Seleccione un rol'
    )

    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for campo in self.fields.values():
            campo.widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['grupo'].widget.attrs.update({
            'class': 'form-select'
        })

    def clean_email(self):
        email = self.cleaned_data['email'].strip()

        if Usuario.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'Este correo electrónico ya está registrado.'
            )

        return email


class UsuarioEditarForm(forms.ModelForm):

    email = forms.EmailField(
        required=True,
        label='Correo electrónico'
    )

    grupo = forms.ModelChoiceField(
        queryset=grupos_disponibles(),
        required=True,
        label='Rol del usuario',
        empty_label='Seleccione un rol'
    )

    class Meta:
        model = Usuario

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
        ]

        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'is_active': 'Usuario activo',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for campo in self.fields.values():
            campo.widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['grupo'].widget.attrs.update({
            'class': 'form-select'
        })

        self.fields['is_active'].widget.attrs.update({
            'class': 'form-check-input'
        })

        if self.instance.pk:
            grupo_actual = self.instance.groups.filter(
                name__in=[
                    'Administrador',
                    'Supervisor',
                    'Administrativo',
                ]
            ).first()

            if grupo_actual:
                self.fields['grupo'].initial = grupo_actual

    def clean_email(self):
        email = self.cleaned_data['email'].strip()

        existe = Usuario.objects.filter(
            email__iexact=email
        ).exclude(
            pk=self.instance.pk
        ).exists()

        if existe:
            raise forms.ValidationError(
                'Este correo electrónico ya está registrado.'
            )

        return email
