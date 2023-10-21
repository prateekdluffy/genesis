# Generated by Django 4.2.6 on 2023-10-19 07:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddToExerciseListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=1, default=1.0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='AddToFoodListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=1, default=1.0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='NutrisumExerciseListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NutrisumExerciseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('calories_burn', models.DecimalField(decimal_places=2, max_digits=5)),
                ('part_name', models.CharField(max_length=128)),
                ('weight_or_strength', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='NutrisumFoodListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NutrisumFoodModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('calories', models.DecimalField(decimal_places=2, max_digits=5)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=5)),
                ('carbohydrate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vitamins', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='NutrisumHistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('calorie_intake_count', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('calorie_burnt_count', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('public', models.BooleanField(default=True)),
                ('exercise_list', models.ManyToManyField(blank=True, related_name='Exercise_Completed_List', through='nutrisum.AddToExerciseListModel', to='nutrisum.nutrisumexerciselistmodel')),
                ('food_list', models.ManyToManyField(blank=True, related_name='Food_Intake_List', through='nutrisum.AddToFoodListModel', to='nutrisum.nutrisumfoodlistmodel')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.AddField(
            model_name='nutrisumfoodlistmodel',
            name='food_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrisum.nutrisumfoodmodel'),
        ),
        migrations.AddField(
            model_name='nutrisumfoodlistmodel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='nutrisumexerciselistmodel',
            name='exercise_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrisum.nutrisumexercisemodel'),
        ),
        migrations.AddField(
            model_name='nutrisumexerciselistmodel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrisum.nutrisumhistorymodel')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='addtofoodlistmodel',
            name='food_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrisum.nutrisumfoodlistmodel'),
        ),
        migrations.AddField(
            model_name='addtofoodlistmodel',
            name='history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrisum.nutrisumhistorymodel'),
        ),
        migrations.AddField(
            model_name='addtoexerciselistmodel',
            name='exercise_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrisum.nutrisumexerciselistmodel'),
        ),
        migrations.AddField(
            model_name='addtoexerciselistmodel',
            name='history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrisum.nutrisumhistorymodel'),
        ),
        migrations.AlterUniqueTogether(
            name='nutrisumfoodlistmodel',
            unique_together={('owner', 'food_item')},
        ),
        migrations.AlterUniqueTogether(
            name='nutrisumexerciselistmodel',
            unique_together={('owner', 'exercise_item')},
        ),
    ]