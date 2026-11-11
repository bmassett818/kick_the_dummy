from drafter import *
from dataclasses import dataclass
import random

@dataclass
class Body_Part:
    name:str
    number:int
    points:int
    limit:int
    
@dataclass
class Weapon:
    name:str
    impact:int
    energy:int
    
@dataclass
class State:
    bones:list[Body_Part]
    organs:list[Body_Part]
    weapon:Weapon
    name:str
    condition:str
    score:int

BONES=[Body_Part("pelvis",1,50,150)]
ORGANS=[Body_Part("brain",0,0,0)]
NO_WEAPON=Weapon("No Weapon",0,0)
WEAPONS=[NO_WEAPON]


def reset_state(state:State):
    state.bones=[]
    state.organs=[]
    for bone in BONES:
        state.bones.append(bone)
    for organ in ORGANS:
        state.organs.append(organ)
    state.weapon=Weapon(NO_WEAPON.name,NO_WEAPON.impact,NO_WEAPON.energy)
    state.condition="alive and well"
    state.score=0

def destroy_organ(organs:list[Body_Part],weapon:Weapon)->int:
    score=0
    organ=organs[random.randint(0,len(ORGANS))]
    if organ.limit<=weapon.energy and organ.number:
        score+=organ.points
        organ.number-=1
        weapon.energy-=organ.limit
    return score  

def destroy_body(bones:list[Body_Part],organs:list[Body_Part],weapon:Weapon)->int:
    score=0
    while weapon.impact>0:
        weapon.impact-=1
        bone=bones[random.randint(0,len(BONES))]
        if bone.number:
            if bone.limit<=weapon.energy:
                score+=bone.points
                bone.number-=1
            weapon.energy-=bone.limit
        else:
            score+=destroy_organ(organs,weapon)
    return score
    
def calculate_score(organs:list[Body_Part],bones:list[Body_Part],weapon:Weapon)->int:
    score=0
    score+=destroy_body(bones,organs,weapon)
    return score

def total_parts(parts:list[Body_Part])->int:
    total=0
    for part in parts:
        total+=part.number
    return total

def set_condition(organs:list[Body_Part],bones:list[Body_Part])->str:
    if total_parts(bones)==total_parts(BONES) and total_parts(organs)==total_parts(ORGANS):
        return "alive and well"
    elif total_parts(bones)>=total_parts(BONES)//4*3 and total_parts(organs)>=total_parts(ORGANS)//4*3:
        if Body_Part("brain",0,0,0) not in organs:
            return "braindead"
        else:
            return "bruised and battered"
    elif total_parts(bones)>=total_parts(BONES)//2 and total_parts(organs)>=total_parts(ORGANS)//2:
        return "barely alive"
    elif total_parts(bones)>0 and total_parts(organs)>0:
        return "eviscerated"
    else:
        return "atomized"
    
@route
def index(state:State)->Page:
    return Page(state, [
        Header("Kick the Dummy"),
        state.name+" is "+state.condition+"\n",
        TextBox("name",""),
        #Button("Set Name","set_name"),
        SelectBox("weapon_choice",["","","",""]),
        ])
'''
@route
def set_name(state:State,name:str)->Page:
'''
start_server(State(BONES,ORGANS,NO_WEAPON,"no name","alive and well",0))
