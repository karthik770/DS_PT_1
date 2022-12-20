

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="test1", Lastname="test", Age=22, Phone=1234567890)
intro(Firstname="test2", Lastname="test", Email="test@rrr.com", Country="india", Age=25, Phone=9234567899)
