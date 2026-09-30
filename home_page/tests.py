from django.test import TestCase
from django.urls import reverse

from .models import Skill


class SkillViewTests(TestCase):
    def test_home_page_groups_skills_by_category(self):
        Skill.objects.create(name='HTML5', category='Frontend', order=1)
        Skill.objects.create(name='Django', category='Backend', order=1)
        Skill.objects.create(name='PostgreSQL', category='Database', order=1)
        Skill.objects.create(name='GitHub', category='Tools/Services', order=1)

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertIn('Frontend', response.context['skills_by_category'])
        self.assertIn('Backend', response.context['skills_by_category'])
        self.assertIn('Database', response.context['skills_by_category'])
        self.assertIn('Tools/Services', response.context['skills_by_category'])
