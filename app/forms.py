from betterforms.multiform import MultiModelForm
from django import forms

from app.models import CV, Contacts


class CVCreateForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = [
            "first_name",
            "last_name",
            "position",
            "salary",
            "education_level",
            "job_category",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["salary"].widget.attrs.update({"required": True})
        self.fields["position"].widget.attrs.update({"required": True})


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ["telegram", "email", "phone", "facebook", "linkedin"]


class CVCreationMultiForm(MultiModelForm):
    form_classes = {
        "cv": CVCreateForm,
        "contacts": ContactsForm,
    }

    def save(self, commit=True):
        objects = super(CVCreationMultiForm, self).save(commit=False)

        if commit:
            contacts = objects["contacts"]
            contacts.save()
            cv = objects["cv"]
            cv.contacts = contacts
            cv.save()
        return objects
