# Generated by Django 2.2 on 2023-09-11 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='lab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lab.Lab', verbose_name='实验室'),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='medicineUsedNum',
            field=models.PositiveIntegerField(default=0, verbose_name='药品使用量(/g或/ml)'),
        ),
        migrations.AlterField(
            model_name='commonuser',
            name='cate',
            field=models.BooleanField(default=False, verbose_name='是否学生'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='upload_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='riskfactor',
            field=models.IntegerField(default=0, verbose_name='风险度（值越大越危险）'),
        ),
    ]
