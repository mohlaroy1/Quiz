from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Group(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    allowed_groups = models.ManyToManyField(Group)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)
    pass_score = models.FloatField(default=60)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def total_questions(self):
        return self.question_set.count()


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='question-images', blank=True, null=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='answer-images', blank=True, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Submission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.student.username} : {self.quiz.title}"

    @property
    def total_correct_answers(self):
        return self.selection_set.filter(correct=True).count()

    @property
    def total_incorrect_answers(self):
        return self.selection_set.filter(correct=False).count()

    @property
    def get_score(self):
        return self.total_correct_answers / self.quiz.total_questions * 100


class Selection(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.answer.question.text} : {self.answer.text}"