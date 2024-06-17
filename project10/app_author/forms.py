from django.forms import (
    ModelForm,
    
)
from django.utils.safestring import SafeString
from .models import Author


class AuthorForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем классы Bootstrap к каждому виджету поля
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": "col-sm-10 ",
                }
            )
            

    class Meta:
        model = Author
        fields = (
            "fullname",
            "born_date",
            "born_location",
            "description",
            "website",
        )

    def as_p(self):
        """Add CSS Styling to divs"""

        return SafeString(
            super()
            .as_p()
            .replace("<label", "<label class='col-sm-2 col-form-label'")
            .replace("<p>", "<p class='row'>")
        )
