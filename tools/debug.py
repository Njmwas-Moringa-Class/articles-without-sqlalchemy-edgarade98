#!/usr/bin/env python3
import ipdb;

from Author import Author 
from Article import Article
from Magazine import Magazine

if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###

 class TestAuthor:
    def setUp(self):
        self.author1 = Author("Sam Pat")

    def test_add_article(self):
        self.author1.add_article("Python Magazine", "The Python Book")

    def test_magazines(self):
        self.author1.add_article("Python Magazine", "The Python Book")
        self.author1.add_article("Tech Journal", "Tech World")
        self.assertCountEqual(self.author1.magazines(), ["Python Magazine", "Tech Journal"])

    def test_topic_areas(self):
        self.author1.add_article("Python Magazine", "The Python Book")
        self.author1.add_article("Tech Journal", "Tech World")
        self.assertCountEqual(self.author1.topic_areas(), ["Python", "Tech"])

class TestArticle:
    def setUp(self):
        self.article1 = Article("Article1", "Author1", "Python", "Python Magazine")
        self.article2 = Article("Article2", "Author2", "Tech", "Tech Journal")

    def test_init(self):
        self.assertEqual(self.article1.title, "Article1")
        self.assertEqual(self.article1.author, "Author1")
        self.assertEqual(self.article1.topic_area, "Python")
        self.assertEqual(self.article1.magazine, "Python Magazine")

class TestMagazine:
    def setUp(self):
        self.magazine1 = Magazine("Python Magazine")
        self.magazine2 = Magazine("Tech Journal")
        self.author1 = Author("Author1")
        self.author2 = Author("Author2")
        self.article1 = Article("Article1", "Author1", "Python", "Python Magazine")
        self.article2 = Article("Article2", "Author2", "Tech", "Tech Journal")

    def test_add_article(self):
        self.magazine1.add_article(self.article1)
        self.assertEqual(len(self.magazine1.articles), 1)

    def test_contributing_authors(self):
        self.magazine1.add_article(self.article1)
        self.assertCountEqual(self.magazine1.contributing_authors(), ["Author1"])



# DO NOT REMOVE THIS
    ipdb.set_trace()
