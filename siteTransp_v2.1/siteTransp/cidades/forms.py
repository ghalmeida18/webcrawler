from django import forms


class SearchForm(forms.Form):
    # TODO: Define form fields here
    dataInicial = forms.CharField(label='Data inicial', required=True)
    dataFinal = forms.CharField(label='Data final', required=True)

    def soma(self):
        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']
        return dataInicial + ' - ' + dataFinal
