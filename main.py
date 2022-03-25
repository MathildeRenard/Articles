class Article:

    def __init__(self,prix,code,nombre):
        self.prix = prix
        self.nombre = nombre
        self.code = code


if  __name__ =='__main__':
    print("Bienvenue")
    article = Article(12,"CA",20)
    print("l'article coute",article.prix,"euros")
    print("Son code est : ",article.code)
    print("Il y a en stock :",article.nombre,"articles")