from datetime import datetime
from django.test import TestCase
from scai.registrations.models import Provider, Functionary, Requisition


class ProvidersModelTest(TestCase):
    def setUp(self):
        self.obj = Provider(
            group='Supermercados',
            name='Supermercado Carro Chefe',
            note='Observações em geral',
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Provider.objects.exists())

    def test_created_at(self):
        """Providers must have an auto created_at, attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_update_at(self):
        """Providers must have an auto update_at, attr"""
        self.assertIsInstance(self.obj.update_at, datetime)

    def test_str(self):
        self.assertEqual('Supermercado Carro Chefe', str(self.obj))


class FunctionarysModelTest(TestCase):
    def setUp(self):
        self.obj = Functionary(
            group='Xikrin',
            name='Koikuiure Kayapo',
            membership='Koikuare',
            conjugate='Pangrã',
            salary=3000.00,
            note='Observações em geral',
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Functionary.objects.exists())

    def test_created_at(self):
        """Functionary must have an auto created_at, attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_update_at(self):
        """Functionary must have an auto update_at, attr"""
        self.assertIsInstance(self.obj.update_at, datetime)

    def test_str(self):
        self.assertEqual('Koikuiure Kayapo', str(self.obj))


class RequisitionsModelTest(TestCase):
    def setUp(self):
        self.obj = Requisition(
            number=1,
            provider=Provider.objects.create(name='Supermercado Carro Chefe'),
            requester='Koikuare',
            functionary=Functionary.objects.create(name='Koikuiure Kayapo'),
            activity='Desconto',
            description='Aquisição de gẽneros alimentícios',
            state='A',
            value=2800.00,
            discount=25.00,
            note='Observações em geral',
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Requisition.objects.exists())

    def test_created_at(self):
        """Requisition must have an auto created_at, attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_update_at(self):
        """Requisition must have an auto update_at, attr"""
        self.assertIsInstance(self.obj.update_at, datetime)

    def test_paid_at(self):
        """Requisition must have an auto update_at, attr"""

        self.assertIsInstance(self.obj.paid_at, datetime)

    def test_str(self):
        self.assertEqual('1', str(self.obj))
