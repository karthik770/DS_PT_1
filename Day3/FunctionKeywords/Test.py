test_data= ['1o','2o','4o','5o','6o','7o','8o','vip1','9o','12o','vip4','14o','15o','16o','vip5'] 

def find_vip(a):
    count=0
    for i in a:
        if ("vip" in i):
            count=count+1
            print(i,end="\n")
    print("Total VIP cards mixed with General ID is ",count)

find_vip(test_data)