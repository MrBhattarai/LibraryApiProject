from django.test import TestCase
from django.urls import reverse

from .models import Book

# Create your tests here.


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="1984",
            subtitle="The book about the future",
            author="George Orwell",
            isbn="9780141036144",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "1984")
        self.assertEqual(self.book.subtitle, "The book about the future")
        self.assertEqual(self.book.author, "George Orwell")
        self.assertEqual(self.book.isbn, "9780141036144")

    def test_book_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The book about the future")
        self.assertTemplateUsed(response, "book_list.html")
