from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django_ckeditor_5.fields import CKEditor5Field


class ClubModel(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug', null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name='Название', unique=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               verbose_name='Автор', related_name='author_club_model')
    desc = models.TextField(verbose_name='Краткое описание')
    tags = TaggableManager()
    text = CKEditor5Field('Полное описание', config_name='extends', null=True, blank=True)
    required_team = models.TextField(verbose_name='Требуются в команду', null=True, blank=True)
    request_team = models.ManyToManyField(get_user_model(), verbose_name='Заявки на участие',
                                          blank=True, related_name='request_team_club_model')

    valid_team = models.ManyToManyField(get_user_model(), verbose_name="Участники клуба",
                                        blank=True, related_name='valid_team_club_model')

    class Meta:
        verbose_name_plural = 'Clubs'

    def get_absolute_url(self):
        return reverse('collab:detail_club', kwargs={'slug': self.slug})

    def parts_with_tags(self):
        # for tag in club.tags.all.prefetch_related
        return self.tags.select_related('tag')

    def __str__(self):
        return self.name
