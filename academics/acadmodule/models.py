from django.db import models
from django.utils import timezone
from Fusion-master.FusionIIIT.applications.globals import ExtraInfo
# Create your models here.

class Constants:

    BRANCH = (
        ('CSE','Computer Science and Engineering'),
        ('ECE','Electronics and Communication Engineering'),
        ('ME','Mechanical Engineering'),
        ('Btech_ALL','Btech All'),
        ('Common','Common'),
        ('DES','Design'),
    )

    #To be corrected ,Add Professional and core courses list.

    PROGRAMME = (
        ('BTECH', 'BTech'),
        ('BDES', 'BDes'),
        ('MTech', 'MTech'),
        ('MDes', 'MDes'),
        ('PhD', 'PhD')
    )

    COURSE_TYPE = (
        ('Core', 'Professional Core'),
        ('Elective', 'Professional Elective'),
        ('Lab', 'Professional Lab'),
        ('Project','Professional Project'),
        ('ES', 'Engineering Science'),
        ('NS', 'Natural Science'),
        ('HS', 'Humanities'),
        ('DS', 'Design'),
        ('MN', 'Manufacturing'),
        ('MS', 'Management Science'),
    )


# class Student(models.Model):
#
#     name = models.CharField(max_length=256)
#     programme = models.CharField(max_length=100,choices=Constants.PROGRAMME)
#     branch = models.CharField(max_length=256,choices=Constants.BRANCH)
#     batch = models.IntegerField(default=int(timezone.now().year))
#     age = models.IntegerField()
#
#     def __str__(self):
#         return self.name

class Course(models.Model):
    course_name = models.CharField(max_length=256)
    course_details = models.TextField(max_length=2500)

class BatchSemester(models.Model):
    semester = models.IntegerField(default=0)
    total_number_of_courses = models.IntegerField(default=0)
    #Professional Courses
    professional_core_courses = models.IntegerField(default=0)
    professional_elective_courses = models.IntegerField(default=0)
    professional_project_courses = models.IntegerField(default=0)
    professional_lab_courses = models.IntegerField(default=0)
    #Core Courses
    Core_engineering_science_courses = models.IntegerField(default=0)
    Core_natural_science_courses = models.IntegerField(default=0)
    Core_humanities_courses = models.IntegerField(default=0)
    Core_design_courses = models.IntegerField(default=0)
    Core_manufacturing_courses = models.IntegerField(default=0)
    Core_management_science_courses = models.IntegerField(default=0)
    #PBI
    pbi = models.BooleanField(default=False)


class BtechCurriculum(models.Model):
    programme = models.CharField(max_length=30,choices=Constants.PROGRAMME)
    batch = models.IntegerField(default=int(timezone.now().year))
    #Professional Courses
    professional_core_credit = models.IntegerField(default=0)
    professional_elective_credit = models.IntegerField(default=0)
    professional_project_credit = models.IntegerField(default=0)
    professional_lab_credit = models.IntegerField(default=0)
    #Core Courses
    Core_engineering_science_credit = models.IntegerField(default=0)
    Core_natural_science_credit = models.IntegerField(default=0)
    Core_humanities_credit = models.IntegerField(default=0)
    Core_design_credit = models.IntegerField(default=0)
    Core_manufacturing_credit = models.IntegerField(default=0)
    Core_management_science_credit = models.IntegerField(default=0)
    #PBI
    pbi = models.IntegerField(default=0)
    #Optional Project
    pr =models.IntegerField(default=0)

    #Semesters
    sem1 = models.ForeignKey(BatchSemester,on_delete=models.CASCADE,related_name="Semester1")
    sem2 = models.ForeignKey(BatchSemester,on_delete=models.CASCADE,related_name="Semester2")
    sem3 = models.ForeignKey(BatchSemester,on_delete=models.CASCADE,related_name="Semester3")
    sem4 = models.ForeignKey(BatchSemester,on_delete=models.CASCADE,related_name="Semester4")
    sem5 = models.ForeignKey(BatchSemester,on_delete=models.CASCADE,related_name="Semester5")
    sem6 = models.ForeignKey(BatchSemester,on_delete=models.CASCADE,related_name="Semester6")
    sem7 = models.ForeignKey(BatchSemester,on_delete=models.CASCADE,related_name="Semester7")
    sem8 = models.ForeignKey(BatchSemester,on_delete=models.CASCADE,related_name="Semester8")

class Curriculum_Course(models.Model):
    semester = models.ForeignKey(BatchSemester,on_delete=models.CASCADE)
    course_id = models.CharField(max_length=20)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    course_type = models.CharField(max_length=200,choices=Constants.COURSE_TYPE)
    course_credits = models.IntegerField(default=0)
    course_lecture = models.IntegerField(default=0)
    course_tutorial = models.IntegerField(default=0)
    course_practical = models.IntegerField(default=0)
    course_discussion = models.IntegerField(default=0)

    class Meta():
        unique_together = ('semester','course_id')

    # head_instructor = models.CharField(max_length=150)

class Curriculum_Instructor(models.Model):
    course = models.ForeignKey(Curriculum_Course,on_delete=models.CASCADE)
    instructor = models.ForeignKey(ExtraInfo,on_delete=models.CASCADE)
    head_instructor = models.BooleanField(default=False)

    class Meta():
        unique_together = ('course','instructor')
















    ##sdns
