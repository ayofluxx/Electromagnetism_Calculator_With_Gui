import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

pe = 4 * math.pi * math.pow(10, -7)
k = math.pow(8.9875 * 10, 9)

class MagnetismCalculator:
    def Coulombs_law(self, q1, q2, r):
        F = k * (q1 * q2) / (r * r)
        return F

    def Electric_Field(self, F, q):
        E = F / q
        return E

    def Electric_Potential_Energy(self, q1, q2, r):
        U = k * (q1 * q2) / r
        return U

    def Electric_Potential(self, q, r):
        V = k * (q / r)
        return V

    def Ohm_law(self, I, R):
        V = I * R
        return V

    def MF_moving_charge(self, q, v, B):
        F = q * v * B
        return F

class MagnetismApp(App):
    def build(self):
        self.calculator = MagnetismCalculator()
        layout = BoxLayout(orientation='vertical')

        # Coulomb's Law input fields and button
        self.q1c_input = TextInput(hint_text='Enter q1', multiline=False)
        self.q2c_input = TextInput(hint_text='Enter q2', multiline=False)
        self.rc_input = TextInput(hint_text='Enter r', multiline=False)
        self.coulombs_button = Button(text="Calculate Coulomb's Law")
        self.coulombs_button.bind(on_press=self.calculate_coulombs_law)
        self.coulombs_result_label = Label(text='Result will be displayed here')

        layout.add_widget(self.q1c_input)
        layout.add_widget(self.q2c_input)
        layout.add_widget(self.rc_input)
        layout.add_widget(self.coulombs_button)
        layout.add_widget(self.coulombs_result_label)

        # Electric Field input fields and button
        self.Ff_input = TextInput(hint_text='Enter F', multiline=False)
        self.qf_input = TextInput(hint_text='Enter q', multiline=False)
        self.electric_field_button = Button(text='Calculate Electric Field')
        self.electric_field_button.bind(on_press=self.calculate_electric_field)
        self.electric_field_result_label = Label(text='Electric Field result will be displayed here')

        layout.add_widget(self.Ff_input)
        layout.add_widget(self.qf_input)
        layout.add_widget(self.electric_field_button)
        layout.add_widget(self.electric_field_result_label)

        # Electric Potential energy input fields and button
        self.q1pe_input = TextInput(hint_text='Enter q1', multiline=False)
        self.q2pe_input = TextInput(hint_text='Enter q2', multiline=False)
        self.rpe_input = TextInput(hint_text='Enter r', multiline=False)
        self.electric_potential_energy_button = Button(text='Calculate Electric Potential Energy')
        self.electric_potential_energy_button.bind(on_press=self.calculate_electric_potential_energy)
        self.electric_potential_energy_result_label = Label(text='Electric Potential Energy result will be displayed here')

        layout.add_widget(self.q1pe_input)
        layout.add_widget(self.q2pe_input)
        layout.add_widget(self.rpe_input)
        layout.add_widget(self.electric_potential_energy_button)
        layout.add_widget(self.electric_potential_energy_result_label)

        # Electric Potential input fields and button
        self.qp_input = TextInput(hint_text='Enter q', multiline=False)
        self.rp_input = TextInput(hint_text='Enter r', multiline=False)
        self.electric_potential_button = Button(text='Calculate Electric Potential')
        self.electric_potential_button.bind(on_press=self.calculate_electric_potential)
        self.electric_potential_result_label = Label(text='Electric Potential result will be displayed here')

        layout.add_widget(self.qp_input)
        layout.add_widget(self.rp_input)
        layout.add_widget(self.electric_potential_button)
        layout.add_widget(self.electric_potential_result_label)

        # Ohm's Law input fields and button
        self.Io_input = TextInput(hint_text='Enter I', multiline=False)
        self.Ro_input = TextInput(hint_text='Enter R', multiline=False)
        self.ohms_law_button = Button(text='Calculate Voltage')
        self.ohms_law_button.bind(on_press=self.calculate_ohm_law_voltage)
        self.ohms_law_result_label = Label(text='Voltage result will be displayed here')

        layout.add_widget(self.Io_input)
        layout.add_widget(self.Ro_input)
        layout.add_widget(self.ohms_law_button)
        layout.add_widget(self.ohms_law_result_label)

        # Magnetic Force on Moving Charge input fields and button
        self.qm_input = TextInput(hint_text='Enter q', multiline=False)
        self.vm_input = TextInput(hint_text='Enter v', multiline=False)
        self.Bm_input = TextInput(hint_text='Enter B', multiline=False)
        self.MF_moving_charge_button = Button(text='Calculate Magnetic Force')
        self.MF_moving_charge_button.bind(on_press=self.calculate_mf_moving_charge)
        self.MF_moving_charge_result_label = Label(text='Magnetic Force result will be displayed here')

        layout.add_widget(self.qm_input)
        layout.add_widget(self.vm_input)
        layout.add_widget(self.Bm_input)
        layout.add_widget(self.MF_moving_charge_button)
        layout.add_widget(self.MF_moving_charge_result_label)

        return layout

    def calculate_coulombs_law(self, instance):
        q1 = float(self.q1c_input.text)
        q2 = float(self.q2c_input.text)
        r = float(self.rc_input.text)
        result = self.calculator.Coulombs_law(q1, q2, r)
        self.coulombs_result_label.text = f'Result: {result}'

    def calculate_electric_field(self, instance):
        F = float(self.Ff_input.text)
        q = float(self.qf_input.text)
        result = self.calculator.Electric_Field(F, q)
        self.electric_field_result_label.text = f'Result: {result}'

    def calculate_electric_potential_energy(self, instance):
        q1 = float(self.q1pe_input.text)
        q2 = float(self.q2pe_input.text)
        r = float(self.rpe_input.text)
        result = self.calculator.Electric_Potential_Energy(q1, q2, r)
        self.electric_potential_energy_result_label.text = f'Result: {result}'

    def calculate_electric_potential(self, instance):
        q = float(self.qp_input.text)
        r = float(self.rp_input.text)
        result = self.calculator.Electric_Potential(q, r)
        self.electric_potential_result_label.text = f'Result: {result}'

    def calculate_ohm_law_voltage(self, instance):
        I = float(self.Io_input.text)
        R = float(self.Ro_input.text)
        result = self.calculator.Ohm_law(I, R)
        self.ohms_law_result_label.text = f'Result: {result}'

    def calculate_mf_moving_charge(self, instance):
        q = float(self.qm_input.text)
        v = float(self.vm_input.text)
        B = float(self.Bm_input.text)
        result = self.calculator.MF_moving_charge(q, v, B)
        self.MF_moving_charge_result_label.text = f'Result: {result}'

if __name__ == '__main__':
    MagnetismApp().run()
