from django.test import TestCase
from django.contrib.auth.models import User
from stocks.models import PartsMaster, SubCategory, Issues


class ModelTest(TestCase):

    @classmethod
    def setUpClass(cls):

        super(ModelTest, cls).setUpClass()

        # create and save a Department object.
        sub = SubCategory(name="Furniture")
        sub.save()
        # create a User model object in temporary database.

        # create a User model object in temporary database.
        user = User(username='tom', password='tom')
        user.save()

        # get employee user.
        user = User.objects.get(username='tom')
        print('Added user data : ')
        print(user)
        print('')

        sub = SubCategory.objects.get(name='Furniture')
        print('Added Sub Category data : ')
        print(sub)
        print('')

        stk = PartsMaster(
            category="Asset",
            subcategory=sub,
            part_no="90000000000",
            item_no="AIS1",
            item_name='testname',
            quantity=100,
            updated_by=user,
        )
        stk.save()
        print('Added stock data : ')
        print(stk)

        # create and save the Employee object.
        iss = Issues(
            part=stk,
            issue_quantity=1,
            issue_to=user,
            updated_by=user
        )
        iss.save()
        print('Added issue : ')
        print(iss)

    def test_subcategory_models(self):
        sub = SubCategory.objects.get(name='Furniture')
        self.assertEqual(sub.name, 'Furniture')

    def test_stock_models(self):
        stk = PartsMaster.objects.get(item_name="testname")
        self.assertEqual(stk.updated_by, 'tom')
