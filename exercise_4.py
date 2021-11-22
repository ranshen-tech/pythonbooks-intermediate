# 将整数100赋值给变量cars
cars =100
# 将字符串4.0赋值给变量space_in_a_car
space_in_a_car =4.0
# 将整数30赋值给变量drivers
drivers =30
# 将整数90赋值给变量passengers
passengers =90
# 将变量cars与变量drivers的值做差，将得到的数值赋值给变量cars_not_driven
cars_not_driven = cars - drivers
# 将变量drivers的值赋值给变量cars_driven
cars_driven = drivers
# 将变量cars_driven与变量space_in_a_car的值做积，将得到的值赋值给变量carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# 将变量passengers与变量cars_driven的值做商，将得到的值赋值给变量average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


print("there are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
