from django.db import models

# Create your models here.
class Members(models.Model):
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=500)
    email=models.EmailField(max_length=250)



    def register(self):
        self.save()

    @staticmethod
    def get_member_by_email(email):
        try:
            return Members.objects.get(email=email)
        except:
            return False

    @staticmethod
    def get_member_by_uname(username):
        try:
            return Members.objects.get(username=username)
        except:
            return False

    def doExists(self):
        if Members.objects.filter(email=self.email):
            return True

        return False

    def validateEmail(self):
        email=self.email
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    def __str__(self):
        return self.username

