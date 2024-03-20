class Article:

    all = []

    def __init__(self, author: object, magazine: object, title: str):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception('Author must be an instance of the Author class')

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise Exception('Magazine must be an instance of the Magazine class')
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title: str):
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, '_title'):
            self._title = title
        else:
            raise Exception('Title must be a string between 5 and 50 char; it is immutable once set')
        
class Author:
### Note to self: property, not method
    def __init__(self, name: str):
        self.name = name

    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name: str):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, '_name'):
            self._name = name
        else:
            raise Exception('Name must be a non-empty string, and may not be changed.')
    
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        result = []
        for article in Article.all:
            if article.author is self and not article.magazine in result:
                result.append(article.magazine)
        return result
                
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
# Result must be 0 (None), not an empty array or won't pass test
    def topic_areas(self):
        result = list(set([article.magazine.category for article in Article.all if article.author is self]))
        if len(result) > 0: 
            return result 

class Magazine:

    def __init__(self, name: str, category: str):
      
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name: str):
        if isinstance(name, str) and 2 <= len(name) <=16:
            self._name = name
        else:
            raise Exception('Name must be a non-empty string')
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category: str):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise Exception('Category value must a a non-empty string.')
        
    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list(set([article.author for article in Article.all if article.magazine is self]))

    def article_titles(self):
        result = [article.title for article in Article.all if article.magazine is self]
        if len(result):
            return result    

    def contributing_authors(self):
        authors_list = [author for author in self.contributors() if len([article for article in author.articles() if article.magazine is self]) > 2]
        if(len(authors_list) == 0):
            return None
        else:
            return authors_list
        
    def top_publisher():
        all_articles_by_magazine = [article.magazine for article in Article.all]
        highest_total = [None, 0]
        for magazine in set(all_articles_by_magazine):
            if all_articles_by_magazine.count(magazine) > highest_total[1]:
                highest_total = [magazine, all_articles_by_magazine.count(magazine)]
        return highest_total[0]