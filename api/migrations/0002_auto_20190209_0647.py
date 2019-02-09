# Generated by Django 2.1.5 on 2019-02-09 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kondo',
            name='baba',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='kondo_baba', to='api.Kondo'),
        ),
        migrations.AlterField(
            model_name='kondo',
            name='mama',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='kondo_mama', to='api.Kondo'),
        ),
        migrations.AlterField(
            model_name='mbuzi',
            name='baba',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mbuzi_baba', to='api.Mbuzi'),
        ),
        migrations.AlterField(
            model_name='mbuzi',
            name='mama',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mbuzi_mama', to='api.Mbuzi'),
        ),
        migrations.AlterField(
            model_name='myama',
            name='breeder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='breeder', to='api.Shamba'),
        ),
        migrations.AlterField(
            model_name='ngombe',
            name='baba',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ngombe_baba', to='api.Ngombe'),
        ),
        migrations.AlterField(
            model_name='ngombe',
            name='mama',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ngombe_mama', to='api.Ngombe'),
        ),
    ]
