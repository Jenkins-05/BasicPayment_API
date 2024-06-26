# Generated by Django 5.0.4 on 2024-04-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_rename_users_transaction_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('SUCCEESS', 'success'), ('PENDING', 'pending'), ('DECLINED', 'declined')], default='pending', max_length=10),
        ),
    ]
