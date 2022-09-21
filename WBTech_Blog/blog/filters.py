from django.forms import DateInput
from django_filters import FilterSet, DateFilter
from .models import Post


# создаём фильтр
class UserLovelyPostFilter(FilterSet):
    creation_date = DateFilter(
        field_name='creation_date',
        label='Опубликованы позже',
        lookup_expr='gt',  # должна быть позже или равна тому (greater than), что указал пользователь
        widget=DateInput(format='%d.%m.%Y', attrs={'type': 'date', 'class': 'inp'}))

    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    class Meta:
        model = Post
        fields = ('status', 'creation_date',)
