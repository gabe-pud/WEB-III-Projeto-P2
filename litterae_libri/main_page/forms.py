from django import forms
from institucional.models import Contato

class ContatoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-indigo-500 focus:border-indigo-500 transition duration-150 shadow-sm',
                'placeholder': field.label
            })
        self.fields['mensagem'].widget.attrs.update({'rows': 4})

    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']
        labels = {
            'nome': 'Seu Nome Completo',
            'email': 'Seu Melhor E-mail',
            'mensagem': 'Sua Mensagem ou Dúvida',
        }