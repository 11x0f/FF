from django.db import models
from apps.stories.choices import StoryStatusChoices, ChapterStatusChoices

class Genre(models.Model):
    name = models.CharField(max_length=25, unique=True)
    slug = models.CharField(max_length=25, unique=True)
    class Meta:
        db_table='genres'

    def __str__(self):
        return f"{self.name}"

class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True)
    slug = models.CharField(max_length=25, unique=True)

    class Meta:
        db_table='tags'

    def __str__(self):
        return f"{self.name}"

class Story(models.Model):
    author = models.ForeignKey("users.User", on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    synopsis = models.TextField()
    slug = models.CharField(max_length=300, blank=True)
    cover_image = models.ImageField(upload_to="stories/images/", null=True, blank=True)
    status = models.CharField(
        max_length=20, 
        choices=StoryStatusChoices.choices, 
        default=StoryStatusChoices.DRAFT
    )
    
    genre = models.ManyToManyField(Genre, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='stories'

    def __str__(self):
        return f"{self.title}"

class Chapter(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    content = models.TextField()
    status = models.CharField(
        max_length=20, 
        choices=ChapterStatusChoices.choices,
        default=ChapterStatusChoices.DRAFT
    )
  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='chapters'
        unique_together = [['story', 'order']]

    def __str__(self):
        return f"{self.story} - {self.title}"

