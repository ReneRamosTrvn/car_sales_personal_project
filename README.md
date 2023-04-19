# car_sales_personal_project
This was just a quick and fun project to improve my skills on pandas, ETL, EDA and API

You can go straight to the docs with this link :)
https://car-sales-tybm.onrender.com/docs

We only have 3 functions you can get data from:

/get_cheapest_car/manufacturer

    """
    This function will give you the cheapest car (no truck/suv) available from selected manufacture.

    Parameters:
    manufacture (str): A manufacture brand of choice (chevrolet, acura, ford, etc)

    Returns:
    A dictionary with keys "Model" and "Price" and their respective values.
    """

get_faster_car/model/horsepower

    """
    This function will give you a dictionary of the top 5 faster cars (no truck/suv)
    than the one you have. We are going to use the horsepower in case your model
    isn't in our database.

    Parameters:
    model (str): The model of your car (camaro, mustang, s40, etc).
    horsepower (int): The quantity of horsepower your car has (320, 118, 230).

    This will return a dictionary with the model and horsepower of 5 cars that are faster
    """
    
get_top_sold/manufacturer

    """
    This function will give you the top 5 most sold cars, trucks or SUVs by a manufacturer.

    Parameters:
    manufacture (str): A manufacturer brand of choice (chevrolet, acura, ford, etc)

    Returns:
    A dictionary with the top 5 sold cars, trucks, SUVs.
    """
    
Technologies used:
-Python
  -Pandas
  -Uvicorn
  -FastAPI
 
 Hosting:
  -Render
