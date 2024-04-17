class data():
    def __init__(self, user, password, url):
        self.user = user
        self.password = password
        self.url = url

      
class maldata():
    def __init__(self, maluser, malpass, shortuser):
        self.maluser = maluser
        self.malpass = malpass
        self.shortuser = shortuser
    
xd = data("234", "123", "https://orbi.edu.do/")  #Data cambiada por privacidad
xd1 = maldata("202020201", "whateva", "U")


        