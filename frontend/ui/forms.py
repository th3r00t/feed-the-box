from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(
        label="Search",
        widget=forms.TextInput(
            attrs={
                'id': 'search'
            }
        )
    )


class DownloadForm(forms.Form):
    download_type = forms.MultipleChoiceField(
        choices={
            'Movie': 'm',
            'Tv Show': 't',
            'Other': 'o'
        }
    ),
    download_link = forms.HiddenInput(
        attrs={
            'id': 'magnet'
        }
    ),
    csrf_token = forms.HiddenInput(
        attrs={
            'id': 'csrfmiddlewaretoken'
        }
    )
