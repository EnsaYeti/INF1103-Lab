class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str):
        self.__supplier_id = supplier_id
        self.__name = name
        self.__contact_email = contact_email

    @property
    def supplier_id(self) -> str:
        return self.__supplier_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def contact_email(self) -> str:
        return self.__contact_email

    def display_information(self):
        print(f"Supplier {self.__supplier_id} | {self.__name} | {self.__contact_email}")

    def to_dict(self):
        return {"ID": self.__supplier_id, "Name": self.__name, "Email": self.__contact_email}

    @classmethod
    def from_dict(cls, data):
        return cls(data["ID"], data["Name"], data["Email"])