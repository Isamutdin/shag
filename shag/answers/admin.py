from django.contrib import admin
from .models import *


# Register your models here.


admin.site.register(InputAnswer)
admin.site.register(ChoiceAnswer)
admin.site.register(FileAnswer)
admin.site.register(TextAnswer)