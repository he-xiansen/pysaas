# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2022-07-15 08:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileRepository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.SmallIntegerField(choices=[(1, '文件'), (2, '文件夹')], verbose_name='类型')),
                ('name', models.CharField(help_text='文件/文件夹名', max_length=32, verbose_name='文件夹名称')),
                ('key', models.CharField(blank=True, max_length=128, null=True, verbose_name='文件储存在COS中的KEY')),
                ('file_size', models.BigIntegerField(blank=True, help_text='字节', null=True, verbose_name='文件大小')),
                ('file_path', models.CharField(blank=True, max_length=255, null=True, verbose_name='文件路径')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='web.FileRepository', verbose_name='父级目录')),
            ],
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=80, verbose_name='主题')),
                ('desc', models.TextField(verbose_name='问题描述')),
                ('priority', models.CharField(choices=[('danger', '高'), ('warning', '中'), ('success', '低')], default='danger', max_length=12, verbose_name='优先级')),
                ('status', models.SmallIntegerField(choices=[(1, '新建'), (2, '处理中'), (3, '已解决'), (4, '已忽略'), (5, '待反馈'), (6, '已关闭'), (7, '重新打开')], default=1, verbose_name='状态')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='开始时间')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='结束时间')),
                ('mode', models.SmallIntegerField(choices=[(1, '公开模式'), (2, '隐私模式')], default=1, verbose_name='模式')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('latest_update_datetime', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='IssuesReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_type', models.IntegerField(choices=[(1, '修改记录'), (2, '回复')], verbose_name='类型')),
                ('content', models.TextField(verbose_name='描述')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='IssuesType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='类型名称')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='模块名称')),
            ],
        ),
        migrations.CreateModel(
            name='PricePolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.SmallIntegerField(choices=[(1, '免费版'), (2, '收费版'), (3, '其他')], default=2, verbose_name='收费类型')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('price', models.PositiveIntegerField(verbose_name='价格')),
                ('project_num', models.PositiveIntegerField(verbose_name='项目数')),
                ('project_member', models.PositiveIntegerField(verbose_name='项目成员数')),
                ('project_space', models.PositiveIntegerField(help_text='G', verbose_name='单项目空间')),
                ('per_file_size', models.PositiveIntegerField(help_text='M', verbose_name='单文件大小')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='项目名')),
                ('color', models.SmallIntegerField(choices=[(1, '#56b8eb'), (2, '#f28033'), (3, '#ebc656'), (4, '#a2d148'), (5, '#20BFA4'), (6, '#7461c2'), (7, '#20bfa3')], default=1, verbose_name='颜色')),
                ('desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='项目描述')),
                ('use_space', models.BigIntegerField(default=0, help_text='字节', verbose_name='项目已使用空间')),
                ('star', models.BooleanField(default=False, verbose_name='星标')),
                ('join_count', models.SmallIntegerField(default=1, verbose_name='参与人数')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('bucket', models.CharField(max_length=128, verbose_name='cos桶')),
                ('region', models.CharField(max_length=32, verbose_name='cos区域')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=64, unique=True, verbose_name='邀请码')),
                ('count', models.PositiveIntegerField(blank=True, help_text='空表示无数量限制', null=True, verbose_name='限制数量')),
                ('use_count', models.PositiveIntegerField(default=0, verbose_name='已邀请数量')),
                ('period', models.IntegerField(choices=[(30, '30分钟'), (60, '1小时'), (300, '5小时'), (1440, '24小时')], default=1440, verbose_name='有效期')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.BooleanField(default=False, verbose_name='星标')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='加入时间')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Project', verbose_name='项目')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(1, '未支付'), (2, '已支付')], verbose_name='状态')),
                ('order', models.CharField(max_length=64, unique=True, verbose_name='订单号')),
                ('count', models.IntegerField(help_text='0表示无限期', verbose_name='数量（年）')),
                ('price', models.IntegerField(verbose_name='实际支付价格')),
                ('start_datetime', models.DateTimeField(blank=True, null=True, verbose_name='开始时间')),
                ('end_datetime', models.DateTimeField(blank=True, null=True, verbose_name='结束时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('price_policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.PricePolicy', verbose_name='价格策略')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=32, verbose_name='用户名')),
                ('email', models.EmailField(max_length=32, verbose_name='邮箱')),
                ('mobile_phone', models.CharField(max_length=32, verbose_name='手机号')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
            ],
        ),
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('depth', models.IntegerField(default=1, verbose_name='深度')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='web.Wiki', verbose_name='父文章')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Project', verbose_name='项目')),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.UserInfo', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='projectuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.UserInfo', verbose_name='参与者'),
        ),
        migrations.AddField(
            model_name='projectinvite',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_invite', to='web.UserInfo', verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='projectinvite',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.UserInfo', verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='module',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='issuestype',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='issuesreply',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_reply', to='web.UserInfo', verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='issuesreply',
            name='issues',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Issues', verbose_name='问题'),
        ),
        migrations.AddField(
            model_name='issuesreply',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.IssuesReply', verbose_name='回复'),
        ),
        migrations.AddField(
            model_name='issues',
            name='assign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='web.UserInfo', verbose_name='指派'),
        ),
        migrations.AddField(
            model_name='issues',
            name='attention',
            field=models.ManyToManyField(blank=True, related_name='observe', to='web.UserInfo', verbose_name='关注者'),
        ),
        migrations.AddField(
            model_name='issues',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_problems', to='web.UserInfo', verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='issues',
            name='issues_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.IssuesType', verbose_name='问题类型'),
        ),
        migrations.AddField(
            model_name='issues',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Module', verbose_name='模块'),
        ),
        migrations.AddField(
            model_name='issues',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child', to='web.Issues', verbose_name='父问题'),
        ),
        migrations.AddField(
            model_name='issues',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='filerepository',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='filerepository',
            name='update_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.UserInfo', verbose_name='最近更新者'),
        ),
    ]
