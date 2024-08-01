from .models import *


# Возвращает автора клуба по slug
def get_author_by_slug(slug):
    return ClubModel.objects.get(slug=slug).author


def get_club_by_slug(slug):
    return ClubModel.objects.get(slug=slug)
