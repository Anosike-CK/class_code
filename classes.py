
class Animal:

    heart = 1
    stomach = 1

    def __init__(self, legs, hands, eyes):

        self.legs = legs
        self.hands = hands
        self.eyes = eyes

me = "tami"
me_list = ['t','a','m','i']
reversed_me = list(reversed(me))
joined_list = ''.join(reversed_me)
print(me[:-1])
print(me[:-4:-1])
print(joined_list)
print(me_list[1] + me_list[3])
# me_added = 
joined_list = 'erol'+ joined_list 
print(joined_list)
print(joined_list[::-1])