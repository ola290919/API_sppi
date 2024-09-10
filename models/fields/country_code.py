import random

import pycountry
from pydantic import RootModel, Field, field_validator


class CountryCode(RootModel):
    root: str = Field(...)

    @field_validator('root')
    def validate(cls, value) -> str:
        if not isinstance(value, str):
            raise ValueError(f'Country Code must be a string')

        # Check if the country code is valid (either 2 or 3 letters)
        if len(value) not in (2, 3):
            raise ValueError(f'Country Code code must be 2 or 3 letters long')

        # Validate using pycountry
        try:
            country = None
            if len(value) == 2:
                country = pycountry.countries.get(alpha_2=value)
            elif len(value) == 3:
                country = pycountry.countries.get(alpha_3=value)

            if not country:
                raise ValueError(f'County Code is not a valid country code')
        except Exception as e:
            raise ValueError(f'County Code got error validating country code: {e}')

        return value

    @classmethod
    def random(cls):
        # Get the list of countries
        countries = list(pycountry.countries)
        # Choose a random country
        country = random.choice(countries)
        # Randomly decide between alpha_2 or alpha_3 code
        return cls(country.alpha_2 if random.choice([True, False]) else country.alpha_3)
