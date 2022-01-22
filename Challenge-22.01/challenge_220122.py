def find_spy(np, list_pairs):
    for pd in list_pairs:

        if (np <= 0) or (len(list_pairs) > np) or (len(pd)!=2):
            return print("-1")

        else:
            # #print(list_pairs)
            # for pd in list_pairs:

            # for sin_num in list(pd):
            #     return print(sin_num)

            # first = pd[0]
            # second = pd[1]
            # print(first,second)

            if pd[0]<pd[1]:
                print(pd[0])
            else:
                print(pd[1])

            

find_spy(3,([[1, 2], [1, 3], [2, 3]]))