import re
from django.core.exceptions import ValidationError as DjangoValidationError

class CreateUserValidator:
    def __init__(self, data, class_error: type = DjangoValidationError) -> None:
        self.data = data
        self.ValidationError = class_error
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

    def clean_first_name(self):
        value = self.data.get('first_name')
        reg_string = r'^.{3,30}$'
        if not re.match(reg_string, value):
            raise self.ValidationError('O primeiro nome precisa atender aos requerimentos')

    def clean_document(self):
        cpf = self.data.get('document')
        clean_cpf = re.sub(r'\D', '', str(cpf))
        if len(clean_cpf) != 11:
            raise self.ValidationError(f'CPF {cpf} deve ter exatamente 11 dígitos numéricos.')


    def clean_phone_number(self):
        pn = self.data.get('phone_number')
        reg_string = r'^.{1,15}$'
        if not re.match(reg_string, pn):
            raise self.ValidationError(f'Número de telefone {pn} inválido!')

    def clean_street(self):
        street = self.data.get('street')
        if not street or len(street) < 3:
            raise self.ValidationError('O nome da rua deve ter pelo menos 3 caracteres.')

    def clean_number(self):
        number = self.data.get('number')
        if not number.isdigit():
            raise self.ValidationError('O número deve ser um valor numérico.')

    def clean_district(self):
        district = self.data.get('district')
        if not district or len(district) < 3:
            raise self.ValidationError('O nome do distrito deve ter pelo menos 3 caracteres.')

    def clean_city(self):
        city = self.data.get('city')
        if not city or len(city) < 3:
            raise self.ValidationError('O nome da cidade deve ter pelo menos 3 caracteres.')

    def clean_state(self):
        state = self.data.get('state')
        reg_string = r'^[A-Z]{2}$'  # Exemplo para siglas de estados
        if not re.match(reg_string, state):
            raise self.ValidationError('O estado deve ser uma sigla válida de 2 letras.')

    def clean_zip_code(self):
        zip_code = self.data.get('zip_code')
        clean_zip = re.sub(r'\D', '', zip_code) # pop numerics caracteres
        if len(clean_zip) != 8:  
            raise self.ValidationError('O CEP deve ter exatamente 8 dígitos numéricos.')

    def clean_password(self):
        password = self.data.get('password')
        if len(password) < 8:
            raise self.ValidationError('A senha deve ter pelo menos 8 caracteres.')
