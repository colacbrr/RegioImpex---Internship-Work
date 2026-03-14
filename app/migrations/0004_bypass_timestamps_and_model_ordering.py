import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_alter_bypass_observatii"),
    ]

    operations = [
        migrations.AddField(
            model_name="bypass",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="bypass",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterModelOptions(
            name="bypass",
            options={"ordering": ["-created_at"], "verbose_name_plural": "Bypass entries"},
        ),
        migrations.AlterModelOptions(
            name="client",
            options={"ordering": ["nume"]},
        ),
        migrations.AlterModelOptions(
            name="depozit",
            options={"ordering": ["nume"]},
        ),
        migrations.AlterModelOptions(
            name="particular",
            options={"ordering": ["nume"]},
        ),
        migrations.AlterModelOptions(
            name="test",
            options={"ordering": ["nume"]},
        ),
    ]
