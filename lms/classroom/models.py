from django.db import models
from django.conf import settings
# Create your models here.


class Module(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()
    class_file = models.FileField()

    def __str__(self):
        return self.name



#content of the course refers to modules
class Course(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=6, unique=True, primary_key=True)
    instructors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='instructors')
    syllabus = models.TextField()
    modules = models.ManyToManyField(Module)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='students')
    teaching_assistants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='teaching_assistant', blank=True)


    def __str__(self):
        return '{0}'.format(self.code)

class Grade(models.Model):
    GRADE_CHOICES = (
        ('A', 'A(80-100)'),
        ('B', 'B(70-79)'),
        ('C', 'C(60-69)'),
        ('D', 'D(50-59)'),
        ('E', 'E(40-49)'),
        ('F', 'F(30-39)'),
    )
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)




class Comments(models.Model):
    created = models.DateTimeField(auto_now=True)
    body = models.TextField()
    author = models.OneToOneField(settings.AUTH_USER_MODEL)


# class Assignment(models.Model):
#     created = models.DateTimeField(auto_now=True)
#     content = models.ManyToManyField(Content)
#     comments = models.OneToOneField(Comments, on_delete=models.CASCADE)
#     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     course = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


#used to handle both quiz and assignments
class Quiz(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quiz')
    comments = models.OneToOneField(Comments, on_delete=models.CASCADE, blank=True, null=True)
    date_of_submission = models.DateTimeField()
    is_assignment = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)
    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text
    

class Discussion(models.Model):
    title = models.CharField(max_length=30)
    comments = models.OneToOneField(Comments, on_delete=models.CASCADE)
    created_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title