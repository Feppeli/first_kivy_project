# A aplicação será rodada no fim do arquivo. as demais classe serão de importante contrução da aplicação.
# importando algumas propriedades
from kivy.uix.screenmanager import Screen, ScreenManager # telas e gerenciador de telas
from kivy.app import App #importando a estrutura de app do Kivy
from kivy.lang import Builder

# Classe do Gerenciador das telas
class GerenciarTelas(ScreenManager):
    pass

# Telas
class TelaMenu(Screen):
    pass

class TelaGame(Screen):
    pass

class TelaGameOver(Screen):
    pass


# Aplicação
class MyApp(App): #Criando a classe do kivy
    def build(self):
        return Builder.load_file('myapp.kv')
MyApp().run() #Rodando aplicação