import numpy as np
from flask import Flask, request, jsonify
import utils

app = Flask(__name__)


# def main():
#     np.random.seed(0)
#     print("Hello World!")
#
#     x1 = np.random.randint(10, size=6)
#     print("x3 ndim: ", x1.ndim)


@app.route("/get_location_names")
def get_location_names():
    print(utils.get_location_names())
    response = jsonify({"locations": utils.get_location_names()})
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/predict_property_price", methods=["POST"])
def predict_property_price():
    location = request.form["location"]
    plot_size = float(request.form["plot_size"])
    bedrooms = float(request.form["num_bedrooms"])
    bathrooms = float(request.form["num_bathrooms"])

    response = jsonify({"estimated_price": utils.get_estimate_price(location, plot_size, bedrooms, bathrooms)})
    response.headers.add("Access-Control-Allow-Origin", "* ")

    return response


if __name__ == "__main__":
    print("python server runing")
    print(utils.get_location_names())
    app.run()

print("Guru99")
