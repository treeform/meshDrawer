"""
    This example show how to use MeshDrawer to draw
    on the screen in any way shape or form you want
    
    The texture MeshDrawer takes is a plate of
    for instance plate of 3 x 3 will be numberd 
    this way:
     
    1 2 3  
    4 5 6
    7 8 9
    
    The plates are created by the create plate tool 

"""
import direct.directbase.DirectStart
from pandac.PandaModules import *
from random import *


maxParticles = 500 # max number of particle (1000) triangles we will display
by = 16 # we have a 16x16 plate texture

generator = MeshDrawer()
generator.setBudget(maxParticles)
generator.setPlateSize(by)
generatorNode = generator.getRoot()
generatorNode.reparentTo(render)
generatorNode.setDepthWrite(False)
generatorNode.setTransparency(True)
generatorNode.setTwoSided(True)
generatorNode.setTexture(loader.loadTexture("radarplate.png"))
generatorNode.setBin("fixed",0)
generatorNode.setLightOff(True)


base.setFrameRateMeter(True)
base.setBackgroundColor(.1,.1,.1,1)
t = loader.loadModel('teapot')
t.reparentTo(render)
t.setPos(0,0,-1)

def randVec():
    return Vec3(random()-.5,random()-.5,random()-.5)

def drawtask(taks):
    seed(1988)
    generator.begin(base.cam,render)
    for i in range(100):
        generator.billboard(randVec()*100,randint(181,207),1,Vec4(random(),random(),random(),1))
    for i in range(100):
        generator.segment(randVec()*100,randVec()*100,187,.1,Vec4(random(),random(),random(),1))
    generator.end()
    return taks.cont

taskMgr.add(drawtask, "draw task")
run()

