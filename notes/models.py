from django.db import models
# Import the built-in User model
from django.contrib.auth.models import User

# Create your models here.



class Note(models.Model):
    """
    Model representing a sticky note.
    """
    # Field for the note's title (e.g., "Grocery List")
    title = models.CharField(max_length=1000)
    # Field for the main content (e.g., "Milk, Eggs, Bread")
    content = models.TextField()
    # Automatically set the time when the note is created
    created_at = models.DateTimeField(auto_now_add=True)
    # Link the note to a specific user
    # (Optional: null=True allows notes without owners)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )


    def __str__(self):
        """
        String representation of the Note object.
        Displays the title in the Admin panel.
        """
        return self.title

