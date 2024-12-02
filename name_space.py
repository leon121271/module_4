def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()

#inner_function()  Если вывести функцию inner_function вне функции test_function - это вызовет ошибку т.к. inner_function
#                  является локальной для test_function и вне функции test_function Python ее не видит.