from num2words import num2words

ARE_TO_CENT = 2.471
DEPRECIATION_PER_YEAR = 0.02

def are_to_cent(are):
    return round(are * ARE_TO_CENT, 2)

def calculate_land_value(total_cents, rate_per_cent):
    return round(total_cents * rate_per_cent)

def calculate_depreciated_building_value(area_sqft, rate_sqft, age_years):
    gross = area_sqft * rate_sqft
    depreciation = age_years * DEPRECIATION_PER_YEAR
    return round(gross * (1 - depreciation))

def to_words(amount):
    return num2words(amount, lang="en_IN").title() + " Only"
