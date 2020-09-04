from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('study_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=50)),
                ('limit', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(null=True)),
                ('cellphone', models.CharField(max_length=20, null=True)),
                ('gender', models.CharField(max_length=6)),
                ('description', models.CharField(max_length=1024, null=True)),
                ('categories', models.CharField(max_length=1024, null=True)),
                ('kakao_profile_img', models.CharField(max_length=1024, null=True)),
                ('s3_profile_img', models.FileField(blank=True, null=True, upload_to='')),
                ('img_flag', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StudyMember',
            fields=[
                ('study_member_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_manager', models.BooleanField(default=False)),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Study')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
        migrations.AddField(
            model_name='study',
            name='study_members',
            field=models.ManyToManyField(through='api.StudyMember', to='api.User'),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('schedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('place', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Study')),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
        migrations.CreateModel(
            name='ActivityPicture',
            fields=[
                ('activity_picture_id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Study')),
            ],
        ),
    ]
