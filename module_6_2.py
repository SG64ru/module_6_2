class Vehile:
    _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, onwer, _model, _color,_engin_power ):
        self.onwer = onwer
        self._model = _model
        self._engin_power = _engin_power
        self._color = _color


    def get_model(self):
        return f"Модель: {self._model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self._engin_power}"

    def get_color(self):
        return f" Цвет: {self._color.upper()}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.onwer}")

    def set_color(self, new_color): #Замена цвета

        if new_color.lower() in self._COLOR_VARIANTS:
            self._color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehile):
    _PASSEGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()

