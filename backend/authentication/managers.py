from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, name, surname, password=None):
        user = self.model(
            email = self.normalize_email(email), #проверка email
            name=name,
            surname=surname,
        )
        
        user.set_password(password) #хэшируем пароль
        user.save() #сохраняем
        
        return user
    
    def create_superuser(self, email, name, surname, password):
        user = self.create_user(
            email = email,
            name=name,
            surname=surname,
            password=password,
        )
        
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        
        user.save()
        
        return user
    