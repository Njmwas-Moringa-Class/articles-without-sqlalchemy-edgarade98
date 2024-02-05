class Magazine:
    pass

    all_magazines = []

    def __init__(self, name, category):
        self._name =  name
        self._category = category
        Magazine.all_magazines.append(self)
    
    def get_name(self):
        return self._name
    
    def get_category(self):
        return  self._category
    
    def get_magazine_contributors (self):
         
        magazines_contributors = set()
        for article in self.articles():
            magazines_contributors.add(article.get_magazine())
        return list(magazines_contributors)
    
    @classmethod
    def get_all_magazines (cls):
        return  cls.all_magazines
    


