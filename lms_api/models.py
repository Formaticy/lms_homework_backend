from django.db import models


class File(models.Model):
    path = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey("lms_api.Person", null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "File"


class PersonType(models.Model):
    type = models.CharField(max_length=20)

    class Meta:
        db_table = "PersonType"


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    mail = models.EmailField()

    type = models.ForeignKey("lms_api.PersonType", on_delete=models.RESTRICT)
    courses = models.ManyToManyField("lms_api.Course", through="RoleOnCourse")

    class Meta:
        db_table = "Person"


class RoleOnCourseType(models.Model):
    type = models.CharField(max_length=30)

    class Meta:
        db_table = "RoleOnCourseType"


class RoleOnCourse(models.Model):
    type = models.ForeignKey("lms_api.RoleOnCourseType", on_delete=models.RESTRICT)
    person = models.ForeignKey("lms_api.Person", null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey("lms_api.Course", null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "RoleOnCourse"


class Course(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    owner = models.ForeignKey("lms_api.Person", null=True, on_delete=models.SET_NULL)
    files = models.ManyToManyField("lms_api.File", db_table="FileForCourse")

    class Meta:
        db_table = "Course"


class TaskType(models.Model):
    type = models.CharField(max_length=30)

    class Meta:
        db_table = "TaskType"


class Task(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()

    type = models.ForeignKey("lms_api.TaskType", on_delete=models.RESTRICT)
    files = models.ManyToManyField("lms_api.File", db_table="FileForTask")

    class Meta:
        db_table = "Task"


class Assignment(models.Model):
    max_points = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    assigner = models.ForeignKey("lms_api.Person", null=True, on_delete=models.SET_NULL)
    task = models.ForeignKey("lms_api.Task", null=True, on_delete=models.SET_NULL)
    role_on_course_type = models.ForeignKey("lms_api.RoleOnCourseType", null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey("lms_api.Course", null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "Assignment"


class Result(models.Model):
    submit_date = models.DateTimeField()
    points = models.FloatField()

    person = models.ForeignKey("lms_api.Person", null=True, on_delete=models.SET_NULL)
    assignment = models.ForeignKey("lms_api.Assignment", null=True, on_delete=models.SET_NULL)
    files = models.ManyToManyField("lms_api.File", db_table="FileForResult")

    class Meta:
        db_table = "Result"


class Announcement(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    text = models.TextField()

    sender = models.ForeignKey("lms_api.Person", null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey("lms_api.Course", null=True, on_delete=models.SET_NULL)
    files = models.ManyToManyField("lms_api.File", db_table="FileForAnnouncement")

    class Meta:
        db_table = "Announcement"