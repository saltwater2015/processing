class LSystem:
    #axioms是所谓公理
    #rule则是用字典表示的规则，
    #key就是原始字符，而值则用于替换。
    #本系统暂时假定，key是单个字符
    def __init__(self, axiom, rules):
        self.m_sentence = axiom
        self.m_rules = rules
        self.m_genCount = 0
            
    def getSentence(self):
        return self.m_sentence
    
    def getGenCount(self):
        return self.m_genCount
    
    def generate(self):
        sentence = []
        for ch in self.m_sentence:
            if ch in self.m_rules:
                sentence.append(self.m_rules[ch])
            else:
                sentence.append(ch)
    
        self.m_sentence = "".join(sentence)        
        ++self.m_genCount
 
 
class Turtle:
    def __init__(self, gen, ln, theta):
         self.m_gen = gen
         self.m_len = ln
         self.m_theta = theta
         
    def render(self):
        stroke(0, 175)
        for ch in self.m_gen:
            if (ch=="F"):
                line(0,0,self.m_len,0)
                translate(self.m_len, 0)
            elif (ch=="G"):
                translate(self.m_len, 0)
            elif (ch=="+"):
                rotate(self.m_theta)
            elif (ch=="-"):
                rotate(-self.m_theta)
            elif (ch=="["):
                pushMatrix()
            elif (ch=="]"):
                popMatrix()
            
    def setLen(self, ln):
        self.m_len=ln
    
    def changeLen(self, percent):
        self.m_len *= percent
    
    def setToDo(self, s):
        self.m_gen = s        
        

global lsys
global turtle

def setup():
    global lsys
    global turtle
    
    rules={}
    rules["F"]="FF+[+F-F-F]-[-F+F+F]"
    
    lsys = LSystem("F", rules)
    turtle = Turtle(lsys.getSentence(), height/3, radians(25))
 
    size(600, 600)
    background(255)
    translate(width/2, height)
    rotate(-PI/2)
    turtle.render()

def draw():
    global lsys
    global turtle
    if (mousePressed==True):
        pushMatrix()
        lsys.generate()
        turtle.setToDo(lsys.getSentence())
        turtle.changeLen(0.5)
        translate(width/2, height);
        rotate(-PI/2);
        turtle.render();
        popMatrix()
        
        
        
    

    
    
    