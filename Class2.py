from Class3 import Verification

class V2(Verification):

    def __init__(self, login, password):
        Verification.__init__(self, login, password)
        self.__save()

    def __save(self):
        with open('user') as r:
            for i in r:
                if f'{self.login, self.password}'+'\n' == i:
                    raise ValueError ('Логин и пароль существует')
        Verification.save(self)

    def show(self):
        return self.login, self.password


x = V2('username1', 'qwerty1234')
x.save()