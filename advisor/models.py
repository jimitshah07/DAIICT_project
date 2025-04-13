from django.db import models

# # Create your models here.
# # Define Skill Model
# class Skill(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField()

#     def __str__(self):
#         return self.name

# # Define JobProfile Model (representing job titles and required skills)
# class JobProfile(models.Model):
#     title = models.CharField(max_length=200)
#     required_skills = models.ManyToManyField(Skill, related_name='job_profiles')

#     def __str__(self):
#         return self.title

# # Define User Skill Assessment Model
# class UserSkillAssessment(models.Model):
#     user_name = models.CharField(max_length=100)
#     skills = models.ManyToManyField(Skill, through='UserSkillProficiency')

#     def __str__(self):
#         return self.user_name

# # Define UserSkillProficiency Model (to store proficiency level for each skill)
# class UserSkillProficiency(models.Model):
#     SKILL_LEVEL_CHOICES = [
#         ('beginner', 'Beginner'),
#         ('intermediate', 'Intermediate'),
#         ('expert', 'Expert'),
#     ]
#     user = models.ForeignKey(UserSkillAssessment, on_delete=models.CASCADE)
#     skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
#     proficiency = models.CharField(max_length=20, choices=SKILL_LEVEL_CHOICES)

#     def __str__(self):
#         return f"{self.user.user_name} - {self.skill.name} - {self.proficiency}"


# from django.db import models
# # from django.contrib.auth.models import User

# # class UserAssessment(models.Model):
# #     USER_TYPE_CHOICES = [
# #         ('student', 'Student'),
# #         ('professional', 'Professional'),
# #     ]

# #     user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='advisor_assessments')
# #     user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
# #     interests = models.JSONField()
# #     generated_questions = models.TextField(blank=True, null=True)
# #     created_at = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return f"{self.user.username} - {self.user_type}"
