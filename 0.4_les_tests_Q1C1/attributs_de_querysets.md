# Attributs de Querysets

```python
#######################################################################################################################

"""
ATTIBUTS QUERYSETS PYTHON DE BASE

'__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__',
'__subclasshook__', '__weakref__',
"""

#######################################################################################################################

"""
ATTRIBUTS DU QUERYSET AGENCY

'establishment', 'establishment_id', 'establishments', 'establishments_history', 'establishments_set', 'from_db',
'full_clean', 'get_deferred_fields', 'hr_assistant', 'hr_responsible', 'id', 'import_errors', 'main_agency',
'main_agency_id', 'managers', 'metropolis', 'metropolis_id', 'name', 'objects', 'payroll_manager',
'payroll_start_date', 'payslips', 'pk', 'prepare_database_save', 'refresh_from_db', 'save', 'save_base',
'serializable_value', 'situations', 'unique_error_message', 'validate_unique'
"""

#######################################################################################################################

"""
ATTRIBUTS DU QUERYSET AGENCY.ESTABLISHMENTS

'_state', 'address', 'agencies', 'agencies_history', 'agency', 'agency_at_date', 'cedex_box', 'cedex_value',
'cedex_zip', 'check', 'city', 'clean', 'clean_fields', 'company', 'company_id', 'coordinates', 'coordinates_origin',
'country', 'date_error_message', 'delete', 'end_date', 'from_db', 'full_address', 'full_address_fields',
'full_cedex_address_fields', 'full_clean', 'geolocate', 'get_coordinates_origin_display', 'get_deferred_fields',
'get_distance_between', 'get_distance_with', 'get_next_by_start_date', 'get_previous_by_start_date', 'id',
'is_active', 'is_main', 'latitude', 'longitude', 'nic', 'objects', 'payroll_start_date', 'payslips', 'pk',
'prepare_database_save', 'refresh_from_db', 'residence_or_street', 'save', 'save_base', 'serializable_value',
'short_address', 'siren', 'siret', 'start_date', 'street1', 'street2', 'trade_name', 'unique_error_message',
'validate_unique', 'zip'
"""

#######################################################################################################################

"""
ATTRIBUTS DU QUERYSET USER

bic, birth_city, birth_country, birth_country_id, birth_date, birth_department, birth_name, city, country, country_id,
creation_date, deletion_date, dependents_count, firstname, gender, gender_id, iban, id, import_errors,
import_errors_hr_assistant, import_errors_hr_responsible, lastname, ldap_account, marital_status, marital_status_id,
modification_date, most_current_situation, most_current_situation_id, nationality, nationality_id, payslips,
situations, social_security_number, street1, street2, street3, tutor, tutor_for, tutor_id, zip
"""

#######################################################################################################################

"""
ATTRIBUTS DU QUERYSET DES USERS PARISIENS

{'id': '0014089', 'gender_id': 'M', 'firstname': 'Matthieu', 'lastname': 'Pena', 'birth_name': 'Pena',
'birth_date': datetime.date(1986, 11, 4), 'birth_city': 'BAYONNE', 'birth_department': '64',
'birth_country_id': None, 'nationality_id': 'F', 'social_security_number': '186116410203117',
'marital_status_id': None, 'dependents_count': 0, 'street1': '44  RUE DE VERGENNES', 'street2': None,
'street3': None, 'zip': '78000', 'city': 'VERSAILLES', 'country_id': 'FR', 'iban': 'FR7630003022270005118289884',
'bic': 'SOGEFRPP', 'most_current_situation_id': 45565, 'tutor_id': None,
'creation_date': datetime.datetime(2021, 7, 8, 21, 5, 34, 545001, tzinfo=<UTC>),
'modification_date': datetime.datetime(2021, 11, 4, 18, 6, 54, 62946, tzinfo=<UTC>), 'deletion_date': None}
"""
```