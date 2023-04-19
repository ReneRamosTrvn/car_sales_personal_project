import pandas as pd
from fastapi import FastAPI

app = FastAPI()
df = pd.read_csv('./clean_car_sales.csv')


@app.get("/")
async def root():
    return {"message": "Welcome to my personal proyect :), go to /docs to see all things you can do."}


@app.get("/get_cheapest_car/{manufacture}")
def get_cheapest_car(manufacturer: str):
    """
    This function will give you the cheapest car (no truck/suv) available from selected manufacture.

    Parameters:
    manufacture (str): A manufacture brand of choice (chevrolet, acura, ford, etc)

    Returns:
    A dictionary with keys "Model" and "Price" and their respective values.
    """
    df_man = df[(df['manufacturer'] == manufacturer)
                & (df['vehicle_type'] == 'car')]
    idx = df_man['price_in_thousands'].idxmin()
    car_model = df_man.loc[idx, 'model']
    car_price = df_man.loc[idx, 'price_in_thousands']
    return {"Model": car_model, "Price": car_price}


@app.get("/get_faster_car/{model}/{horsepower}")
def get_faster_car(model: str, horsepower: int):
    """
    This function will give you a dictionary of the top 5 faster cars (no truck/suv)
    than the one you have. We are going to use the horsepower in case your model
    isn't in our database.

    Parameters:
    model (str): The model of your car (camaro, mustang, s40, etc).
    horsepower (int): The quantity of horsepower your car has (320, 118, 230).

    This will return a dictionary with the model and horsepower of 5 cars that are faster
    """

    try:
        your_car = df[df['model'] == model].iloc[0]
    except IndexError:
        your_car = {'horsepower': horsepower}

    faster_cars = df[(df['vehicle_type'] == 'car') & (
        df['horsepower'] > your_car['horsepower'])].head(5)[['model', 'horsepower']]

    return faster_cars.to_dict('records')


@app.get("/get_top_sold/{manufacture}")
def get_top_sold(manufacturer: str):
    """
    This function will give you the top 5 most sold cars, trucks or SUVs by a manufacturer.

    Parameters:
    manufacture (str): A manufacturer brand of choice (chevrolet, acura, ford, etc)

    Returns:
    A dictionary with the top 5 sold cars, trucks, SUVs.
    """

    top_5_cars = df[(df['manufacturer'] == manufacturer)].sort_values(
        'sales_in_thousands', ascending=False).head(5)[['model', 'sales_in_thousands']]

    return top_5_cars.to_dict('records')
