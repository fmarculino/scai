from datetime import datetime
from django.test import TestCase
from scai.registrations.models import Providers, Functionarys, Requisitions


class ProvidersModelTest(TestCase):
    def setUp(self):
        self.obj = Providers(
            group='Supermercados',
            name='Supermercado Carro Chefe',
            note='Observações em geral',
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Providers.objects.exists())

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
        self.obj = Functionarys(
            group='Xikrin',
            name='Koikuiure Kayapo',
            membership='Koikuare',
            conjugate='Pangrã',
            salary=3000.00,
            note='Observações em geral',
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Functionarys.objects.exists())

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
        self.obj = Requisitions(
            number=1,
            provider=Providers,
            requester='Koikuare',
            functionary=Functionarys,
            activity='Desconto',
            description='Aquisição de gẽneros alimentícios',
            state='A',
            value=2800.00,
            discount=25.00,
            note='Observações em geral',
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Requisitions.objects.exists())

    # def test_created_at(self):
    #     """Requisition must have an auto created_at, attr"""
    #     self.assertIsInstance(self.obj.created_at, datetime)
    #
    # def test_update_at(self):
    #     """Requisition must have an auto update_at, attr"""
    #     self.assertIsInstance(self.obj.update_at, datetime)
    #
    # def test_paid_at(self):
    #     """Requisition must have an auto update_at, attr"""
    #
    #     self.assertIsInstance(self.obj.paid_at, datetime)
    #
    # def test_str(self):
    #     self.assertEqual('Supermercado Carro Chefe', str(self.obj))
