from django.db import models

class Conversation(models.Model):
    user_1 = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True,  related_name="conversations_as_user1")
    user_2 = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True,  related_name="conversations_as_user2")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "conversations"
        unique_together = [["user_1", "user_2"]]

    def __str__(self):
        return f"{self.user_1} - {self.user_2}"

class Message(models.Model):
    conversation =  models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "messages"

    def __str__(self):
        return f"{self.message}"