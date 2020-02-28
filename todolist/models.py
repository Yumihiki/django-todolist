from django.conf import settings
from django.db import models
from django.utils import timezone


class ToDoList(models.Model):

    class Meta:
        db_table = 'todolist'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='タイトル', max_length=10)
    content = models.TextField(verbose_name='内容', max_length=5000)
    created_date = models.DateField(verbose_name='作成日', default=timezone.now())
    updated_date = models.DateField(verbose_name='更新日', blank=True, null=True)

    THINKING = '考え中'
    WORKING = '作業中'
    FINISHED = '完了'
    STATUS = [
        (THINKING, 'Thinking'),
        (WORKING, 'Working'),
        (FINISHED, 'Finished'),
    ]
    status = models.CharField(
        verbose_name='ステータス',
        max_length=3,
        choices=STATUS,
        default=THINKING,
    )

    def update(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
