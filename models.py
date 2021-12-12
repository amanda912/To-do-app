from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    Date = models.DateTimeField(default="2014-09-12 12:00:32")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'

def changepassword(request):
    old_pass = request.POST['old_pass']
    new_pass = request.POST['new_pass']
    print(old_pass)
    print(new_pass)
    u = User.objects.get(email = request.user.email)
    print(u.password)
    u.set_password('new password')
  
    u.save()
    u = User.objects.get(email = request.user.email)
    print(u.password)
    