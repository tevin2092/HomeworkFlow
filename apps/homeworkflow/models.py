from django.db import models

absent_types = {
    "late":"late",
    "absent":"absent",
}

behaviour = {
    "excellent":"excellent",
    "good":"good",
    "average":"average",
    "poor":"poor"
}

class Attendance(models.Model):
    date = models.DateField()
    student_id = models.ForeignKey('userprofile.Student', on_delete=models.CASCADE)
    type = models.CharField(choices=absent_types, max_length=10)
    lesson_id = models.ForeignKey('classroom.Lesson', on_delete=models.CASCADE)

class Homework(models.Model):
    lesson_id = models.ForeignKey('classroom.Lesson', on_delete=models.CASCADE)
    due_date = models.DateField()
    description = models.TextField()
    # Constraint: due date in future
    # class Meta:
    #     models.CheckConstraint(
    #             name='%(app_label)s_%(class)s_due_date_in_future_check',
    #             check=models.Q(due_date__gt=models.F('current_date'))
    #         ),


class Homework_Uncompleted(models.Model):
    homework_id = models.ForeignKey('homeworkflow.Homework', on_delete=models.CASCADE)
    student_id = models.ForeignKey('userprofile.Student', on_delete=models.CASCADE)

class Weekly_Feedback(models.Model):
    student_id = models.ForeignKey('userprofile.Student', on_delete=models.CASCADE)
    teacher_id = models.ForeignKey('userprofile.Teacher', on_delete=models.PROTECT)
    homework_completion = models.ForeignKey('homeworkflow.Homework_Uncompleted', on_delete=models.PROTECT) #get average by student id
    #sum(student_id) of homework_uncompleted
    attendance_rate = models.ForeignKey('homeworkflow.Attendance', on_delete=models.PROTECT)  #get average by student id
    date_created = models.DateField(auto_now_add=True)
    written_feedback = models.TextField()
    social_behaviour = models.CharField(choices=behaviour, max_length=10)
    work_ethics = models.CharField(choices=behaviour, max_length=10)
    parent_checked = models.BooleanField(default=False)
