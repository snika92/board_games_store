from django.forms import ModelForm
from django.core.exceptions import ValidationError
from store.models import Game
from django.conf import settings

FORBIDDEN_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"


class GameForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Game
        exclude = ["created_at", "updated_at"]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        lowered_title = list(map(lambda word: word.lower(), title.split()))
        if any(element in lowered_title for element in FORBIDDEN_WORDS):
            raise ValidationError(f"Название не может содержать такое слово")
        elif Game.objects.filter(title=title).exists():
            raise ValidationError('Игра с таким названием уже существует в каталоге')
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')
        lowered_description = list(map(lambda word: word.lower(), description.split()))
        if any(element in lowered_description for element in FORBIDDEN_WORDS):
            raise ValidationError(f"Описание не может содержать такое слово")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError(f"Цена не может быть отрицательной")
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        extension = image.name.split('.')[-1]
        if image and image.size > settings.UPLOAD_FILE_MAX_SIZE:
            raise ValidationError(f"Размер изображения не должен превышать 5 МБ ")
        elif not extension or extension.lower() not in settings.WHITELISTED_IMAGE_TYPES.keys():
            raise ValidationError(f'Изображение может быть только в формате "png", "jpg", "jpeg"')
        return image
