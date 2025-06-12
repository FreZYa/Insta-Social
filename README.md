# Social Project

A Django-based social media application with TailwindCSS for styling.

## Setup Instructions

### Prerequisites
- Python 3.x
- Node.js and npm

### Installation

1. Clone the repository
```
git clone <repository-url>
cd socialproject
```

2. Create and activate a virtual environment
```
python -m venv env
source env/bin/activate  # On Windows, use: env\Scripts\activate
```

3. Set up environment variables
```
# Copy the example env file
cp env.example .env
# Edit .env with your own values
```

4. Install Python dependencies
```
pip install -r requirements.txt
```

5. Install Node.js dependencies
```
npm install
```

6. Create environment file
```
# Copy the example env file
cp env.example .env
# Edit .env with your own values
```

7. Build CSS (choose one)
```
# Build once
npm run build

# Watch for changes during development
npm run watch
```

8. Run migrations
```
python manage.py migrate
```

9. Create a superuser (optional)
```
python manage.py createsuperuser
```

10. Start the development server
```
python manage.py runserver
```

## Features
- 👤 User registration and authentication
- 📝 Create and share posts with images
- 💖 Like and comment on posts
- 🎨 Modern UI with TailwindCSS
- 📱 Responsive design
- 🔐 Password reset functionality
- 👥 User profiles with profile pictures

## Project Structure
- `users/`: User management app
- `posts/`: Posts and content management
- `media/`: User uploaded content
- `socialproject/`: Main project settings
- `static/`: Static files (CSS, JS, images)
- `templates/`: HTML templates

## Technologies Used
- **Backend**: Django 4.2.23
- **Frontend**: HTML, TailwindCSS 2.2.16
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Image Processing**: Pillow
- **Template Filters**: django-mathfilters

## Development
For development with live CSS reloading:
```bash
npm run watch
```

## Contributing
1. Fork the project
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request 