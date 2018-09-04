# -*- coding: utf-8 -*-
# Generoi input-tiedostot ja skriptitiedoston Vensimille

import numpy as np
import os


def createcin(p,scenario_roads,scenario_bio):
    
    global POLICY_PUBLIC_INFRA
    global POLICY_PUBLIC_COST_SUBSIDY
    global POLICY_MARKETING_DURATION_PUBLIC
    global POLICY_ELECTRIC_INFRA
    global POLICY_ELECTRIC_COST_SUBSIDY
    global POLICY_MARKETING_DURATION_ELECTRIC
    global POLICY_BIOFUEL_CAPACITY
    global POLICY_INCREASE_ROAD_CAPACITY
    
    global g
    global name
  
    POLICY_PUBLIC_INFRA = 0
    POLICY_PUBLIC_COST_SUBSIDY = 0
    POLICY_MARKETING_DURATION_PUBLIC = 0
    POLICY_ELECTRIC_INFRA = 0
    POLICY_ELECTRIC_COST_SUBSIDY = 0
    POLICY_MARKETING_DURATION_ELECTRIC = 0
    POLICY_BIOFUEL_CAPACITY = 0
    POLICY_INCREASE_ROAD_CAPACITY = 1

    if scenario_roads =='no roads':
        POLICY_INCREASE_ROAD_CAPACITY = 0     
    if scenario_bio == 'bio':
        POLICY_BIOFUEL_CAPACITY = 1
        
    if p=='p infra 0':
        POLICY_PUBLIC_INFRA = 1
        POLICY_MARKETING_DURATION_PUBLIC = 0
    elif p=='p infra 3':
        POLICY_PUBLIC_INFRA = 1
        POLICY_MARKETING_DURATION_PUBLIC = 3 
    elif p=='p infra 6':
        POLICY_PUBLIC_INFRA = 1
        POLICY_MARKETING_DURATION_PUBLIC = 6
    elif p=='p cost 0':
        POLICY_PUBLIC_COST_SUBSIDY = 1
        POLICY_MARKETING_DURATION_PUBLIC = 0
    elif p=='p cost 3':
        POLICY_PUBLIC_COST_SUBSIDY = 1
        POLICY_MARKETING_DURATION_PUBLIC = 3  
    elif p=='p cost 6':
        POLICY_PUBLIC_COST_SUBSIDY = 1
        POLICY_MARKETING_DURATION_PUBLIC = 6
    elif p=='p infra cost 0':
        POLICY_PUBLIC_INFRA = 1
        POLICY_PUBLIC_COST_SUBSIDY = 1
        POLICY_MARKETING_DURATION_PUBLIC = 0
    elif p=='p infra cost 3':
        POLICY_PUBLIC_INFRA = 1
        POLICY_PUBLIC_COST_SUBSIDY = 1
        POLICY_MARKETING_DURATION_PUBLIC = 3
    elif p=='p infra cost 6':
        POLICY_PUBLIC_INFRA = 1
        POLICY_PUBLIC_COST_SUBSIDY = 1
        POLICY_MARKETING_DURATION_PUBLIC = 6
    elif p=='e infra 10':
        POLICY_ELECTRIC_INFRA = 1
        POLICY_MARKETING_DURATION_ELECTRIC = 10
    elif p=='e infra 30':
        POLICY_ELECTRIC_INFRA = 1
        POLICY_MARKETING_DURATION_ELECTRIC = 30
    elif p=='e infra cost -':
        POLICY_ELECTRIC_INFRA = 1
        POLICY_ELECTRIC_COST_SUBSIDY = 1
        POLICY_MARKETING_DURATION_ELECTRIC = 20
    elif p=='e infra cost +':
        POLICY_ELECTRIC_INFRA = 1
        POLICY_ELECTRIC_COST_SUBSIDY = 1
        POLICY_MARKETING_DURATION_ELECTRIC = 40
    elif p=='e infra cost - p':
        POLICY_ELECTRIC_INFRA = 1
        POLICY_ELECTRIC_COST_SUBSIDY = 1
        POLICY_MARKETING_DURATION_ELECTRIC = 20
        POLICY_PUBLIC_INFRA = 1
        POLICY_PUBLIC_COST_SUBSIDY = 1
        POLICY_MARKETING_DURATION_PUBLIC = 10
    elif p=='e infra cost + p':
        POLICY_ELECTRIC_INFRA = 1
        POLICY_ELECTRIC_COST_SUBSIDY = 1
        POLICY_MARKETING_DURATION_ELECTRIC = 40
        POLICY_PUBLIC_INFRA = 1
        POLICY_PUBLIC_COST_SUBSIDY = 1
        POLICY_MARKETING_DURATION_PUBLIC = 10



    
    g=open('cin\\params['+p+']['+scenario_roads+']['+scenario_bio+'].cin', 'w')


    setval('POLICY PUBLIC INFRA',POLICY_PUBLIC_INFRA)
    setval('POLICY PUBLIC COST SUBSIDY',POLICY_PUBLIC_COST_SUBSIDY)
    setval('POLICY MARKETING DURATION PUBLIC',POLICY_MARKETING_DURATION_PUBLIC)
    setval('POLICY ELECTRIC INFRA',POLICY_ELECTRIC_INFRA)
    setval('POLICY ELECTRIC COST SUBSIDY',POLICY_ELECTRIC_COST_SUBSIDY)
    setval('POLICY MARKETING DURATION ELECTRIC',POLICY_MARKETING_DURATION_ELECTRIC)
    setval('POLICY BIOFUEL CAPACITY',POLICY_BIOFUEL_CAPACITY)
    setval('POLICY INCREASE ROAD CAPACITY',POLICY_INCREASE_ROAD_CAPACITY)

    
    g.close()
    
def extremecondition_vsc():
    global g
    g=open('sensitivity\\extremeconditions.vsc', 'w')
    g.write('100000,L,1234,,0\n')
    

    unif('ALPHA',0,1)
    unif('Biofuel price index',0.1,2)
    unif('Car Lifetime',5,20)
    unif('CONTACT RATE DIRECT',0.2,0.3)
    unif('CONTACT RATE INDIRECT',0.1,0.2)
    unif('Cost[public transport]',0.1,1)
    #Cost[regular car] = 1
    unif('Cost use[electric car]',0.1,2)
    unif('DELAY BIOFUEL',5,50)
    unif('DELAY INFRA CONSTRUCTION[public transport]',5,30)
    unif('DELAY INFRA CONSTRUCTION[regular car]',5,30)
    unif('DELAY INFRA CONSTRUCTION[electric car]',5,30)
    unif('DELAY POPULATION MOVEMENT',5,50)
    unif('DELAY ROAD INFRA',5,20)
    unif('DELAY USAGE CHANGE',1,10)
    unif('exo infra init[public transport]',0.1,1)
    #exo infra init[regular car] = 1
    #exo infra init[electric car] = 0
    #ExposureRef = 0.05
    #FINAL TIME = 2050
    unif('INIT ELECTRIC CAR WTC',0,1)
    unif('INIT PUBLIC WTC AMONG CAR USERS',0,1)
    #initial ownership fraction[electric car] = 0
    unif('INITIAL PERFORMANCE[public transport]',0.1,2)
    #INITIAL PERFORMANCE[regular car] = 1
    #INITIAL PERFORMANCE[electric car] = 0
    #initial population = 1.36e+006
    #INITIAL TIME = 2015
    #Marketing[regular car] = 0
    unif('MARKETING EFFECTIVENESS',0.001,0.1)
    unif('MAX POPULATION FRACTION WITH NO PUBLIC TRANSPORT',0,1)
    unif('MaxDecay',0.1,1)
    #new infra[regular car] = 0
    unif('OIL PRICE GROWTH RATE',-0.01,0.05)
    unif('POPULATION INCREASE SLOPE',0,100000)
    
    # Possibility to use    
    
    
    unif('Public transport decision interval',1,15)
    #REF COST = 1
    #REF PERFORMANCE = 1
    #REF USE COST = 1
    unif('SENSITIVITY CONGESTION',0.1,20)
    #TIME STEP = 0.125
    #Trips Per Person = 2.8
    #WtC init[public transport,public transport] = 1
    #WtC init[public transport,regular car] = 1
    #WtC init[regular car,regular car] = 1
    #WtC init[electric car,regular car] = 1
    #WtC init[electric car,electric car] = 1

    unif('POLICY PUBLIC INFRA',0,2)
    unif('POLICY PUBLIC COST SUBSIDY',0,1)
    unif('POLICY MARKETING DURATION PUBLIC',0,50)
    unif('POLICY ELECTRIC INFRA',0,2)
    unif('POLICY ELECTRIC COST SUBSIDY',0,1)
    unif('POLICY MARKETING DURATION ELECTRIC',0,50)
    unif('POLICY BIOFUEL CAPACITY',0,1)
    #unif('POLICY INCREASE ROAD CAPACITY',0,1)
    
    unif('Policy Time Cost',2010,2015)
    unif('Policy Time infra',2010,2015)
    unif('Policy Time marketing',2010,2015)
    

    g.close()

def setval(param_str,value):
    global g
    g.write(param_str+' = '+ str(value) + '\n')
    
def unif(param_str,minimi,maksimi):
    global g
    g.write(param_str+'=RANDOM_UNIFORM('+str(minimi)+','+str(maksimi)+')\n')


def create_cmd(cmd_name,scenario_roads,scenario_bio,policies):
    f = open(cmd_name+'['+scenario_roads+']['+scenario_bio+'].cmd','w')
    f.write('SPECIAL>CLEARRUNS\n')
    f.write('SIMULATE>BASED|\n')
    f.write('SIMULATE>PAYOFF|\n')
    
    for j in policies:
        createcin(j,scenario_roads,scenario_bio)
        f.write('\n')
        f.write('SIMULATE>RUNNAME|['+j+'].vdf\n')
        f.write('SIMULATE>READCIN|\\cin\\params['+j+']['+scenario_roads+']['+scenario_bio+'].cin\n')
        f.write('MENU>RUN|o\n')
    f.close()
    
def create_cmd_artikkeli():
    savelist = 'export save list.lst'
    
    f = open('_artikkeliin.cmd','w')
    f.write('SPECIAL>CLEARRUNS\n')
    f.write('SIMULATE>BASED|\n')
    f.write('SIMULATE>PAYOFF|\n')
    
    scenario_roads = 'no roads'
    scenario_bio = 'no bio'
    folder = '['+scenario_roads+']['+scenario_bio+']'
    for j in policies:
        createcin(j,scenario_roads,scenario_bio)
        f.write('\n')
        run ='['+j+']['+scenario_roads+']['+scenario_bio+']'
        
        f.write('SIMULATE>RUNNAME|['+j+']['+scenario_roads+']['+scenario_bio+'].vdf\n')
        f.write('SIMULATE>READCIN|\\cin\\params['+j+']['+scenario_roads+']['+scenario_bio+'].cin\n')
        f.write('MENU>RUN|o\n')
        f.write('MENU>VDF2TAB|'+run+'.vdf|\\outputs\\'+folder+'\\'+run+'.tab|'+savelist+'|*\n')
        f.write('SPECIAL>CLEARRUNS\n')
        
    '''    
        
    scenario_roads = 'no roads'
    scenario_bio = 'no bio'
    folder = '[no roads][no bio]'
    for j in policies:
        createcin(j,scenario_roads,scenario_bio)
        f.write('\n')
        run ='['+j+']['+scenario_roads+']['+scenario_bio+']'
        
        f.write('SIMULATE>RUNNAME|['+j+']['+scenario_roads+']['+scenario_bio+'].vdf\n')
        f.write('SIMULATE>READCIN|\\cin\\params['+j+']['+scenario_roads+']['+scenario_bio+'].cin\n')
        f.write('MENU>RUN|o\n')
        f.write('MENU>VDF2TAB|'+run+'.vdf|\\outputs\\'+folder+'\\'+run+'.tab|'+savelist+'|*\n')
        f.write('SPECIAL>CLEARRUNS\n')
        
    scenario_roads = 'roads'
    scenario_bio = 'bio'
    folder = '[roads][bio]'    
    for j in policies:
        createcin(j,scenario_roads,scenario_bio)
        f.write('\n')
        run ='['+j+']['+scenario_roads+']['+scenario_bio+']'
        
        f.write('SIMULATE>RUNNAME|.vdf\n')
        f.write('SIMULATE>READCIN|\\cin\\'+run+'.cin\n')
        f.write('MENU>RUN|o\n')
        f.write('MENU>VDF2TAB|'+run+'.vdf|\\outputs\\'+folder+'\\'+run+'.tab|'+savelist+'|*\n')
        f.write('SPECIAL>CLEARRUNS\n')
        
        
    '''
    
    f.close()
    
################

extremecondition_vsc()

                   
policies = ['e infra cost -','e infra cost +','e infra cost - p', 'e infra cost + p']
create_cmd_artikkeli()

