# Generated by Django 2.2 on 2020-04-08 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200408_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间'),
        ),
        migrations.AddField(
            model_name='banner',
            name='updated_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='is_http',
            field=models.BooleanField(default=False, verbose_name='是否站外地址'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='link',
            field=models.CharField(blank=True, help_text='站内地址格式：/users/<br>站外地址格式：http://www.baidu.com', max_length=150, null=True, verbose_name='轮播图广告地址'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='名称'),
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='名称')),
                ('orders', models.IntegerField(default=0, verbose_name='显示顺序')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否上架')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(blank=True, null=True, verbose_name='更新时间')),
                ('link', models.CharField(help_text='如果是站外链接,必须加上协议, 格式如: http://www.renran.cn', max_length=500, verbose_name='导航地址')),
                ('is_http', models.BooleanField(default=False, verbose_name='是否站外地址')),
                ('option', models.SmallIntegerField(choices=[(1, '头部导航'), (2, '脚部导航')], default=1, verbose_name='导航位置')),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='son', to='home.Nav', verbose_name='父亲导航')),
            ],
            options={
                'verbose_name': '导航菜单',
                'db_table': 'rr_nav',
            },
        ),
    ]
