from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-", "."]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                if label == "C":
                    button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5},background_color=(3, 1, 0, 1))
                else:
                    button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color = (0, 1, 2, 1))
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color = (3, 1, 0, 1)
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Очистка виджета с решением
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                # Не добавляйте два оператора подряд, рядом друг с другом
                print('a')
                return
            elif current == "" and button_text in self.operators:
                print('c')
                # Первый символ не может быть оператором
                return
            else:
                # Очистка виджета с решением
                new_text = current + button_text
                self.solution.text = new_text
                print(current)
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            while text[-1] in ('+', '-', '/', '*'):
                print(text)
                return
            while text[-2:] in ('+.', '-.', '/.', '*.', '/0'):
                print(text[-2:])
                self.solution.text = 'FUCK YOY!!!'
                return
            # if text[-1] == '+' or text[-1] == '-' or text[-1] == '/' or text[-1] == '*':
            # while text[-2:] in ('.+', '.-', './', '.*'):
            #     print(text[-2:])
            #     self.solution.text = "Error"
            #     return
            if text == 'FUCK YOY!!!':
                self.solution.text = ""
                return
            solution = str(eval(self.solution.text))
            print(solution)
            self.solution.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()
