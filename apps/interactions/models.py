from django.db import models

class StoryLike(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    story = models.ForeignKey("stories.Story", on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'story_likes'
        unique_together = [[ "user", "story"]]

class ChapterLike(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    chapter = models.ForeignKey("stories.Chapter", on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chapter_likes'
        unique_together = [[ "user", "chapter"]]


class Bookmark(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    story = models.ForeignKey("stories.Story", on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)   

    class Meta:
        db_table = 'bookmarks'
        unique_together = [[ "user", "story"]]

class Follow(models.Model):
    # who is doing the follow
    follower = models.ForeignKey("users.User", on_delete = models.CASCADE, related_name="following_set")
    # who is being followed
    following = models.ForeignKey("users.User", on_delete = models.CASCADE, related_name="follower_set")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "follows"
        unique_together = [["follower", "following"]]

class Comment(models.Model):
    chapter = models.ForeignKey("stories.Chapter", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comments"

    def __str__(self):
        return f"{self.comment}"


