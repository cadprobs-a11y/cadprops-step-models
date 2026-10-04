# CADProps original model construction. CC0-1.0. Coordinates: millimetres.
from OCP.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeCone
from OCP.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCP.gp import gp_Pnt, gp_Dir, gp_Ax2

def box(x,y,z,dx,dy,dz):return BRepPrimAPI_MakeBox(gp_Pnt(x,y,z),dx,dy,dz).Shape()
def cyl(x,y,z,r,h,d=(0,0,1)):return BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(x,y,z),gp_Dir(*d)),r,h).Shape()
def cut(a,b):return BRepAlgoAPI_Cut(a,b).Shape()
def fuse(a,b):return BRepAlgoAPI_Fuse(a,b).Shape()

def originals():
 b=cut(fuse(cyl(0,0,0,12,25),cyl(0,0,0,18,4)),cyl(0,0,-1,7,27))
 yield ('sleeves-and-washers','flanged-bushing','Flanged bushing','A 24 mm sleeve with a 36 mm flange and 14 mm bore; overall length 25 mm.',b)
 outer=BRepPrimAPI_MakeCone(16,10,40).Shape()
 inner=BRepPrimAPI_MakeCone(gp_Ax2(gp_Pnt(0,0,-1),gp_Dir(0,0,1)),13,7,42).Shape()
 yield ('flanges-and-pipes','tapered-pipe-reducer','Tapered pipe reducer','A 40 mm long hollow transition from 32 mm to 20 mm outer diameter.',cut(outer,inner))
 tray=cut(box(0,0,0,80,60,24),box(3,3,3,74,54,25))
 yield ('enclosures-and-plates','electronics-tray','Electronics enclosure tray','An open 80 × 60 × 24 mm enclosure with 3 mm nominal walls and base.',tray)
 cover=box(0,0,0,80,60,3)
 for y in [10,17,24,31,38,45]: cover=cut(cover,box(14,y,-1,52,3,5))
 yield ('enclosures-and-plates','vented-cover','Vented enclosure cover','An 80 × 60 × 3 mm plate with six 52 × 3 mm ventilation slots.',cover)
 plate=cut(box(0,0,0,60,60,5),cyl(30,30,-1,12,7))
 for x in [10,50]:
  for y in [10,50]:plate=cut(plate,cyl(x,y,-1,2.5,7))
 yield ('enclosures-and-plates','motor-mount-plate','Motor mounting plate','A 60 × 60 × 5 mm plate with a 24 mm central opening and four 5 mm mounting holes.',plate)
 housing=box(-60,-37,0,120,74,9)
 housing=fuse(housing,box(-34,-18,8,68,36,38))
 housing=fuse(housing,cyl(0,-23,49,37,46,(0,1,0)))
 housing=fuse(housing,cyl(0,-27,49,40,8,(0,1,0)))
 housing=cut(housing,cyl(0,-30,49,26,60,(0,1,0)))
 for x in [-47,47]:
  for y in [-25,25]:
   housing=cut(housing,cyl(x,y,-1,5,12));housing=cut(housing,cyl(x,y,6,8,5))
 for x in [-23,23]:
  for z in [26,72]:housing=cut(housing,cyl(x,-29,z,3.2,55,(0,1,0)))
 yield ('enclosures-and-plates','bearing-housing','Bearing housing','An original 120 × 74 × 89 mm demonstration housing with a 52 mm through bore and mounting holes.',housing)
 hinge=fuse(box(0,0,0,50,35,4),cyl(8,0,8,7,35,(0,1,0)))
 hinge=cut(hinge,cyl(8,-1,8,3.5,37,(0,1,0)))
 for y in [8,27]:hinge=cut(hinge,cyl(38,y,-1,2.5,7))
 yield ('enclosures-and-plates','hinge-mounting-leaf','Hinge mounting leaf','A 50 × 35 mm mounting leaf with a 7 mm hinge bore and two 5 mm mounting holes.',hinge)

