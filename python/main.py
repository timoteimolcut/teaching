# # def fun(a,b):
# #     for i in range(a,b):
# #         print (i)
# # a = 10
# # b = 20
# # fun(a,b)



# def fun (c,d,e,g):
#     for i in range(c*2):
        # f = (i**d/e)
        # if f == g:
#             print("result:",i,f)
#             break 
#         else: 
#             print("test:",i,f)
#     # if g==f:
#     #     for i in range(c,g):
#     #         print(i)
#     # else: print(f)




# c = 50
# d = 3
# e = 2
# g = 10976
# fun(c,d,e,g)










amount_owed = 28000
max_month = 130

def fun (max_month,amout_owed):
    for i in range(max_month):
        month_pay = 428
        formula1 = i*month_pay
        formula2 = (i+1)*month_pay
        if formula1 <= amount_owed and amount_owed <= formula2:
            print("result:",i//12,i%12,formula1,formula2-amount_owed)
            break
        else:
            print("test:",i//12,i%12,formula1)

fun (max_month,amount_owed)





# a = 1
# b = 3
# if a<b:
#     print("ok")
# else:
#     print("not ok")
#     for i in range(10):
#         print(i)






