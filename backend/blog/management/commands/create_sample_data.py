from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Category, Tag, Post


class Command(BaseCommand):
    help = 'Create sample blog data'

    def handle(self, *args, **options):
        # Create categories
        tech_category, _ = Category.objects.get_or_create(
            name='Technology',
            slug='technology',
            defaults={'description': 'Posts about technology and programming'}
        )
        
        lifestyle_category, _ = Category.objects.get_or_create(
            name='Lifestyle',
            slug='lifestyle',
            defaults={'description': 'Posts about lifestyle and personal experiences'}
        )

        # Create tags
        django_tag, _ = Tag.objects.get_or_create(name='Django', slug='django')
        vue_tag, _ = Tag.objects.get_or_create(name='Vue.js', slug='vuejs')
        python_tag, _ = Tag.objects.get_or_create(name='Python', slug='python')
        javascript_tag, _ = Tag.objects.get_or_create(name='JavaScript', slug='javascript')
        web_tag, _ = Tag.objects.get_or_create(name='Web Development', slug='web-development')

        # Get or create admin user
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()

        # Create sample posts
        post1, created = Post.objects.get_or_create(
            title='Welcome to Mike\'s Blog',
            slug='welcome-to-mikes-blog',
            defaults={
                'author': admin_user,
                'content': '''
# Welcome to My Blog!

This is the first post on my new Vue3 + Django blog! I'm excited to share my thoughts and experiences about web development, technology, and life.

## What You Can Expect

- **Technology Posts**: Deep dives into Django, Vue.js, and modern web development
- **Tutorials**: Step-by-step guides for building awesome applications
- **Personal Thoughts**: My experiences in the tech industry

## Built With Modern Tech

This blog is built using:
- **Backend**: Django + Django REST Framework
- **Frontend**: Vue 3 + Vite
- **Deployment**: GitHub Actions + Docker
- **Database**: PostgreSQL (production) / SQLite (development)

Stay tuned for more content!
                '''.strip(),
                'excerpt': 'Welcome to my new Vue3 + Django blog! Learn about what you can expect and the technology behind this site.',
                'category': tech_category,
                'status': Post.PUBLISHED
            }
        )
        if created:
            post1.tags.set([django_tag, vue_tag, web_tag])

        post2, created = Post.objects.get_or_create(
            title='Building a Modern Blog with Vue3 and Django',
            slug='building-modern-blog-vue3-django',
            defaults={
                'author': admin_user,
                'content': '''
# Building a Modern Blog with Vue3 and Django

In this post, I'll walk you through the process of building a modern, full-stack blog application using Vue3 for the frontend and Django for the backend.

## Why This Tech Stack?

### Django - The Backend Powerhouse
- **Rapid Development**: Django's "batteries included" philosophy
- **REST API**: Django REST Framework for clean API design
- **Admin Interface**: Built-in admin panel for content management
- **Security**: Built-in protection against common vulnerabilities

### Vue3 - The Modern Frontend
- **Reactive**: Composition API for better code organization
- **Performance**: Optimized rendering and bundle sizes
- **Developer Experience**: Great tooling with Vite
- **Community**: Large ecosystem of components and libraries

## Key Features Implemented

1. **RESTful API** with Django REST Framework
2. **Responsive Design** with modern CSS
3. **Component-based Architecture** with Vue3
4. **Automated Deployment** with GitHub Actions
5. **Containerization** with Docker

## Getting Started

To run this blog locally:

```bash
# Backend
cd backend
python manage.py runserver

# Frontend  
cd frontend
npm run dev
```

## What's Next?

- Add user authentication
- Implement commenting system
- Add search functionality
- Create admin dashboard in Vue

Happy coding! 🚀
                '''.strip(),
                'excerpt': 'A comprehensive guide to building a modern blog with Vue3 and Django, including deployment with GitHub Actions.',
                'category': tech_category,
                'status': Post.PUBLISHED
            }
        )
        if created:
            post2.tags.set([django_tag, vue_tag, python_tag, javascript_tag, web_tag])

        self.stdout.write(
            self.style.SUCCESS('Successfully created sample blog data!')
        )