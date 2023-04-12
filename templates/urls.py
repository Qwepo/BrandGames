from django.views.generic import TemplateView
from django.urls import path

urlpatterns = [
    path(
        "docs/",
        TemplateView.as_view(template_name="docs.html", extra_context={"schema_url": "api_schema"}),
        name="swagger-ui",
    ),
]
