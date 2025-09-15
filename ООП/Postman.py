from ООП.Person_module import Person
from ООП.Post_module import Post


class Postman(Person, Post):
   pass
anna = Postman("Геннадий", 65, "мужской", 210, 100)


print(anna.send_parcel())
