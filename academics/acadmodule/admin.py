from django.contrib import admin
from .models import BtechCurriculum,Course,BatchSemester
# Register your models here.

admin.site.register(BtechCurriculum)
admin.site.register(BatchSemester)
admin.site.register(Course)
