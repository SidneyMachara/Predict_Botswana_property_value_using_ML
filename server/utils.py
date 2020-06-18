import json
import numpy as np
import pickle

__locations = None
__data_columns = None
__model = None


def get_estimate_price(location, plot_size, num_bedrooms, num_bathrooms):
    try:
        location_index = __data_columns.index(location.lower())
    except:
        location_index = -1

    _x = np.zeros(len(__data_columns))
    _x[0] = num_bedrooms
    _x[1] = num_bathrooms
    _x[2] = plot_size
    if location_index >= 0:
        _x[location_index] = 1

    return round(__model.predict([_x])[0], 2)


def get_location_names():
    load_saved_artifacts()
    return __locations


def load_saved_artifacts():
    print("--> load_saved_artifacts()")

    global __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[4:]

    global __model
    with open("./artifacts/Botswana_property_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("DONE --> load_saved_artifacts()")


if __name__ == "__main__":
    load_saved_artifacts()
    # print(get_location_names())
    # print(get_estimate_price("block 10", 1000, 2, 2))
