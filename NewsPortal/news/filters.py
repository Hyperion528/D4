from django.db.models import fields
from .models import New
from django_filters import CharFilter, FilterSet, RangeFilter, DateFromToRangeFilter


class F(FilterSet):
    date_pub = DateFromToRangeFilter()


    class Meta:
        model = New
        fields ='date_pub'
        fields ={'author':['icontains']}