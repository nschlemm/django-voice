from django import forms
from djangovoice.models import Feedback


class WidgetForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = (
            'email', 'type', 'anonymous', 'private', 'title', 'description')


class EditForm(forms.ModelForm):
    class Meta:
        model = Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)

        # add class to fix width of title input and textarea:
        for field_name in ['title', 'description']:
            field = self.fields[field_name]
            field.widget.attrs = {'class': 'input-block-level'}
