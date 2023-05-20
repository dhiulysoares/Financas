# Generated by Django 4.2.1 on 2023-05-20 21:28

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nome do cartão / Beneficiário')),
                ('limit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='limite')),
            ],
            options={
                'verbose_name': 'Cartão de crédito',
                'verbose_name_plural': 'Cartões de crédito',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Preço total da fatura')),
                ('pay_date', models.DateField(blank=True, null=True, verbose_name='Data de vencimento')),
                ('credit_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.creditcard', verbose_name='Cartão de Crédito')),
            ],
            options={
                'verbose_name': 'Fatura',
                'verbose_name_plural': 'Faturas',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descrição da compra')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Preço')),
                ('buy_date', models.DateField(default=datetime.date.today, verbose_name='Data da compra')),
                ('pay_date', models.DateField(blank=True, null=True, verbose_name='Data de vencimento')),
                ('total_parcels', models.IntegerField(default=1, verbose_name='Número de parcelas')),
                ('payment_form', models.CharField(blank=True, choices=[('in_cash', 'À vista'), ('installments', 'Parcelado'), ('period', 'A prazo')], max_length=200, null=True, verbose_name='Forma de pagamento')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.invoice', verbose_name='Fatura')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('transaction_type', models.CharField(blank=True, choices=[('input', 'Entrada'), ('output', 'Saída')], max_length=200, null=True, verbose_name='Tipo de transação')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Data da transação')),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor transacionado')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Transação',
                'verbose_name_plural': 'Transações',
            },
        ),
        migrations.DeleteModel(
            name='Movement',
        ),
    ]