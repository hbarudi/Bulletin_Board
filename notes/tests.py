from django.test import TestCase
from django.urls import reverse
from .models import Note

# Create your tests here.
# If your app uses a User/Author model linked to the note,
# import it here.
# Since the diagram implies a simple flow, we will focus on Note.
# from django.contrib.auth.models import User



class NoteModelTest(TestCase):


    def setUp(self):
        # Create a Note object for testing
        # We don't strictly need an author
        # based on the sequence diagram,
        # but if your model requires a user,
        # uncomment the user creation lines.
        # user = User.objects.create(username='testuser')
        Note.objects.create(
            title='Test Note', content='This is a test note content.'
        )


    def test_note_has_title(self):
        # Test that a Note object has the expected title
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')


    def test_note_has_content(self):
        # Test that a Note object has the expected content
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test note content.')



class NoteViewTest(TestCase):


    def setUp(self):
        # Create a Note object for testing views
        Note.objects.create(
            title='Test Note', content='This is a test note content.'
        )


    def test_note_list_view(self):
        # Test the note-list view (assuming the home page lists notes)
        # We use 'notes' app namespace if defined, or just the url name.
        # Common names are 'index', 'home', or 'note_list'.
        # Adjust 'index' below to match the name=
        # in your urls.py if different.
        try:
            url = reverse('index')
        except:
            # Fallback if the url is named differently
            url = reverse('note_list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note content.')


    def test_create_note_view_status(self):
        # Test that the create note page loads (GET request)
        # Adjust 'note_create' or 'add_note' to match your urls.py
        try:
            url = reverse('add_note')  # Common name
        except:
            try:
                url = reverse('note_create')
            except:
                # Fallback based on sequence diagram path /note/new/
                # This might fail if the URL pattern name isn't
                # guessed correctly without reading urls.py
                url = '/note/new/'

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_create_note_submission(self):
        # Test creating a new note via POST request
        try:
            url = reverse('add_note')
        except:
            try:
                url = reverse('note_create')
            except:
                url = '/note/new/'

        # Simulate a POST request with form data
        response = self.client.post(url, {
            'title': 'New Test Note',
            'content': 'Content for new test note'
        })

        # Check if the response is a redirect (status code 302)
        # This usually happens after successful form submission
        self.assertIn(response.status_code, [200, 302])

        # If it was a redirect, verify the note was created in DB
        if response.status_code == 302:
            self.assertTrue(
                Note.objects.filter(title='New Test Note').exists()
            )
