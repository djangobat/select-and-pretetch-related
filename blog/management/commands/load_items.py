import random

from django.core.management.base import BaseCommand

from blog.models import User, Profile, Category, Post


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-u', '--user', type=int, default=50, help='')
        parser.add_argument('-c', '--category', type=int, default=20, help='')
        parser.add_argument('-p', '--post', type=int, default=10, help='')


    def handle(self, *args, **kwargs):

        num_users = kwargs['user']
        num_categories = kwargs['category']
        num_posts = kwargs['post']

        self.stdout.write("Cleaning database...")

        User.objects.all().delete()
        Category.objects.all().delete()
        Post.objects.all().delete()

        # Create users
        self.stdout.write(self.style.HTTP_NOT_MODIFIED(f"Creating { num_users } users..."))

        users = [User(name=f'User-{ index }') for index in range(num_users)]
        User.objects.bulk_create(users)

        # Create profiles
        self.stdout.write(self.style.HTTP_NOT_MODIFIED(f"Creating { num_users } profiles..."))

        profiles = [Profile(address=f'Address-{ user.name }', user=user) for user in User.objects.all()]
        Profile.objects.bulk_create(profiles)

        # Create categories
        self.stdout.write(self.style.HTTP_NOT_MODIFIED(f"Creating { num_categories } categories..."))
        categories = [Category(name=f'Category-{ index }') for index in range(num_categories)]
        Category.objects.bulk_create(categories)

        # Create posts
        self.stdout.write(self.style.HTTP_NOT_MODIFIED(f"Creating { num_posts*num_users } posts..."))

        for user in User.objects.all():
            for i in range(num_posts):
                new_post = Post(title=f"Post-{ i + 1 }", owner=user)
                new_post.save()
                new_post.categories.add(Category.objects.first())

        self.stdout.write(
            self.style.SUCCESS(f"SUCCESS: { num_users } users, { num_users } profiles, { num_categories } categories, { num_posts*num_users } posts")
        )
