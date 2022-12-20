
def find_vip(test_data):
    for i in test_data:
        if ("vip" in i):
            yield i

test_data= ['1o','2o','4o','5o','6o','7o','8o','vip1','9o','12o','vip4','14o','15o','16o','vip5'] 
count = 0
print("The number of vip card is : ", end="")

for j in find_vip(test_data):
    count = count + 1
print(count)
