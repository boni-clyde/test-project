class RegisterAttributes:
    def __init__(self, number, email, number_autoreg, email_autoreg):
        self.number = number
        self.email = email
        self.number_autoreg = number_autoreg
        self.email_autoreg = email_autoreg

class AuthenticationAttributes:
    def __init__(self, ls, temp_number, temp_email):
        self.ls = ls
        self.temp_number = temp_number
        self.temp_email = temp_email

class Attributes:
    ELK_AUTH = AuthenticationAttributes(ls=1, temp_number=0, temp_email=0)
    ELK_REG = RegisterAttributes(number=1, email=1, number_autoreg=0, email_autoreg=0)
    
    ONLINE_AUTH = AuthenticationAttributes(ls=0, temp_number=1, temp_email=1)
    ONLINE_REG = RegisterAttributes(number=0, email=0, number_autoreg=0, email_autoreg=0)

    START_AUTH = AuthenticationAttributes(ls=1, temp_number=1, temp_email=1)
    START_REG = RegisterAttributes(number=1, email=1, number_autoreg=1, email_autoreg=1)

    SMART_AUTH = AuthenticationAttributes(ls=0, temp_number=1, temp_email=0)
    SMART_REG = RegisterAttributes(number=1, email=0, number_autoreg=1, email_autoreg=0)

    KEY_AUTH = AuthenticationAttributes(ls=0, temp_number=1, temp_email=1)
    KEY_REG = RegisterAttributes(number=1, email=1, number_autoreg=1, email_autoreg=1)

class TestObject:
    def __init__(self, auth, reg, link):
        self.auth_attr = auth
        self.reg_attr = reg
        self.link = link

testObjectMapper = {
    "ELK" : TestObject(Attributes.ELK_AUTH, Attributes.ELK_REG, "https://lk.rt.ru/"),
    "ONLINE" : TestObject(Attributes.ONLINE_AUTH, Attributes.ONLINE_REG, "https://my.rt.ru/"),
    "START" : TestObject(Attributes.START_AUTH, Attributes.START_REG, "https://start.rt.ru/"),
    "SMART" : TestObject(Attributes.SMART_AUTH, Attributes.SMART_REG, "https://lk.smarthome.rt.ru/"),
    "KEY" : TestObject(Attributes.KEY_AUTH, Attributes.KEY_REG, "https://key.rt.ru/main")
}