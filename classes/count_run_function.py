class CallsCounter:
    def __init__(self):
        self.counter = 0

    def quantity_of_calls(self):
        self.counter += 1
        return self.counter


calling = CallsCounter()

print('Quantity of calls: ' + str(calling.quantity_of_calls()))
print('Quantity of calls: ' + str(calling.quantity_of_calls()))
print('Quantity of calls: ' + str(calling.quantity_of_calls()))
print('Quantity of calls: ' + str(calling.quantity_of_calls()))
print('Quantity of calls: ' + str(calling.quantity_of_calls()))
