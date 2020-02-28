# 未着手

from django import forms
from .models import ToDoList


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList

        # 入力項目から作成日時、更新日時を除外
        exclude = (
            'created_date',
            'updated_date',
        )
