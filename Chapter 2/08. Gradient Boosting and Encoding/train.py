import data_handler as dh

x_train, x_test, y_train, y_test = dh.get_data("./insurance.csv")

print(dh.hello)
print(len(x_train))
print(len(y_train))