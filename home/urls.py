from django.urls import path
from .views import index, awards, experience, interests, skills, education, base
urlpatterns = [
    path("", index, name="index"),
    path("base/", base, name = "base"),
    path("awards/", awards, name="awards"),
    path("education/", education, name="education"),
    path("experience/", experience, name="experience"),
    path("interests/", interests, name="interests"),
    path("skills/", skills, name="skills"),
]