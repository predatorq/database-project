from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.CharField(primary_key=True, max_length=8)
    book_name = models.CharField(max_length=50)
    book_isbn = models.CharField(max_length=17)
    book_author = models.CharField(max_length=10)
    book_publisher = models.CharField(max_length=50)
    book_price = models.DecimalField(max_digits=19, decimal_places=4)
    interview_times = models.SmallIntegerField()

    class Meta:
        db_table = 'book'


class Reader(models.Model):
    reader_id = models.CharField(primary_key=True, max_length=8)
    reader_name = models.CharField(max_length=50)
    reader_sex = models.CharField(max_length=2)
    reader_department = models.CharField(max_length=60)

    class Meta:
        db_table = 'reader'


class Record(models.Model):
    reader = models.ForeignKey(Reader, models.DO_NOTHING)
    book = models.OneToOneField(Book, models.DO_NOTHING, primary_key=True)
    borrow_date = models.DateField()
    return_date = models.DateField()
    notes = models.CharField(max_length=50)

    class Meta:
        db_table = 'record'
        unique_together = (('book', 'reader'),)