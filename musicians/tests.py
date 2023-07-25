from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Musician

class MusicianTest(TestCase):
      
      @classmethod
      def setUpTestData(cls):
          testuser1 = get_user_model().objects.create_user(
              username='testuser1', password='1234'
          )
  
          testuser1.save()
  
          test_musician = Musician.objects.create(
              owner = testuser1,
              name = 'Kurt Cobain',
              instrument = 'guitar'
          )
  
          test_musician.save()

          test_musician_2 = Musician.objects.create(
              owner = testuser1,
              name = 'Dave Grohl',
              instrument = 'drums'
          )
          test_musician_2.save()
  
      def test_musician_content(self):
          musician = Musician.objects.get(id=1)
          actual_owner = str(musician.owner)
          actual_name = str(musician.name)
          actual_instrument = str(musician.instrument)
  
          self.assertEqual(actual_owner, 'testuser1')
          self.assertEqual(actual_name, 'Kurt Cobain')
          self.assertEqual(actual_instrument, 'guitar')

      def test_musician_2_content(self):
          musician = Musician.objects.get(id=2)
          actual_owner = str(musician.owner)
          actual_name = str(musician.name)
          actual_instrument = str(musician.instrument)
  
          self.assertEqual(actual_owner, 'testuser1')
          self.assertEqual(actual_name, 'Dave Grohl')
          self.assertEqual(actual_instrument, 'drums')
