from django.db import models


class Providers(models.Model):
    group = models.CharField('grupo', max_length=50)
    name = models.CharField('nome', max_length=100)
    note = models.TextField('observações', )
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    update_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'fornecedor'
        verbose_name_plural = 'fornecedores'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Functionarys(models.Model):
    group = models.CharField('grupo', max_length=50)
    name = models.CharField('nome', max_length=100)
    membership = models.CharField('filiação', max_length=100)
    conjugate = models.CharField('conjugue', max_length=100)
    salary = models.DecimalField('salário', max_digits=15, decimal_places=2)
    note = models.TextField('observações', )
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    update_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'funcionário'
        verbose_name_plural = 'funcionários'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Requisitions(models.Model):
    open = 'A'
    paid = 'P'
    STATES = (
        (open, 'Aberto'),
        (paid, 'Pago')
    )
    number = models.AutoField('número', primary_key=True)
    provider = models.ForeignKey('Providers', on_delete=models.CASCADE,
                                 verbose_name='fornecedor')
    requester = models.CharField('requisitante', max_length=100)
    functionary = models.ForeignKey('Functionarys', on_delete=models.CASCADE,
                                    verbose_name='funcionário')
    activity = models.CharField('atividade', max_length=100)
    description = models.TextField('Descrição')
    value = models.DecimalField('valor', max_digits=15, decimal_places=2)
    discount = models.DecimalField('desconto', max_digits=15, decimal_places=2)
    state = models.CharField('situação', max_length=1, choices=STATES,
                             default=open)
    note = models.TextField('observações', )
    paid_at = models.DateTimeField('pago em', auto_now_add=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    update_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'requisição'
        verbose_name_plural = 'requisições'
        ordering = ('number',)

    def __str__(self):
        return str(self.number)
