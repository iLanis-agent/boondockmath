import json, math

def num(x): return isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x)
def pos(x): return num(x) and x>0
def jround(x): return math.floor(x+0.5)
def r1(x): return jround(x*10)/10
def jsnum(x):
    if isinstance(x,float) and x==int(x): return str(int(x))
    return str(x)

GRAY_PER_PERSON=4; HOURS_PER_BOTTLE=12

def tank_plan(gray_gal,people):
    if not pos(gray_gal): return {"error":"the gray tank gallons must be above zero"}
    if not pos(people): return {"error":"the headcount must be above zero"}
    days=gray_gal/(people*GRAY_PER_PERSON)
    if days<3: verdict="the gray tank ends the weekend early"
    elif days<=5: verdict="a working week at most"
    else: verdict="the tank outlasts the fresh water"
    return {"days":r1(days),"verdict":verdict}

def render_tank(r,gray_gal,people):
    word=" person aboard" if people==1 else " people aboard"
    return ("The "+jsnum(gray_gal)+"-gallon gray tank with "+jsnum(people)+word
            +" at the 4-gallon navy-shower norm fills in about "+jsnum(r["days"])+" days - "+r["verdict"]+".")

def batt_plan(bank_ah,usable_pct,daily_ah):
    if not pos(bank_ah): return {"error":"the bank amp-hours must be above zero"}
    if not pos(usable_pct) or usable_pct>100: return {"error":"the usable percent must sit between zero and 100"}
    if not pos(daily_ah): return {"error":"the daily amp-hours must be above zero"}
    usable=bank_ah*usable_pct/100
    nights=usable/daily_ah
    if nights<1: verdict="the lights dim before dawn"
    elif nights<=3: verdict="a few honest nights"
    else: verdict="the bank outlasts the water"
    return {"usable":r1(usable),"nights":r1(nights),"verdict":verdict}

def render_batt(r,bank_ah,usable_pct,daily_ah):
    return ("The "+jsnum(bank_ah)+" amp-hour bank honestly gives "+jsnum(usable_pct)+"% of itself - "
            +jsnum(r["usable"])+" amp-hours against the "+jsnum(daily_ah)+"-amp-hour day, about "+jsnum(r["nights"])
            +" nights - "+r["verdict"]+".")

def prop_plan(bottles,hours_per_night):
    if not pos(bottles): return {"error":"the bottle count must be above zero"}
    if not pos(hours_per_night): return {"error":"the furnace hours per night must be above zero"}
    furnace_hours=bottles*HOURS_PER_BOTTLE
    nights=furnace_hours/hours_per_night
    if nights<3: verdict="a cold weekend at best"
    elif nights<=7: verdict="several honest nights"
    else: verdict="the bottles outlast the trip"
    return {"furnaceHours":r1(furnace_hours),"nights":r1(nights),"verdict":verdict}

def render_prop(r,bottles,hours_per_night):
    word=" bottle holds" if bottles==1 else " bottles hold"
    return ("The "+jsnum(bottles)+word+" about "+jsnum(r["furnaceHours"])+" honest furnace-hours; at "
            +jsnum(hours_per_night)+" hours a night that is about "+jsnum(r["nights"])+" nights - "+r["verdict"]+".")

cases=[]
def add(tool,args):
    if tool=="tank": r=tank_plan(*args); fn=render_tank
    elif tool=="batt": r=batt_plan(*args); fn=render_batt
    else: r=prop_plan(*args); fn=render_prop
    case={"tool":tool,"args":args,"result":r}
    if "error" not in r: case["render"]=fn(r,*args)
    cases.append(case)

for a in [(40,2),(30,4),(60,2),(24,1),(50,3),(36,2)]:
    add("tank",a)
for a in [(200,50,35),(100,80,20),(100,50,60),(400,80,40),(200,50,25),(100,50,30)]:
    add("batt",a)
for a in [(2,4),(1,6),(2,3),(3,5),(1,4),(2,8)]:
    add("prop",a)
add("tank",[0,2]); add("tank",[40,0])
add("batt",[0,50,35]); add("batt",[200,0,35]); add("batt",[200,110,35]); add("batt",[200,50,0])
add("prop",[0,4]); add("prop",[2,0])

json.dump(cases,open("expected.json","w"),separators=(",",":"))
print(len(cases),"cases")
