import random

class Post:
    def __init__(self):
        self.__parcels = {}
        self.__name = "post office"
        self.__post_id = "7732"
        self.__id_password = {}#словарь id пароль
        print("Объект создан")
    @property
    def name(self):
        return self.__name  #геттер для получения имени почты
    @property
    def id(self):
        return self.__post_id   #геттер для айди почты
    @name.setter
    def name(self, new_name):
        self.__name = new_name  #сеттер для имени почты

    @property
    def parcels(self):
        return self.__parcels

    def __generate_id(self):
        while True:
            parcel_id = str(random.randint(100, 999))
            if parcel_id not in self.__parcels:
                return parcel_id

    def send_parcel(self):
        parcel_name = input("введите название посылки: ")
        parcel_id = self.__generate_id()
        self.__parcels[parcel_id] = parcel_name
        password = input(f"введите пароль для посылки {parcel_id}: ")
        self.__id_password[parcel_id] = password
        print(f"посылка {parcel_name} успешно отправлена, id {parcel_id}")

    def receive_parcel(self):
        parcel_id = input("введите id посылки: ")
        if parcel_id in self.__parcels: # проверка есть ли посылка с таким id
            password = input("введите пароль: ")
            if password == self.__id_password[parcel_id]:   # сравнение пароля
                del self.__parcels[parcel_id]   # "удаление" посылки если пароль верный
                print(f"посылка {parcel_id} получена")
            else:
                print("неверный пароль")    # уведомление об ошибке, что пароль не правильный
        else:
            print(f"посылка с id {parcel_id} не найдена")   # уведомление, если посылки нет

# post = Post()
# post.send_parcel()
# post.send_parcel()
# #print(post._Post__parcels)
# print(post.parcels)
# #print(post.name)
# #print(post.id)
# post.receive_parcel()
# #print(post.parcels)
# #print(post._Post__id_password)