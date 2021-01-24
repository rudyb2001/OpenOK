from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    title = forms.CharField(label='Title',
        widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "A description of the course",
                "class": "new-class-name two",
                "id": "textarea1",
                "rows": 10,
                "cols": 30
            }
        )
    )
    resources = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "The resources included for your course",
                "class": "new-class-name three",
                "id": "textarea2",
                "rows": 10,
                "cols": 30
            }
        )
    )

    class Meta:
        model = Course
        fields = [
            "title",
            "description",
            "resources" #,
            #"password"
        ]
    
    """
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        return title
    """

class RawCourseForm(forms.Form):
    title = forms.CharField(label='Title',
        widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "A description of the course",
                "class": "new-class-name two",
                "id": "textarea1",
                "rows": 10,
                "cols": 30
            }
        )
    )
    resources = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "The resources included for your course",
                "class": "new-class-name three",
                "id": "textarea2",
                "rows": 10,
                "cols": 30
            }
        )
    ) 