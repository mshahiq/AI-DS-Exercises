from matplotlib import pyplot as plt

def cube_intersection(cubeA_size,cubeA_x,cubeA_y,cubeA_z,cubeB_size,cubeB_x,cubeB_y,cubeB_z):
    Ax1 = cubeA_y - (cubeA_size/2) # coordinates A1(Ax1,Ay1,Az1), A2(Ax2,Ay2,Az2), A3(Ax3,Ay3,Az3), A4(Ax4,Ay4,Az4) 
    Ax3 = cubeA_y - (cubeA_size/2)

    Ay1 = cubeA_x - (cubeA_size/2)
    Ay2 = cubeA_x - (cubeA_size/2)

    Ax2 = cubeA_y + (cubeA_size/2)
    Ax4 = cubeA_y + (cubeA_size/2)

    Ay3 = cubeA_x + (cubeA_size/2)
    Ay4 = cubeA_x + (cubeA_size/2)

    Bx1 = cubeB_y - (cubeB_size/2)
    Bx3 = cubeB_y - (cubeB_size/2)

    By1 = cubeB_x - (cubeB_size/2)
    By2 = cubeB_x - (cubeB_size/2)

    Bx2 = cubeB_y + (cubeB_size/2)
    Bx4 = cubeB_y + (cubeB_size/2)

    By3 = cubeB_x + (cubeB_size/2)
    By4 = cubeB_x + (cubeB_size/2)

############################################### trying to solve for Z axis #############################################
    # A5 = cubeA_z
    # A6 = cubeA_z
    # A7 = cubeA_z
    # A8 = cubeA_z

    # B5 = cubeB_z
    # B6 = cubeB_z
    # B7 = cubeB_z
    # B8 = cubeB_z
########################################################################################################################

    # print(Ax1,Ay1," ",Ax2,Ay2," ",Ax3,Ay3," ",Ax4,Ay4)

    # print(Bx1,By1," ",Bx2,By2," ",Bx3,By3," ",Bx4,By4)


    cubeA_xcoordinates = [Ax1,Ax2,Ax4,Ax3,Ax1]
    cubeA_ycoordinates = [Ay1,Ay2,Ay4,Ay3,Ay1]

    cubeB_xcoordinates = [Bx1,Bx2,Bx4,Bx3,Bx1]
    cubeB_ycoordinates = [By1,By2,By4,By3,By1]





    if (Ax4>Bx1 and Ay4>By1) and (Bx4>Ax1 and By4>Ay1):
        # for my own help, sketched the graph
        plt.xlim(-40, 40)
        plt.ylim(-40, 40)
        plt.grid()
        plt.plot(cubeA_xcoordinates, cubeA_ycoordinates, marker="o", markersize=5,  markerfacecolor="red")
        plt.plot(cubeB_xcoordinates, cubeB_ycoordinates, marker="x", markersize=5,  markerfacecolor="blue")
        plt.show()
        return 1
    else:
        return 0



print(cube_intersection(5,10,10,0,2,9,9,0))



    