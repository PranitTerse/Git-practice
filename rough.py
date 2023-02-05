# from sympy import *
import numpy as np

def printsupress(nparray):
    np.set_printoptions(suppress=True,
    formatter={'float_kind':'{:f}'.format})

    print(nparray)
    

H = np.array([[1,1,0,1,0,0,0],[0,0,1,1,0,1,0],[0,0,0,1,1,0,1]])

# print("H_transpose = ",H.transpose(),)

# X = np.array([[0,1],[1,0]])
# Y = np.array([[0,-1j],[1j,0]])
# Z = np.array([[1,0],[0,-1]])
# print("\n",X,"\n",Y,"\n",Z)
# print(Y+Z)

# def commutator(x,y):
#     comm = x@y - y@x
#     return comm

# def anticommutator(x,y):
#     anticomm = x@y + y@x
#     return anticomm
# print(commutator(Z,X))
# print(anticommutator(Z,X))
########################################################################

R = "1111111"
C = "1110111"
t=theta=0.1
def log(x):
    log= -np.log(x)
    return log
x = np.empty([7,2])
for i in range(7):
    if R[i]=="0":
        x[i] = np.array([log(1-t),log(t)])
    else:
        x[i] = np.array([log(t),log(1-t)])

####################### 0,1 -> 013 #################
u0_013 = x[0]; u1_013 = x[1]


####################### 2,5 -> 235 #################
u5_235 = x[5]; u2_235 = x[2]


####################### 4,6 -> 346 #################
u6_346 = x[6]; u4_346 = x[4]

u013_3 = u235_3 = u346_3 = np.zeros(2)
u013_0 = u013_1 = u235_2 = u235_5 = u346_4 = u346_6 = np.zeros(2)
x3_final = np.zeros(2)
####################### 013 -> 3 #################
# u013_3= np.empty(2)
 
# for i3 in range(2):
#     store_sum = []
#     print("for x3=",i3)
#     for i0 in range(2):
#         for i1 in range(2):
#             if (i0+i1+i3)%2==0:
#                 sum= x[0][i0]+x[1][i1]
#                 store_sum.append(sum)
#     print("Min",store_sum," = ",min(store_sum))
#     u013_3[i3]=min(store_sum)

# print("013 -> 3 =",u013_3,"\n")

####################### 235 -> 3 #################
# u235_3= np.empty(2)

# for i3 in range(2):
#     store_sum = []
#     print("for x3=",i3)
#     for i5 in range(2):
#         for i2 in range(2):
#             if (i5+i2+i3)%2==0:
#                 sum= x[5][i5]+x[2][i2]
#                 store_sum.append(sum)
#     print("Min",store_sum," = ",min(store_sum))
#     u235_3[i3]=min(store_sum)

# print("235 -> 3 =",u235_3,"\n")

####################### 346 -> 3 #################
# u346_3= np.empty(2)
 
# for i3 in range(2):
#     store_sum = []
#     print("for x3=",i3)
#     for i6 in range(2):
#         for i4 in range(2):
#             if (i6+i4+i3)%2==0:
#                 sum= x[6][i6]+x[4][i4]
#                 store_sum.append(sum)
#     print("Min",store_sum," = ",min(store_sum))
#     u346_3[i3]=min(store_sum)

# print("346 -> 3 =",u346_3,"\n")

def first_pass(a,b):
    tar = np.empty(2)
    for i3 in range(2):
        store_sum = []
        # print("for x3=",i3)
        for i0 in range(2):
            for i1 in range(2):
                if (i0+i1+i3)%2==0:
                    sum= x[a][i0]+x[b][i1]
                    store_sum.append(sum)
        
        # print("Min",store_sum," = ",min(store_sum))
        tar[i3] = min(store_sum)
    # tar = tar - log(np.sum(tar))
    return tar

def final_pass(n):
    tar= np.empty(2)
    global x3_final
    x3_final = x[3] + u013_3 + u235_3 + u346_3
    # x3_final = x3_final - min(x3_final)

    for i0 in range(2):
        store_sum = []
        # print("for x0=",i0)
        for i3 in range(2):
            for i1 in range(2):
                if (i0+i1+i3)%2==0:
                    if n == 0:
                        sum= x[3][i3] + u235_3[i3] + u346_3[i3] +x[1][i1]
                    elif n == 1:
                        sum= x[3][i3] + u235_3[i3] + u346_3[i3] +x[0][i1]
                    elif n == 2:
                        sum= x[3][i3] + u013_3[i3] + u346_3[i3] +x[5][i1]
                    elif n == 5:
                        sum= x[3][i3] + u013_3[i3] + u346_3[i3] +x[2][i1]
                    elif n == 4:
                        sum= x[3][i3] + u013_3[i3] + u235_3[i3] +x[6][i1]
                    elif n == 6:
                        sum= x[3][i3] + u013_3[i3] + u235_3[i3] +x[4][i1]
                    store_sum.append(sum)
        # print("Min",store_sum)
        # print(min(store_sum))
        tar[i0]=min(store_sum)
    # tar = tar - log(np.sum(tar))
    return tar

def decoding():
    decoded_R = np.empty(7)
    x_final = np.empty([7,2])
    for i in range(7):
        if i==0:
            x_final[i] = x[i] + u013_0
            decoded_R[i] = np.argmin(x_final[i])
        elif i == 1:
            x_final[i] = x[i] + u013_1
            decoded_R[i] = np.argmin(x_final[i])
        elif i == 2:
            x_final[i] = x[i] + u235_2
            decoded_R[i] = np.argmin(x_final[i])
        elif i == 3:
            x_final[i] = x3_final
            decoded_R[i] = np.argmin(x_final[i])
        elif i == 5:
            x_final[i] = x[i] + u235_5
            decoded_R[i] = np.argmin(x_final[i])
        elif i == 4:
            x_final[i] = x[i] + u346_4
            decoded_R[i] = np.argmin(x_final[i])
        elif i == 6:
            x_final[i] = x[i] + u346_6
            decoded_R[i] = np.argmin(x_final[i])
    
    return(x_final,decoded_R)
    
for i in range(1):
    # print("Iteration {}".format(i+1))
    u013_3 =  first_pass(0,1) 
    print("013 -> 3 = ",u013_3,"\n")
    
    u235_3 =  first_pass(2,5)
    # print("235 -> 3 =",u235_3,"\n")
    u346_3 =  first_pass(4,6)
    # print("346 -> 3 =",u346_3,"\n")
    
    

    u013_0 =  final_pass(0)
    # print("013 -> 0 =",u013_0,"\n")
    u013_1 =  final_pass(1)
    # print("013 -> 1 =",u013_1,"\n")
    # print("3 ->013 = ", x3_final - u013_3)
    u235_2 =  final_pass(2)
    # print("235 -> 2 =",u235_2,"\n")
    u235_5 =  final_pass(5)
    # print("235 -> 5 =",u235_5,"\n")

    u346_4 =  final_pass(4)
    # print("346 -> 4 =",u346_4,"\n")
    u346_6 =  final_pass(6)
    # print("346 -> 6 =",u346_6,"\n")
    x_final, decoded_R = decoding()
    x = x_final
    


print("\n Final Costs =")
for i in range(7):
    print("x{} = ".format(i),x_final[i]) 
print("\n Original codeword = ",C)
print("\n Received codeword = ",R)
print("\n Decoded codeword:", decoded_R)

 
# ##################### 013 -> 0 ######################################
# u013_0= np.empty(2)
# for i0 in range(2):
#     store_sum = []
#     print("for x0=",i0)
#     for i3 in range(2):
#         for i1 in range(2):
#             if (i0+i1+i3)%2==0:
#                 sum= u3_013[i3]+x[1][i1]
#                 store_sum.append(sum)
#     print("Min",store_sum)
#     print(min(store_sum))
#     u013_0[i0]=min(store_sum)

# print("013 -> 0 =",u013_0)




