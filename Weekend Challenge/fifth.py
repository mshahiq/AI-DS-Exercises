# def find_Spy(nump,list_pairs): 

#     if nump<=0 or (len(list_pairs)>nump):
#         return -1   
#     for lp in list_pairs:
#         if (len(lp)!=2):
#             return -1
            
#     list_of_nonspies = []
#     for i in list_pairs:
#         list_of_nonspies.append(i[1])
#     chance_spies = {}
#     for i in list_pairs:
#         if i[0] not in list_of_nonspies:
#             chance_spies[i[0]] = chance_spies.get(i[0] , 0  ) +1

#     for key,values in chance_spies.items():
#         return key

# print(find_Spy(3,[[1, 2],[1, 3], [2,3]]))

class find_spy:

    def __init__(self,nump,list_of_pairs) -> None:
        self.nump = nump
        self.list_of_pairs = list_of_pairs

    def find_spy_in_pairs(self):

        if self.nump<=0 or (len(self.list_of_pairs)>self.nump):
            return -1   
        for lp in self.list_of_pairs:
            if (len(lp)!=2):
                return -1
            
        list_of_nonspies = []
        for i in self.list_of_pairs:
            list_of_nonspies.append(i[1])
        chance_spies = {}
        for i in self.list_of_pairs:
            if i[0] not in list_of_nonspies:
                chance_spies[i[0]] = chance_spies.get(i[0] , 0  ) +1

        for key,values in chance_spies.items():
            return key

detect_the_spy = find_spy(3,[['felix', 'lara'], ['felix', 'jeno'], ['lara', 'jeno']])

#detect_the_spy = find_spy(3,[['felix', 'lara'], ['lara', 'jeno'], ['lara', 'felix']])

print(detect_the_spy.find_spy_in_pairs())
