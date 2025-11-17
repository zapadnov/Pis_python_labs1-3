from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    # название статьи, обычное текстовое поле с ограничением по длине
    title = models.CharField(max_length=200)

    # поле с автором: связываем статью с пользователем из встроенной модели User
    # при удалении пользователя его статьи тоже удаляются (CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # основное содержимое статьи, без ограничений по длине
    text = models.TextField()

    # дата, когда запись была создана; Django сам подставит текущую дату один раз
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        """
        Строка, которую будет показывать админка и shell.
        Возвращаю строку в формате: логин_автора: заголовок_статьи.
        """
        return "%s: %s" % (self.author.username, self.title)

    def get_excerpt(self):
        """
        Возвращает короткий фрагмент текста статьи.
        Если символов больше 140, берём только первые 140 и добавляем '...',
        иначе отдаём исходный текст полностью.
        """
        return self.text[:140] + "..." if len(self.text) > 140 else self.text
