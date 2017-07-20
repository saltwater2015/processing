class Mover:
    MAX_VEL = 10
    def __init__(self, pos, vel, acc):
        self.loc = loc #位置向量
        self.vel = vel #速度向量
        self.acc = acc #加速度向量
        
    def update():
        if ((self.loc.x > width) or (self.loc.x < 0)):
            
            self.vel.x = self.vel.x * -1;
        if ((self.loc.y > height) or (self.loc.y < 0)):
            self.vel.y = self.vel.y * -1;

        self.vel.add(self.acc)
        self.vel.limit(MAX_VEL) 
        self.loc.add(self.vol)
   
    def display():
        stroke(8)
        fill(75)
        ellipse(self.loc.x, self.loc.y, 16,16)
 
global b1
global b2               

def setup():
    global b1
    global b2
    size(500,500)
    background(255)
    b1 = Mover(PVector(150,150), PVector(0.1, 0), PVector(0.1,0.1))
    b2 = Mover(PVector(100,100), PVector(0.1, 0.1), PVector(0.5,0.1))

    
    
def draw():
    global b1
    global b2

    b1.update()    
    b2.update()
    
    b1.display()
    b2.display()