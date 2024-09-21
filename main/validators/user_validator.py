from collections import defaultdict
import re
from django.core.exceptions import ValidationError

class CreateUserValidator:
    def __init__(self, data, erros=None) -> None:
        self.erros = defaultdict(list)
        self.data = data
        self.clean()
        
    def clean(self):    
        self.clean_first_name()
        self.clean_document()
        self.clean_phone_number()
        self.clean_street()
        self.clean_number()
        self.clean_district()
        self.clean_city()
        self.clean_state()
        self.clean_zip_code()
        self.clean_password()

        if self.erros:
            raise ValidationError(self.erros)


    def clean_first_name(self):
        value = self.data.get('first_name')
        reg_string = r'^[a-zA-Z0-9._]{3,20}$'
        if not re.match(reg_string, value):
            self.erros['first_name'].append('O primeiro nome precisa atender aos requerimentos')
        return value
       
    def clean_document(self):
        cpf = self.data.get('document')
        reg_string = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
        if not re.match(reg_string, str(cpf)):
            self.erros['document'].append(f'CPF {cpf} é inválido, tente novamente com um documento ')

    def clean_phone_number(self):
        pn = self.data.get('phone_number')
        reg_string = r'^.{1,15}$'
        if not re.match(reg_string, pn):
            self.erros['phone_number'].append(f'Número de telefone {pn} inválido!')

    def clean_street(self):
        street = self.data.get('street')
        if not street or len(street) < 3:
            self.erros['street'].append('O nome da rua deve ter pelo menos 3 caracteres.')
        return street

    def clean_number(self):
        number = self.data.get('number')
        if not number.isdigit():
            self.erros['number'].append('O número deve ser um valor numérico.')
        return number

    def clean_district(self):
        district = self.data.get('district')
        if not district or len(district) < 3:
            self.erros['district'].append('O nome do distrito deve ter pelo menos 3 caracteres.')
        return district

    def clean_city(self):
        city = self.data.get('city')
        if not city or len(city) < 3:
            self.erros['city'].append('O nome da cidade deve ter pelo menos 3 caracteres.')
        return city

    def clean_state(self):
        state = self.data.get('state')
        reg_string = r'^[A-Z]{2}$'  # Exemplo para siglas de estados
        if not re.match(reg_string, state):
            self.erros['state'].append('O estado deve ser uma sigla válida de 2 letras.')
        return state

    def clean_zip_code(self):
        zip_code = self.data.get('zip_code')
        reg_string = r'^\d{5}-\d{3}$'  # Formato brasileiro de CEP
        if not re.match(reg_string, zip_code):
            self.erros['zip_code'].append('O CEP deve estar no formato XXXXX-XXX.')
        return zip_code

    def clean_password(self):
        password = self.data.get('password')
        if len(password) < 8:
            self.erros['password'].append('A senha deve ter pelo menos 8 caracteres.')
        return password            
        