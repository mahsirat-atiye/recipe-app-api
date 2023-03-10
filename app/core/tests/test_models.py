"""
Test for models
"""
from decimal import Decimal
from core import models
from django.test import TestCase
from django.contrib.auth import get_user_model  # refernce to custome model


def create_user(email='user@example.com', password='testpass123'):
    """Create a return a new user."""

    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        email = 'test@example.com'
        password = 'testpass1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['test1@Example.com', 'test1@example.com'],
            ['Test2@example.com', 'Test2@example.com'],
            ['Test3@example.COM', 'Test3@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'pass123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email='', password='pass')

    def test_create_superuser(self):
        email = 'test@example.com'
        password = 'testpass1234'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password,
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_recipe(self):
        email = 'test@example.com'
        password = 'testpass1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title='sample recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='sample description',
        )
        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        """Test creating a tag is successful."""

        user = create_user()

        tag = models.Tag.objects.create(user=user, name='Tag1')
        self.assertEqual(str(tag), tag.name)


def test_create_ingredient(self):
    """Test creating an ingredient is successful."""
    user = create_user()
    ingredient = models.Ingredient.objects.create(
        user=user,
        name='Ingredient1'
    )
    self.assertEqual(str(ingredient), ingredient.name)
