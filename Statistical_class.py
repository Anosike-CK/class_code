class Statistics:

    def __init__(self, x,y):

        self.x = x
        self.y = y
    
    def mean(self):

        return [sum(self.x)/len(self.x), sum(self.y)/len(self.y)]
        

    def list_meanbar(self):

        mean_bars = self.mean()
        x_bar = mean_bars[0]
        y_bar = mean_bars[1]

        x_xbar = [x - x_bar for x in self.x]
        y_ybar = [y - y_bar for y in self.y]

        return [x_xbar, y_ybar]
        
    def mean_deviation(self):

        list_bars = self.list_meanbar()
        x_xbar = list_bars[0]
        y_ybar = list_bars[1]

        mean_deviated_x = sum(x_xbar)/len(x_xbar)
        mean_deviated_y = sum(y_ybar)/len(y_ybar)

        print('x'.center(13), 'y'.center(10), 'x_xbar'.center(10), 'y_ybar'.center(10))

        for i in zip(self.x, self.y, self.list_meanbar()[0],self.list_meanbar()[1]):
            print(str(i[0]).center(13), str(i[1]).center(10), str(i[2]).center(10), str(i[3]).center(10))
        print(f'mean deviation of x = {mean_deviated_x}, mean deviation of y = {mean_deviated_y}')

             
            

x = [x for x in range(20)]
y = [1,5,10,2,5,6,7,2,9,5,9,3,4,30,20,14,13,25,17,12]

# print(x)
Stat = Statistics(x,y)
# Stat.list_meanbar()
Stat.mean_deviation()
# import ast 

# def test(x):
#     x = ast.literal_eval(x) 
#     print(x)

# x = input("enter value : ")

# test(x)
        