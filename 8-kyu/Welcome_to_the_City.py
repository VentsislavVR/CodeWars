def say_hello(name, city, state):
    full_name = ' '.join(name)
    welcome_message = f"Hello, {full_name}! Welcome to {city}, {state}!"
    return welcome_message


input_name = ['John', 'Smith']
input_city = 'Phoenix'
input_state = 'Arizona'
result = say_hello(input_name, input_city, input_state)
print(result)




