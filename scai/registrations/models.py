from django.db import models
from django.urls import reverse


class Provider(models.Model):
    group = models.CharField('grupo', blank=True, max_length=50)
    name = models.CharField('nome', max_length=100)
    note = models.TextField('observações', blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    update_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'fornecedor'
        verbose_name_plural = 'fornecedores'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Functionary(models.Model):
    GROUPS = (
        ('functionary', 'Funcionário'),
        ('leadership', 'Liderança'),
        ('agricultural', 'Agríola'),
        ('retired', 'Aposentados'),
        ('agricultural wives', 'Esposas agricola'),
        ('cleaning', 'Limpeza'),
        ('education 1º step', 'Educação 1º etapa'),
        ('education 2º step', 'Educação 2º etapa'),
        ('krimeiruk wives', 'Esposas Krimeiruk'),
        ('kamkrokró wives', 'Esposas Kamkrokró'),
        ('purekokeí wives', 'Esposas Purokokeí'),
    )
    group = models.CharField('grupo', max_length=50, choices=GROUPS,
                             default='functionary')
    name = models.CharField('nome', max_length=100)
    membership = models.CharField('filiação', max_length=100, blank=True)
    conjugate = models.CharField('conjugue', max_length=100, blank=True)
    salary = models.DecimalField('salário', default=0, max_digits=15,
                                 decimal_places=2)
    note = models.TextField('observações', blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    update_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'índio'
        verbose_name_plural = 'índios'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Requisition(models.Model):
    open = 'A'
    paid = 'P'
    STATES = (
        (open, 'Aberto'),
        (paid, 'Pago')
    )
    number = models.AutoField('número', primary_key=True)
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE,
                                 verbose_name='fornecedor')
    requester = models.CharField('requisitante', max_length=100, blank=True)
    functionary = models.ForeignKey('Functionary', on_delete=models.CASCADE,
                                    verbose_name='índio')
    activity = models.CharField('atividade', max_length=100, blank=True)
    description = models.TextField('Descrição', blank=True)
    value = models.DecimalField('valor', default=0, max_digits=15,
                                decimal_places=2)
    discount = models.DecimalField('desconto', default=0, max_digits=15,
                                   decimal_places=2, blank=True)
    state = models.CharField('situação', max_length=1, choices=STATES,
                             default=open)
    note = models.TextField('observações', blank=True)
    paid_at = models.DateTimeField('pago em', auto_now_add=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    update_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'requisição'
        verbose_name_plural = 'requisições'
        ordering = ('number',)

    def __str__(self):
        return str(self.number)

    @property
    def document_url(self):
        return reverse('document-requisition', kwargs={'pk': self.pk})

    @property
    def total_value(self):
        return self.value - self.discount
