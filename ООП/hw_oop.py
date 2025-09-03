class Pochta:
    def __init__(self):
        self.parcels = {}
    def send_parcel(self, parcel_id, parcel_name):
        self.parcels[parcel_id] = parcel_name
    def receive_parcel(self, parcel_id):
        self.parcels.pop(parcel_id, None)
post = Pochta()
post.send_parcel("001", "Ноутбук")
post.send_parcel("002", "Телефон")
print(post.parcels)
post.receive_parcel("001")
print(post.parcels)