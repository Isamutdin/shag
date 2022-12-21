from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):

    def _create_user(self, username=None, email=None, 
        phone=None, password=None, **extra_fields):

        if (not username) and (not email) and (not phone):
            raise ValueError('Должен быть установлен один из этих полей (username, email, phone)')

        if not username:
            username = phone if phone else email

        if phone:
            self.model(
                phone=phone,
                username=username,
                **extra_fields
            )

        else:
            email = self.normalize_email(email)

            self.model(
                email=email,
                username=username,
                **extra_fields
            )

        if extra_fields.get('is_superuser'):
            user = self.model(
                username=username,
                **extra_fields
            )


        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username=username, email=email, password=password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
            
        return self._create_user(
            username=username,
            password=password,
            **extra_fields
        )
