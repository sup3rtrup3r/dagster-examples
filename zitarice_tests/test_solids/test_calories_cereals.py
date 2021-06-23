# from dagster import execute_solid
# from zitarice.solids.caloriest_cereals import find_highest_calorie_cereal
# from zitarice.solids.download_cereals_csv import download_cereals
#
#
# def test_find_highest_calorie_cereal_solid():
#     cereals = execute_solid(download_cereals)
#     res = execute_solid(find_highest_calorie_cereal(cereals))
#     assert res.success
#     assert str(res.output_value()) == "Strawberry Fruit Wheats"
