from django.test import TestCase
from todo.models import List, Task
from django.core.exceptions import ValidationError

class ListAndItemModelsTest(TestCase):

    def test_saving_and_saving_list(self):
        list_ = List(name_text="prova")
        list_.save()
        list2 = List(name_text="tega")

        saved_list = List.objects.first()
        self.assertEqual(saved_list.name_text, "prova")
        self.assertEqual(saved_list, list_)
        self.assertEqual(saved_list, list2)

        first_task = Task(name_text = "primo")
        first_task.save()

        saved_task = Task.objects.all()
        self.assertEqual(saved_task.count(), 1)

"""
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)

    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    def test_get_absolute_url(self):
    	list_ = List.objects.create()
    	self.assertEqual(list_.get_absolute_url(), '/lists/%d/' % (list_.id,))

"""