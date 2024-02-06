from Author import Author
from Magazine import Magazine

class Article:
    pass
   
    all_articles = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all_articles.append(self)
    
    def get_author(self):
        from Author import Author  #import statement
        return Author.get_author_by_id(self.author)

    def get_title(self):
        return self._title
    
    def get_author(self):
        return self._author
    
    def get_magazine (self):
        return self._magazine
    
    @classmethod
    def get_all_articles (cls):
        return  cls.all_articles
    
    

    
    