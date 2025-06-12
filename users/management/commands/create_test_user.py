from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import Profile

class Command(BaseCommand):
    help = 'Create a test user for debugging login issues'
    
    def handle(self, *args, **options):
        # Delete existing test user if exists
        User.objects.filter(username='testuser').delete()
        
        # Create new test user
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
        
        # Create profile for the user
        Profile.objects.create(user=user)
        
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ Test user created successfully!\n'
                f'Username: testuser\n'
                f'Password: testpass123\n'
                f'Email: test@example.com'
            )
        ) 