# Generated by Django 2.0.7 on 2018-12-29 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0023_auto_20181227_2027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-created'], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='К-сть сторінок'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Видавництво'),
        ),
        migrations.AddField(
            model_name='book',
            name='publishing_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Рік видавництва'),
        ),
        migrations.AddField(
            model_name='book',
            name='amazon_link',
            field=models.URLField(blank=True, null=True, verbose_name='Посилання на книгу на Amazon'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=250, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book.Category', verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='book',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='club.Club', verbose_name='Клуб'),
        ),
        migrations.AlterField(
            model_name='book',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Додано'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(default='', verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book.Genre', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('UK', 'Ukrainian'), ('EN', 'English'), ('RU', 'Russian')], default='UK', max_length=2, verbose_name='Мова'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL, verbose_name='Власник'),
        ),
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(default='', upload_to='books_image', verbose_name='Зображення'),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('AV', 'Available'), ('BK', 'Booked')], default='AV', max_length=2, verbose_name='Статус'),
        ),
    ]