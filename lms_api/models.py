from django.db import models


class TaskType(models.Model):
    type = models.CharField(max_length=30)

    class Meta:
        db_table = "TaskType"


class Task(models.Model):
    title = models.CharField(max_length=50)
    max_points = models.FloatField()
    text = models.TextField()

    course = models.ForeignKey('lms_api.Course', null=True, on_delete=models.SET_NULL)
    type = models.ForeignKey('lms_api.TaskType', on_delete=models.RESTRICT)
    files = models.ManyToManyField('lms_api.File', db_table='FileForTask')

    class Meta:
        db_table = "Task"


class Assignment(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    assigner = models.ForeignKey('lms_api.Person', null=True, on_delete=models.SET_NULL)
    task = models.ForeignKey('lms_api.Task', null=True, on_delete=models.SET_NULL)
    role = models.ForeignKey('lms_api.Role', null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "Assignment"


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

    type = models.ForeignKey('lms_api.PersonType', on_delete=models.RESTRICT)
    courses = models.ManyToManyField('lms_api.Course', through='Role')
    tasks = models.ManyToManyField('lms_api.Task', through='Assignment') # здесь сомнения, как реализовать правльно связь м2м с tasks через промежуточные таблицы Assignment и Result. по итогу убрал связь м2м с Result
    # results = models.ManyToManyField('lms_api.Task', through='Result') # здесь сомнения, как реализовать правльно связь м2м с tasks через промежуточные таблицы Assignment и Result

    class Meta:
        db_table = "Person"


class Course(models.Model):
    name = models.CharField(max_length=100)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    owner = models.ForeignKey('lms_api.Person', null=True, on_delete=models.SET_NULL)
    files = models.ManyToManyField('lms_api.File', db_table='FileForCourse')

    class Meta:
        db_table = "Course"



class RoleType(models.Model):
    type = models.CharField(max_length=30)

    class Meta:
        db_table = "RoleType"


class Role(models.Model):
    person = models.ForeignKey('lms_api.Person', null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey('lms_api.Course', null=True, on_delete=models.SET_NULL)
    type = models.ForeignKey('lms_api.RoleType', on_delete=models.RESTRICT)

    class Meta:
        db_table = "Role"


class Result(models.Model):
    submit_date = models.DateTimeField()
    points = models.FloatField()

    person = models.ForeignKey('lms_api.Person', null=True, on_delete=models.SET_NULL)
    task = models.ForeignKey('lms_api.Task', null=True, on_delete=models.SET_NULL)
    files = models.ManyToManyField('lms_api.File', db_table='FileForResult')

    class Meta:
        db_table = "Result"


class File(models.Model):
    path = models.CharField(max_length=100)
    date = models.DateTimeField()

    owner = models.ForeignKey('lms_api.Person', null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "File"


class Announcement(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.TextField()

    sender = models.ForeignKey('lms_api.Person', null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey('lms_api.Course', null=True, on_delete=models.SET_NULL) # здесь в явном виде не задавал связь м2м (наверное, так норм)
    files = models.ManyToManyField('lms_api.File', db_table='FileForAnnouncement')

    class Meta:
        db_table = "Announcement"
