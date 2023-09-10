from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    if str(country_name) == str('Yemen, Rep.'):
        print(" yes   yes")
        return 'ye'
    for code, name in COUNTRIES.items():
        if country_name==name:
                return code

    return None


