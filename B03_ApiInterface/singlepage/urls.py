from django.urls import path


from . import views

app_name = "singlepage"
urlpatterns = [
    path("output", views.output, name="output"),
    path("sections/<int:num>", views.section, name="section"),
    path("OperatorInfo", views.operator_info, name="opInfo")
]