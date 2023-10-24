# Generated by Django 4.2.5 on 2023-10-18 22:39

from django.db import migrations


def forwards_func(apps, schema_editor):
    """Migrate single version projects to new versioning scheme field."""
    Project = apps.get_model("projects", "Project")
    Project.objects.filter(single_version=True).update(
        versioning_scheme="single_version",
        # Set this field to false, so we always rely on the versioning scheme field instead.
        single_version=False,
    )
    # Migrate projects that were created before the versioning scheme field was added.
    Project.objects.filter(versioning_scheme=None).update(
        versioning_scheme="multi_version"
    )


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0109_add_project_versioning_scheme"),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
