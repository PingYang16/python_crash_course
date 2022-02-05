def build_car_info(manufacturer, model_name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info

car = build_car_info('subaru', 'outback', color = 'blue', location = 'Seattle', two_package = True)
print(car)