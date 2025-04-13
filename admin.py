from django.contrib import admin
from .models import Skill, JobProfile, UserSkillAssessment, UserSkillProficiency

admin.site.register(Skill)
admin.site.register(JobProfile)
admin.site.register(UserSkillAssessment)
admin.site.register(UserSkillProficiency)

