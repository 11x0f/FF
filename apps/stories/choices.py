from django.db import models

class StoryStatusChoices(models.TextChoices):
    DRAFT = "draft", "Draft"
    PUBLISHED = "published", "Published"
    COMPLETED = "completed", "Completed"
    HIATUS = "hiatus", "Hiatus"

class ChapterStatusChoices(models.TextChoices):
    DRAFT = "draft", "Draft"
    COMPLETED = "completed", "Completed"
    PUBLISHED = "published", "Published"