## 1) Создать двух пользователей (с помощью метода User.objects.create_user('username')).
from django.contrib.auth.models import User

user1 = User.objects.create_user(username='user1', password='1236547')
user1.save()



user2 = User.objects.create_user(username='user2', password='454857')
user2.save()

## 2) Создать два объекта модели Author, связанные с пользователями.

from django.contrib.auth.models import User
from News.models import Author

user1, created1 = User.objects.get_or_create(username='user1')
author1, created_author1 = Author.objects.get_or_create(author=user1)

user2, created2 = User.objects.get_or_create(username='user2')
author2, created_author2 = Author.objects.get_or_create(author=user2)

## 3) Добавить 4 категории в модель Category.

from News.models import Category
category = Category.objects.create(name='Политика')
category = Category.objects.create(name='Кино')
category = Category.objects.create(name='Финансы')
category = Category.objects.create(name='Столица')

## 4) Добавить 2 статьи и 1 новость.

from News.models import Author, Category, Post, PostCategory

#### 1)
article = Post.objects.create(
    author=author1,
    article_type='article',
    title='***',
    text='''***''',
)

category_obj = Category.objects.get(name='Политика')

post_category = PostCategory.objects.create(category=category_obj, post=article1)


#### 2)
article2 = Post.objects.create(
    author=author1,
    article_type='article',
    title='***',
    text='''***''',
)

category_obj = Category.objects.get(name='Кино')

post_category = PostCategory.objects.create(category=category_obj, post=article2)

#### 3)
news1 = Post.objects.create(
    author=author1,
    article_type='news',
    title='***',
    text='''***''',
)

category_obj2 = Category.objects.get(name='Политика')

post_category = PostCategory.objects.create(category=category_obj2, post=news1)


## 5) Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
existing_article = Post.objects.get(id=1)
category1 = Category.objects.get(name='Политика')
category2 = Category.objects.get(name='Кино')

## 6) Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
from News.models import Comment, Post
from django.contrib.auth.models import User

# Получить статью, к которой нужно добавить комментарий
existing_article = Post.objects.get(id=1)

# Получить пользователя, который добавляет комментарий
comment_author = User.objects.get(username='user1')

# Создать новый комментарий
new_comment = Comment.objects.create(
    post=existing_article,
    author=comment_author,
    text='КОмментарий!'
)

## 7) Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.

from News.models import Post, Comment
post_ = Post.objects.get(id=1)
post_.like()  # post_.dislike()

comment = Comment.objects.get(id=1)
comment.like()

## 8) Обновить рейтинги пользователей.
from News.models import Author

authors = Author.objects.all()

for author in authors:
    author.update_rating()


## 9) Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).

from News.models import Author

best_author = Author.objects.order_by('-rating').first()
if best_author:
    username = best_author.author.username
    rating = best_author.rating
    print(f"Username: {username}, Rating: {rating}")
else:
    print("No authors found.")


## 10) Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.

from News.models import Post

best_post = Post.objects.order_by('-rating').first()

if best_post:
    creation_date = best_post.time_post
    author_username = best_post.author.author.username
    author_rating = best_post.author.rating
    post_title = best_post.title
    post_preview = best_post.preview()

    print(f"Date: {creation_date}, Username: {author_username}, Rating: {author_rating}")
    print(f"Title: {post_title}, Preview: {post_preview}")
else:
    print("No posts found.")


## 11) Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.

from News.models import Comment

comments = Comment.objects.filter(post__id=1)

for comment in comments:
    print(f"Дата: {comment.time_comment}")
    print(f"Пользователь: {comment.author.username}")
    print(f"Рейтинг: {comment.rating}")
    print(f"Текст комментария: {comment.text}\n")