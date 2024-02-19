from Magazine import Magazine


class Author:
    all_authors = []

    def __init__(self, name):
        self._name = name
        Author.all_authors.append(self)
        self.all_articles = []

    @classmethod
    def get_author_by_id(cls, author_id):
        return cls.all_authors[author_id]

    def articles(self):
        return self.all_articles

    def get_articles(self):
        return Article.get_articles_by_author(self.id)

    def get_name(self):
        return self._name


    def get_magazines (self) :
    
        author_magazines = set()
        for article in self.articles():
            author_magazines.add(article.get_magazine())
        return list(author_magazines)
    
    def add_article (self, magazine, title):
        from Article import Article
        article = Article(self, magazine, title)
        self.all_articles.append(article)
        Article.all_articles.append(article)
    
    def topic_areas(self):
        magazine_categories = set()
        for magazine in self.get_magazines():
            magazine_categories.add(magazine.get_category())
        return list(magazine_categories)

@classmethod
def get_all_authors(cls):
    return cls.all_authors







