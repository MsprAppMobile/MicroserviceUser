class User:

    def __init__(self, id="", pseudo="", mail="", password="",telephone="",genre="",codeP="",ville="",adresse="",complementAdresse="",role=""):
        self.id = id
        self.pseudo = pseudo
        self.mail = mail
        self.password = password
        self.telephone = telephone
        self.genre = genre
        self.codeP = codeP
        self.ville = ville
        self.adresse = adresse
        self.complementAdresse = complementAdresse
        self.role = role


    def getId(self):
        return self.id

    def getPseudo(self):
        return self.pseudo

    def getMail(self):
        return self.mail

    def getPassword(self):
        return self.password


    def getTel(self):
        return self.telephone

    def getGenre(self):
        return self.genre
    
    def getCodeP(self):
        return self.codeP

    def getVille(self):
        return self.ville
    

    def getAdresse(self):
        return self.adresse

    def getCompAdresse(self):
        return self.complementAdresse

    def getRole(self):
        return self.role
    
    