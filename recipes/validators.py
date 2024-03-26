import pint
from django.core.exceptions import ValidationError
from pint.errors import UndefinedUnitError

valid_unit_measurements = ['pounds', 'oz', 'lbs', 'gram']



def validate_unit_of_measure(value):
    ureg = pint.UnitRegistry()
    try:
        ureg[value]
    except UndefinedUnitError:
        raise ValidationError(
            f"{value} is not a valid unit of measure"
        )
    except:
        raise ValidationError(
                f"{value} is invalid. Unknow error"
            ) 
    # if value not in valid_unit_measurements: