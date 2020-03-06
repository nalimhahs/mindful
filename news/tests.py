from django.contrib.auth import get_user_model 
from django.test import Client, TestCase
from django.urls import reverse
from .models import News
class NewsTests(TestCase):
def setUp(self):
self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
)
        self.news = News.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
)
def test_string_representation(self):
    news = News(title='A sample title') 
    self.assertEqual(str(news), news.title)
def test_post_content(self): 
    self.assertEqual(f'{self.news.title}', 'A good title') 
    self.assertEqual(f'{self.news.author}', 'testuser') 
    self.assertEqual(f'{self.news.body}', 'Nice body content')
def test_post_list_view(self):
    response = self.client.get(reverse('home')) 
    self.assertEqual(response.status_code, 200) 
    self.assertContains(response, 'Nice body content') 
    self.assertTemplateUsed(response, 'allnews/allnews.html')
def test_post_detail_view(self):
    response = self.client.get('/news/1/')
    no_response = self.client.get('/news/100000/') 
    self.assertEqual(response.status_code, 200) 
    self.assertEqual(no_response.status_code, 404) 
    self.assertContains(response, 'A good title')   
    self.assertTemplateUsed(response, 'detail.html')