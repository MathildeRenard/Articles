class Article:

    def __init__(self,prix,code,nombre):
        self.prix = prix
        self.nombre = nombre
        self.code = code


if  __name__ =='__main__':
    print("Bienvenue")
    
    
    nombre = input("Saisissez le nombre d'articles voulus :") 
    
    prix = input("Saisissez le prix de l'article voulu :") 
    code = input("Saisissez le code de l'article voulu :") 
    article = Article(prix,code,nombre)
    print("l'article coute",article.prix,"euros")
    print("Son code est : ",article.code)
    print("Il y a en stock :",article.nombre,"articles")
    