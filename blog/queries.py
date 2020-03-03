from django.db.models import Prefetch

from .models import User, Category, Post
from .decorators import debugger_queries


# Truy vấn thông thường

@debugger_queries
def post_list():
    queryset = Post.objects.all()

    posts = []

    for post in queryset:
        posts.append({
            'id': post.id,
            'title': post.title,
        })

    return posts


# Truy vấn gây hit database vì không sử dụng select_related

@debugger_queries
def post_list_bad():
    queryset = Post.objects.all()

    posts = []

    for post in queryset:
        posts.append({
            'id': post.id,
            'title': post.title,
            'owner': post.owner.name,
        })

    return posts


# Thực hiện select_related với ForeignKey

@debugger_queries
def post_list_select_related_good():
    queryset = Post.objects.select_related("owner")

    posts = []

    for post in queryset:
        posts.append({
            'id': post.id,
            'title': post.title,
            'owner': post.owner.name,
        })

    return posts


# Truy vấn không sử dụng select_related gây hit database

@debugger_queries
def user_list_bad():
    queryset = User.objects.all()

    users = []

    for user in queryset:
        users.append({
            'id': user.id,
            'name': user.name,
            'address': user.profile.address,
        })

    return users


# Thực hiện select_related với OneToOneField 

@debugger_queries
def user_list_select_related_good():
    queryset = User.objects.select_related("profile")

    users = []

    for user in queryset:
        users.append({
            'id': user.id,
            'name': user.name,
            'address': user.profile.address,
        })

    return users


# Sử dụng nhiều tham số vào select_related

@debugger_queries
def post_list_select_related_2():
    queryset = Post.objects.select_related("owner", "owner__profile")

    posts = []

    for post in queryset:
        posts.append({
            'id': post.id,
            'title': post.title,
            'owner': post.owner.name,
            'address': post.owner.profile.address,
        })

    return posts


# Truy vấn gây hit database vì không sử dụng prefetch_related

@debugger_queries
def post_list_bad_2():
    queryset = Post.objects.all()

    posts = []

    for post in queryset:
        catgories = [category.name for category in post.categories.all()]
        posts.append({
            'id': post.id,
            'title': post.title,
            'catgories': catgories,
        })

    return posts


# Thực hiện prefetch_related với ManyToManyField

@debugger_queries
def post_list_prefetch_related_good():
    queryset = Post.objects.prefetch_related("categories")

    posts = []

    for post in queryset:
        catgories = [category.name for category in post.categories.all()]
        posts.append({
            'id': post.id,
            'title': post.title,
            'catgories': catgories,
        })

    return posts


# Thực hiện prefetch_related với ForeignKey đảo ngược

@debugger_queries
def post_list_prefetch_related_good_2():
    queryset = User.objects.prefetch_related('posts_created')

    users = []

    for user in queryset:
        posts = [post.title for post in user.posts_created.all()]

        users.append({
            'id': user.id,
            'name': user.name,
            'posts': posts,
        })

    return users


# Thực hiện prefetch_related vẫn gây hit database

@debugger_queries
def post_list_prefetch_related_bad():
    queryset = Post.objects.prefetch_related("categories")

    posts = []

    for post in queryset:
        catgories = [category.name for category in post.categories.filter(name__startswith="c")]
        posts.append({
            'id': post.id,
            'title': post.title,
            'catgories': catgories,
        })

    return posts


# Thực hiện prefetch_related cùng với Prefetch

@debugger_queries
def post_list_prefetch_related_good_3():
    queryset = Post.objects.prefetch_related(
            Prefetch("categories", queryset=Category.objects.filter(name__startswith="c"))
        )

    posts = []

    for post in queryset:
        catgories = [category.name for category in post.categories.all()]
        posts.append({
            'id': post.id,
            'title': post.title,
            'catgories': catgories,
        })

    return posts


# Thực hiện với cả select_related và prefetch_related

@debugger_queries
def post_list_select_prefetch_related():
    queryset = User.objects.prefetch_related('posts_created', 'posts_created__categories').select_related('profile')

    users = []

    for user in queryset:
        data = {'posts': [], 'categories': []}
        for post in user.posts_created.all():
            data['posts'].append(post.title)
            categories = [category.name for category in post.categories.all()]
            data['categories'].append(categories)

        users.append({
            'id': user.id,
            'name': user.name,
            'address': user.profile.address,
            'posts': data['posts'],
            'categories': data['categories'],
        })

    return users
