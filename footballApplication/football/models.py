from django.core.validators import MaxLengthValidator
from django.db import models
from footballApplication.football.validators import BadLanguageValidator


class Countries(models.Model):
    name = models.CharField(
        max_length=100
    )

    flag = models.ImageField(
        upload_to='flags'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'
        verbose_name = 'Country'


class Championship(models.Model):
    name = models.CharField(
        max_length=100
    )

    logo = models.ImageField(
        upload_to='logos'
    )

    country = models.ForeignKey(
        to=Countries,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='championships',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Championships'
        verbose_name = 'Championship'


class Teams(models.Model):
    name = models.CharField(
        max_length=100
    )

    points = models.IntegerField()

    position = models.IntegerField()

    emblem = models.FileField(
        upload_to='emblems'
    )

    titles = models.IntegerField()

    european_title = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    championship = models.ForeignKey(
        to=Championship,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='teams',
    )

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Teams'
        verbose_name = 'Team'


class Players(models.Model):
    name = models.CharField(
        max_length=100
    )

    image = models.ImageField(
        upload_to='players'
    )

    position = models.CharField(
        max_length=100
    )

    secondary_position = models.CharField(
        max_length=100
    )

    nationality = models.CharField(
        max_length=100
    )

    year = models.IntegerField()

    salary = models.IntegerField()

    team = models.ForeignKey(
        to=Teams,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='players',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Players'
        verbose_name = 'Player'


class Comment(models.Model):
    team = models.ForeignKey(
        to=Teams,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    author = models.CharField(
        max_length=30,
    )

    content = models.TextField(
        validators=[BadLanguageValidator(['fuck', 'shit'])]
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )




