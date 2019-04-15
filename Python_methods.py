unsorted = [1,6,0,9,32,3,4]

stringed_list = map(str, unsorted)
print("\nlist string --->", list(stringed_list))

def squared(x):
    return pow(x,2)

#square_map = map(squared,unsorted)
square_map = map(squared,unsorted)
print("\n Squared list ---->", list(square_map))

list_for_join = ['1','6','0','32','3','4']
joined  = "".join(list_for_join)
print("\n joined list string --->", joined)
