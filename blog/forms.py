from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError
from blog.models import Blog
from django.conf import settings

FORBIDDEN_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class BlogForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Blog
        exclude = ["created_at", "updated_at", "views_count"]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        lowered_title = list(map(lambda word: word.lower(), title.split()))
        if any(element in lowered_title for element in FORBIDDEN_WORDS):
            raise ValidationError("Название не может содержать такое слово")
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        lowered_content = list(map(lambda word: word.lower(), content.split()))
        if any(element in lowered_content for element in FORBIDDEN_WORDS):
            raise ValidationError("Статья не может содержать такое слово")
        return content

    def clean_image(self):
        image = self.cleaned_data.get('image')
        extension = image.name.split('.')[-1]
        if image and image.size > settings.UPLOAD_FILE_MAX_SIZE:
            raise ValidationError("Размер изображения не должен превышать 5 МБ ")
        elif not extension or extension.lower() not in settings.WHITELISTED_IMAGE_TYPES.keys():
            raise ValidationError('Изображение может быть только в формате "png", "jpg", "jpeg"')
        return image
