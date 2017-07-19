class LSystem:
    #axioms是所谓公理
    #rule则是用字典表示的规则，key就是原始字符，而值则用于替换。本系统暂时假定，key是单个字符
    def __init__(self, axiom, rules):
        m_sentence = axiom
        m_ruls = ruls
        m_genCount = 0
        
    def generate(self):
        sentence = []
        for ch in m_sentence:
            sentence.append(rules[ch])
    
        m_sentence = "".join(sentence)
        
        ++m_genCount
        
    def getSentence(self):
        return m_sentence
    
    def getGenCount(self):
        return m_genCount
    
 
class Turtle:
    def __init__(self, gen, ln, theta):
         m_gen = gen
         m_len = ln
         m_theta = theta
         
    def render(self):
        stroke(0, 175)
        for ch in gen:
            if (ch=="F"):
                line(0,0,m_len,0)
                translate(m_len, 0)
            elif (ch=="G"):
                translate(m_len, 0)
            elif (ch=="+"):
                rotate(m_theta)
            elif (ch=="-"):
                rotate(-m_theta)
            elif (ch=="["):
                pushMatrix()
            elif (ch=="]"):
                popMatrix()
            
    def setLen(self, ln):
        m_len=ln
    
    def changeLen(self, percent):
        m_len *= percent
    
    def setToDo(self, s):
        m_gen = s        