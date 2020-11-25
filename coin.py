class Coin:
    def __init__(self,rare = False):

        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00
        
        self.color = "gold"
        self.num_edges = 1.00
        self.diameter  = 1.00
        self.thickness = 1.00
        self.heads = True

        

    def rust(self):
        self.color = "greenish"