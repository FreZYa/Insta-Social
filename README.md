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

3. Install Python dependencies
```
pip install -r requirements.txt
```

4. Install Node.js dependencies
```
npm install
```

5. Build CSS
```
npm run build
```

6. Run migrations
```
python manage.py migrate
```

7. Start the development server
```
python manage.py runserver
```

## Project Structure
- `users/`: User management app
- `posts/`: Posts and content management
- `media/`: User uploaded content
- `socialproject/`: Main project settings 