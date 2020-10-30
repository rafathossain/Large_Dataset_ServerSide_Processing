from django.db import models


class DataSet(models.Model):
    text = models.TextField()
    random = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'dataset'
