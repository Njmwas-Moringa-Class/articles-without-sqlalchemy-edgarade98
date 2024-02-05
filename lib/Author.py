
from Magazine import Magazine

class Author:
    all_authors = []

    pass
    def __init__(self, name):
        self._name = name
        Author.all_authors.append(self)

    def get_articles(self):
        from Article import Article  # Move import statement here
        return Article.get_articles_by_author(self.id)

    def get_name(self):
        return self._name
    
    
    def get_magazines (self) :

        author_magazines = set()
        for article in self.articles():
            author_magazines.add(article.get_magazine())
        return list(author_magazines)
    
    
@classmethod
def get_all_authors(cls):
    return cls.all_authors





