from django.utils import timezone
from haystack import indexes
from .models import Product
import datetime


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')
    price = indexes.CharField(model_attr='price')

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        # return self.get_model().objects.filter(date_upload__lte=datetime.datetime.now())
        return self.get_model().objects.filter(display=True)
