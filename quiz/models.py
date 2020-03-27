from django.db import models

# Create your models here.
from teacher.models import Teacher
from student.models import Student

class ClassInfo(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_code = models.CharField(max_length=8, primary_key=True)
    class_name = models.CharField(max_length=30)

class ClassEnrolled(models.Model):
    class_code = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)

    #Rows should not be same i.e a single student cannot be enrolled in same class twice
    class Meta:
        unique_together = ('class_code', 'student_id')


class QuizInfo(models.Model):
    quiz_id = models.CharField(max_length=100, primary_key=True)
    quiz_name = models.CharField(max_length=50)
    class_code = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)
    launch_time = models.DateTimeField('Date to Launch Quiz')




class QuizQuestion(models.Model):
    # Initializing choices of question type
    MCQ = "MCQ"
    Blanks = "Blanks"

    QuestionTypes = [(MCQ, "MCQ"),
                     (Blanks, "Fill blanks")]

    quiz_id = models.ForeignKey(QuizInfo, on_delete=models.CASCADE)
    question_type = models.CharField(choices=QuestionTypes, default=MCQ, max_length=15)
    question_id = models.IntegerField(primary_key=True, auto_created=True)
    question = models.CharField(max_length=200)

    def getQuizType(self):
        return self.question_type

class QuestionAnswer(models.Model):
    question_id = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    question_answer = models.CharField(max_length=100)

class QuestionOptions(models.Model):
    question_id = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    question_choice = models.CharField(max_length=100)





