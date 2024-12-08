class Article:
    all=[]
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,title):
        if hasattr(self,"_title"):
            return
        if not isinstance(title, str) and not(5 <= len(title) <= 50):
            raise TypeError("name must be a string of character between 5 and 50")
        self._title = title
   

class Author:
    def __init__(self, name):
        self.name=name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if hasattr(self, "_name"):
            return
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self._name = name
   
    def articles(self):
        return[article for article in Article.all if article.author == self]
        
    def magazines(self):
        return list(set(article.magazine for article in self.articles()))
        
    def add_article(self, magazine, title):
        return Article(self,magazine,title)

    def topic_areas(self):
        return list(set((article.magazine.category) for article in self.articles() if article.magazine.category))or None

class Magazine:
    magazines=[]
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.magazines.append(self)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name, str) and (2 <= len(name) <= 16):
            self._name=name
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self,category):
        if isinstance(category,str)and(len(category)>0):
            self._category=category

    def articles(self):
        return[article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self.articles():
            return None
        return[article.title for article in self.articles() ] 

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        contributing_authors = [author for author in set(authors)if authors.count(author) > 2 and isinstance(author, Author)]
        return contributing_authors if contributing_authors else None