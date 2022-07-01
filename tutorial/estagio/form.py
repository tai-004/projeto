from django import forms
from .models import Estagio

# Model form
class PostarModelForm(forms.ModelForm):
    class Meta:
        model = Estagio
        fields = ["file", "titulo", "descricao"]

    def clean_file(self):
        file = self.cleaned_data['file']
        ext = file.name.split('.')[-1].lower()
        if ext not in ["pdf"]:
            raise forms.ValidationError("Somente arquivos pdf são permitidos.")
        # return cleaned data is very important.
        return file