# Mike's Blog - Vue3 + Django

A modern, full-stack blog application built with Vue3 frontend and Django backend, featuring automated deployment with GitHub Actions.

![Blog Screenshot](https://github.com/user-attachments/assets/c5f26e1d-4c00-45f9-a661-1c7e963b2e7f)

## 🚀 Features

- **Modern Tech Stack**: Vue3 + Django REST Framework
- **Responsive Design**: Mobile-first CSS with beautiful UI
- **RESTful API**: Clean API design with Django REST Framework
- **Admin Interface**: Built-in Django admin for content management
- **Automated Deployment**: GitHub Actions CI/CD pipeline
- **Containerized**: Docker support for easy deployment
- **Content Management**: Categories, tags, and rich blog posts
- **SEO Friendly**: Clean URLs and meta data support

## 🛠 Tech Stack

### Backend
- **Django 5.2.6** - Python web framework
- **Django REST Framework** - API development
- **SQLite/PostgreSQL** - Database (SQLite for dev, PostgreSQL for production)
- **Django CORS Headers** - Cross-origin resource sharing
- **Pillow** - Image handling

### Frontend
- **Vue 3** - Progressive JavaScript framework
- **Vite** - Fast build tool and dev server
- **Axios** - HTTP client for API calls
- **Modern CSS** - Responsive grid layouts and gradients

### DevOps
- **GitHub Actions** - CI/CD automation
- **Docker** - Containerization
- **Docker Compose** - Local development orchestration

## 📁 Project Structure

```
blog/
├── backend/                 # Django backend
│   ├── blog_project/       # Django project settings
│   ├── blog/               # Blog app
│   │   ├── models.py       # Data models (Post, Category, Tag, Comment)
│   │   ├── serializers.py  # API serializers
│   │   ├── views.py        # API views
│   │   └── admin.py        # Admin interface
│   └── manage.py
├── frontend/               # Vue3 frontend
│   ├── src/
│   │   ├── components/     # Vue components
│   │   ├── services/       # API service layer
│   │   └── App.vue         # Main app component
│   ├── package.json
│   └── vite.config.js
├── .github/workflows/      # GitHub Actions
├── docker-compose.yml      # Development orchestration
├── Dockerfile             # Production container
└── requirements.txt       # Python dependencies
```

## 🏃‍♂️ Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- npm or yarn

### 1. Clone the repository
```bash
git clone https://github.com/mike1936/blog.git
cd blog
```

### 2. Backend Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Setup Django
cd backend
python manage.py migrate
python manage.py createsuperuser
python manage.py create_sample_data  # Optional: create sample blog posts
python manage.py runserver 8000
```

### 3. Frontend Setup
```bash
# Install Node dependencies
cd frontend
npm install

# Start development server
npm run dev
```

### 4. Access the Application
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000/api
- **Django Admin**: http://localhost:8000/admin

## 🐳 Docker Development

Run the entire stack with Docker Compose:

```bash
docker-compose up --build
```

This will start:
- Django backend on port 8000
- Vue frontend on port 5173
- PostgreSQL database on port 5432

## 🚀 Deployment

### GitHub Actions

The project includes a GitHub Actions workflow that:
1. **Tests** both frontend and backend
2. **Builds** production assets
3. **Deploys** to your target environment

Configure these secrets in your GitHub repository:
- `DJANGO_SECRET_KEY` - Django secret key for production
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts
- `DATABASE_URL` - Production database URL

### Manual Deployment

1. **Build the Docker image**:
```bash
docker build -t blog-app .
```

2. **Run in production**:
```bash
docker run -d \
  -p 80:8000 \
  -e SECRET_KEY="your-secret-key" \
  -e DEBUG=False \
  -e ALLOWED_HOSTS="yourdomain.com" \
  blog-app
```

### Deployment Platforms

This app can be deployed to:
- **Heroku** - Platform as a Service
- **DigitalOcean App Platform** - Managed containers
- **AWS Elastic Beanstalk** - AWS managed platform
- **Google Cloud Run** - Serverless containers
- **Your own VPS** - With Docker

## 📝 API Endpoints

- `GET /api/posts/` - List all published posts
- `GET /api/posts/{slug}/` - Get specific post
- `GET /api/categories/` - List all categories
- `GET /api/tags/` - List all tags
- `GET /api/stats/` - Get blog statistics
- `POST /api/posts/{slug}/comments/` - Create comment

## 🎨 Customization

### Adding New Content
1. Use the Django admin interface at `/admin`
2. Create categories, tags, and posts
3. The Vue frontend will automatically display new content

### Styling
- Edit Vue components in `frontend/src/components/`
- Modify global styles in `frontend/src/App.vue`
- Add new CSS classes as needed

### API Extensions
- Add new models in `backend/blog/models.py`
- Create serializers in `backend/blog/serializers.py`
- Add views in `backend/blog/views.py`
- Update URLs in `backend/blog/urls.py`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django team for the amazing web framework
- Vue.js team for the reactive frontend framework
- Open source community for all the tools and libraries
