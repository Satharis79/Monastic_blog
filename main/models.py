from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class CustomAccountManager(BaseUserManager):
    def create_user(self, user_name, password=None, **other_fields):
        monk = self.model(user_name=user_name, **other_fields)
        monk.set_password(password)
        monk.save(using=self._db)
        return monk

    def create_superuser(self, user_name, password=None, **other_fields):
        monk = self.create_user(user_name, password, **other_fields)
        monk.is_staff = True
        monk.is_superuser = True                                
        monk.save(using=self._db)
        return monk

class Monk(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField('Username', max_length=100, unique=True)
    first_name = models.CharField('First name', max_length=100, default='John')
    city_of_origin = models.CharField('City of origin', max_length=100, default='Doe')
    start_date = models.DateTimeField('Date of joining', default=timezone.now)
    userpic = models.ImageField('Userpic', upload_to='media/img', default='media/img/undefined_monk.jpg')
    
    SIR = 'Sir'
    MADAM = 'Madam'
    FATHER = 'Father'
    MOTHER = 'Mother'
    BROTHER = 'Brother'
    SISTER = 'Sister'
    MASTER = 'Master'
    MISTRESS = 'Mistress'
    BISHOP = 'Bishop'
        
    TITLE_CHOICES = [
    (SIR, 'Sir'),
    (MADAM, 'Madam'),
    (FATHER, 'Father'),
    (MOTHER, 'Mother'),
    (BROTHER, 'Brother'),
    (SISTER, 'Sister'),
    (MASTER, 'Master'),
    (MISTRESS, 'Mistress'),
    (BISHOP, 'Bishop'),
    ]

    title = models.CharField(
        'Title of address',
        max_length=30,
        choices=TITLE_CHOICES,
        default=BROTHER,
    )
    
    about = models.TextField('Your confession', max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_literate = models.BooleanField('Litteratus', default=False)
    is_ordained = models.BooleanField('Ordinatus', default=False)    

    objects = CustomAccountManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['first_name', 'city_of_origin']    

    def __str__(self):
        return self.user_name

    def full_address(self):
        return f'{self.title} {self.first_name} of {self.city_of_origin}'