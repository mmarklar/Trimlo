from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_accessed = models.DateTimeField(auto_now=True)

    # This method forces it to be saved every time it is accessed.
    # This, combined with the date_accessed field being set to auto_now
    # allows us to sort the boards by when they were last accessed
    @classmethod
    def from_db(cls, db, field_names, values):
        obj = super().from_db(db, field_names, values)
        obj.save()
        return obj

class Column(models.Model):
    title = models.CharField(max_length=255)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

class Card(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    column = models.ForeignKey(Column, on_delete=models.CASCADE)

class ChecklistItem(models.Model):
    text = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    order = models.PositiveIntegerField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    class Meta:
        ordering = ['order']
