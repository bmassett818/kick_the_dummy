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

BONES=[Body_Part("pelvis",1,50,450),Body_Part("foot",2,20,100),Body_Part("leg",2,30,200),Body_Part("arm",2,30,200),
       Body_Part("rib",12,20,50),Body_Part("spine",1,100,300),Body_Part("hand",2,20,100),Body_Part("collarbone",1,70,450),
       Body_Part("skull",1,100,350),Body_Part("neck",1,100,200)]
ORGANS=[Body_Part("brain",1,500,50),Body_Part("liver",1,350,50),Body_Part("lung",2,400,70),Body_Part("kidney",2,300,50),
        Body_Part("heart",1,750,60),Body_Part("eye",2,200,30)]
NO_WEAPON=Weapon("no weapon",0,0)
WEAPONS=[Weapon("bat",4,400),Weapon("sniper",2,1000),Weapon("rocket launcher",6,1000),Weapon("nuke",100,100000)]


def reset_state(state:State):
    state.bones=[]
    state.organs=[]
    for bone in BONES:
        state.bones.append(Body_Part(bone.name,bone.number,bone.points,bone.limit))
    for organ in ORGANS:
        state.organs.append(Body_Part(organ.name,organ.number,organ.points,organ.limit))
    state.weapon=Weapon(NO_WEAPON.name,NO_WEAPON.impact,NO_WEAPON.energy)
    state.condition="alive and well"
    state.score=0

def destroy_organ(organs:list[Body_Part],weapon:Weapon)->int:
    score=0
    index=random.randint(0,len(ORGANS)-1)
    if organs[index].limit<=weapon.energy and organs[index].number:
        score+=organs[index].points
        organs[index].number-=1
        weapon.energy-=organs[index].limit
    return score  

def destroy_body(bones:list[Body_Part],organs:list[Body_Part],weapon:Weapon)->int:
    score=0
    while weapon.impact>0:
        weapon.impact-=1
        index=random.randint(0,len(BONES)-1)
        if bones[index].number:
            if bones[index].limit<=weapon.energy:
                score+=bones[index].points
                bones[index].number-=1
            weapon.energy-=bones[index].limit
        else:
            score+=destroy_organ(organs,weapon)
    return score
    
def calculate_score(bones:list[Body_Part],organs:list[Body_Part],weapon:Weapon)->int:
    score=0
    score+=destroy_body(bones,organs,weapon)
    return score

def total_parts(parts:list[Body_Part])->int:
    total=0
    for part in parts:
        total+=part.number
    return total

def set_condition(bones:list[Body_Part],organs:list[Body_Part])->str:
    if total_parts(bones)>=total_parts(BONES) and total_parts(organs)>=total_parts(ORGANS):
        return "alive and well"
    elif total_parts(bones)>=total_parts(BONES)//4*3 and total_parts(organs)>=total_parts(ORGANS)//4*3:
        return "bruised and battered"
    elif total_parts(bones)>=total_parts(BONES)//2 and total_parts(organs)>=total_parts(ORGANS)//2:
        return "barely alive"
    elif total_parts(bones)>0 and total_parts(organs)>0:
        return "eviscerated"
    else:
        return "atomized"

def all_num(string:str)->bool:
    all_numbers=not string==""
    for character in string:
        all_numbers=all_numbers and character in "0123456789"
    return all_numbers
    
@route
def index(state:State)->Page:
    return Page(state, [
        Header("Kick the Dummy"),
        state.name+" is "+state.condition+"\n",
        TextBox("name",""),
        Button("Set Name","set_name"),
        SelectBox("weapon_choice",["bat","sniper","rocket launcher","nuke"]),
        Button("Kick the Dummy","weapon_directory"),
        "\n",
        ])

@route
def set_name(state:State,name:str)->Page:
    state.name=name
    return index(state)

@route
def bat(state:State,num_weapons:str)->Page:
    return Page(state, [
        Header("Score: "+str(state.score)),
        "condition: "+state.condition,
        TextBox("num_weapons","0"),
        Button("Fire","fire"),
        "\n",
        "hit dummy with "+num_weapons+" bats",
        "\n",
        Button("Back","back"),
        ])

@route
def sniper(state:State,num_weapons:str)->Page:
    return Page(state, [
        Header("Score: "+str(state.score)),
        "condition: "+state.condition,
        TextBox("num_weapons","0"),
        Button("Fire","fire"),
        "\n",
        "hit dummy with "+num_weapons+" snipers",
        "\n",
        Button("Back","back"),
        ])

@route
def rocket_launcher(state:State,num_weapons:str)->Page:
    return Page(state, [
        Header("Score: "+str(state.score)),
        "condition: "+state.condition,
        TextBox("num_weapons","0"),
        Button("Fire","fire"),
        "\n",
        "hit dummy with "+num_weapons+" rocket launchers",
        "\n",
        Button("Back","back"),
        ])

@route
def nuke(state:State,num_weapons:str)->Page:
    return Page(state, [
        Header("Score: "+str(state.score)),
        "condition: "+state.condition,
        TextBox("num_weapons","0"),
        Button("Fire","fire"),
        "\n",
        "hit dummy with "+num_weapons+" nukes",
        "\n",
        Button("Back","back"),
        ])

@route
def weapon_directory(state:State,weapon_choice:str,num_weapons="0")->Page:
    for weapon in WEAPONS:
        if weapon.name==weapon_choice:
            state.weapon=Weapon(weapon.name,weapon.impact,weapon.energy)
    if not all_num(num_weapons):
        num_weapons="0"
    if weapon_choice=="bat":
        return bat(state,num_weapons)
    elif weapon_choice=="sniper":
        return sniper(state,num_weapons)
    elif weapon_choice=="rocket launcher":
        return rocket_launcher(state,num_weapons)
    elif weapon_choice=="nuke":
        return nuke(state,num_weapons)
        
@route
def fire(state:State,num_weapons)->Page:
    if all_num(num_weapons):
        count=int(num_weapons)
    else:
        count=0
    while count>0:
        count-=1
        weapon=Weapon(state.weapon.name,state.weapon.impact,state.weapon.energy)
        state.score+=calculate_score(state.bones,state.organs,weapon)
    state.condition=set_condition(state.bones,state.organs)
    return weapon_directory(state,state.weapon.name,num_weapons)

@route
def back(state:State)->Page:
    reset_state(state)
    return index(state)
    
start_server(State([Body_Part("pelvis",1,50,450),Body_Part("foot",2,20,100),Body_Part("leg",2,30,200),Body_Part("arm",2,30,200),
       Body_Part("rib",12,20,50),Body_Part("spine",1,100,300),Body_Part("hand",2,20,100),Body_Part("collarbone",1,70,450),
       Body_Part("skull",1,100,350),Body_Part("neck",1,100,200)],
      [Body_Part("brain",1,500,50),Body_Part("liver",1,350,50),Body_Part("lung",2,400,70),Body_Part("kidney",2,300,50),
       Body_Part("heart",1,750,60),Body_Part("eye",2,200,30)],Weapon(NO_WEAPON.name,NO_WEAPON.impact,NO_WEAPON.energy),"no name","alive and well",0))
