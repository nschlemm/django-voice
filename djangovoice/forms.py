from django import forms
from djangovoice.models import Feedback


class WidgetForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = (
            'email', 'type', 'anonymous', 'private', 'title', 'description')

    def __init__(self, *args, **kwargs):
        super(WidgetForm, self).__init__(*args, **kwargs)

        for field_name in ['title', 'description']:
            field = self.fields[field_name]
            field.widget.attrs = {'class': 'input-block-level'}


class EditForm(forms.ModelForm):
    class Meta:
        model = Feedback
