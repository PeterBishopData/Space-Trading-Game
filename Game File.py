import csv
from itertools import zip_longest as z
from tkinter import *
import random

#A - Upload Data Files
#B - Game Options
#C - Player Voyageur Status Check
#D - Current System Status Check
#E - Fly to New Planet or SG
#F - Jump to New System
#G - Rescued due to No Fuel
#K - Landing Operations
#K1 - Repair Ship
#K2 - Buy Missiles
#K3 - Cash in Bounties
#K4 - Fill up with Fuel
#L - Operations in an Asteroid Belt
#Q - Combat
#Q1- Retreat
#Q2- Attack
#R - Respawning
#V - Trading
#V1 - Set Up
#V2 - Selling
#V3 - Purchasing
#Z - Mission Management
#AE - Collect Stellar Gas
#AJ - Ending Game

#A - Upload Data Files

with open('Data/Bank.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')
    
    for row in readCSV:
    
       bankAmount = int(row[0])

with open('Data/Cargo.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')

    dataListCargo = []
    
    for row in readCSV:
    
        slot= row[0]
        goods= row[1]
        amount= int(row[2])

        combo = [slot, goods, amount, 0]
        
        dataListCargo = dataListCargo + [combo]

with open('Data/Jumps.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')

    dataListJumps = []
    
    for row in readCSV:

        d1 = row[0]
        d2 = row[1]
        d3 = row[2]
        d4 = row[3]
        
        combo = [d1, d2, d3, d4]
        
        dataListJumps = dataListJumps + [combo]
        
with open('Data/MissionDist.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')

    dataMissionDistance = []
    
    for row in readCSV:

        start = row[0]
        finish = row[1]
        variable = row[2]
        
        combo = [start, finish, variable]
        
        dataMissionDistance  = dataMissionDistance + [combo]

with open('Data/Systems.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')

    dataListSystems = []
    dataListSyPackage = []
    dataListRescue = []
    
    for row in readCSV:
       
        system = row[0]
        place = row[1]
        config = row [2]
        systemR = row[9]
        placeR = row[10]

        combo1 = [system, place, config]

        dataListSystems = dataListSystems + [combo1] 
        
        if config != 'AF' and config != 'SG' and config != 'GF':
            
            combo2 = [system, place]
   
            dataListSyPackage = dataListSyPackage + [combo2]
        
        combo3 = [system, systemR, placeR]
        
        dataListRescue = dataListRescue + [combo3]

#Programming Note - The Jump Distances has to be loaded in section F.

with open('Data/TradeGoods.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')

    dataListSPrices = []
    
    for row in readCSV:
    
        material = row[0]
        buyM = int(row[1])
        buyR= int(row[2])
        buyG = int(row[3])
        buySB = int(row[4])
        sellM = int(row[5])
        sellR = int(row[6])
        sellG = int(row[7])
        sellSB = int(row[8])
        amount = int(row[9])

        combo = [material, buyM, buyR, buyG, buySB, sellM, sellR, sellG, sellSB, amount]
        
        dataListSPrices = dataListSPrices + [combo] 

with open('Data/Voyageur.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')
    
    for row in readCSV:
    
        nameVoyageur = row[0]
        profession = row[1]
        nameShip = row[2]       
        shipSystem = row[3]
        shipLocation = row[4]
        cargoCapacity = int(row[5])
        hullPoints = int(row[6])
        missilesArmed = int(row[7])
        bountyLevel = int(row[8])
        numberPackages = int(row[9])
        missionSystem = row[10]
        missionPlanet = row[11]
        missionReward = int(row[12])
        fuelAmount = int(row[13])
        
endGame = 'N'

asteroidEnemyDefence = 0

def main ():

#B - Game Options

    class Option:

        global shipSystem
        
        indexEvent = random.randint(1,10)
         
        def __init__(self):
            self.master = Tk()
            self.master.title('Game Options')
            self.master.geometry('260x240+50+50')
            self.master.configure(bg = "#FFFFFF" )
                           
            self.OptionVS= Button(self.master, text = '[#]',command = self.activateVoyageurStatus)
            self.OptionVS.place(x = 10, y = 0)
            self.OptionVS.configure(fg = '#FF0000', bg = '#FFFFFF')

            self.labelEntryVS = Label(self.master, text = 'Voyageur Stats Check')
            self.labelEntryVS.place(x = 40, y = 0)
            self.labelEntryVS.configure(bg = '#FFFFFF')
            
            self.OptionSS = Button(self.master, text = '[#]',command = self.activateSystemStatus)
            self.OptionSS.place(x = 10, y = 25)
            self.OptionSS.configure(fg = '#FF0000', bg = '#FFFFFF')

            self.labelEntrySS = Label(self.master, text = 'Current System Stats Check')
            self.labelEntrySS.place(x = 40, y = 25)
            self.labelEntrySS.configure(bg = '#FFFFFF')
            
            self.labelEntryGO = Label(self.master, text = 'You have the following options')
            self.labelEntryGO.place(x = 10, y = 55)
            self.labelEntryGO.configure(bg = '#FFFFFF')
            
            self.Option4B = Button(self.master, text = '[#]',command = self.activateEndGame)
            self.Option4B.place(x = 10, y = 80)
            self.Option4B.configure(fg = '#FF0000', bg = '#FFFFFF')

            self.labelEntry4L = Label(self.master, text = 'You can end the Game')
            self.labelEntry4L.place(x = 40, y = 80)
            self.labelEntry4L.configure(bg = '#FFFFFF') 
            
            self.Option1B = Button(self.master, text = '[#]',command = self.activateFly)
            self.Option1B.place(x = 10, y = 105)
            self.Option1B.configure(fg = '#FF0000', bg = '#FFFFFF')

            self.labelEntry1L = Label(self.master, text = 'You can fly to a new planet or star gate')
            self.labelEntry1L.place(x = 40, y = 105)
            self.labelEntry1L.configure(bg = '#FFFFFF')

            lengthS = len(dataListSystems)
            for mark in range (0, lengthS):
 
                if shipLocation == dataListSystems[mark][1]:

                    if dataListSystems[mark][2] == 'SG':
                    
                        self.Option2B = Button(self.master, text = '[#]',command = self.activateJump)
                        self.Option2B.place(x = 10, y = 130)
                        self.Option2B.configure(fg = '#FF0000', bg = '#FFFFFF')

                        self.labelEntry2L = Label(self.master, text = 'You can jump to a new system')
                        self.labelEntry2L.place(x = 40, y = 130)
                        self.labelEntry2L.configure(bg = '#FFFFFF')              
                
                    elif dataListSystems[mark][2] == 'AF':
                            
                        self.Option2B = Button(self.master, text = '[#]',command = self.activateAFEvent)
                        self.Option2B.place(x = 10, y = 130)
                        self.Option2B.configure(fg = '#FF0000', bg = '#FFFFFF')

                        self.labelEntry2L = Label(self.master, text = 'You can entry the asteroid field')
                        self.labelEntry2L.place(x = 40, y = 130)
                        self.labelEntry2L.configure(bg = '#FFFFFF')
                        
                    elif dataListSystems[mark][2] == 'GF':
                        
                        global hullPoints
                        
                        if hullPoints > 5:
                                                                
                            self.OptionSG = Button(self.master, text = '[#]',command = self.activateStellarGas)
                            self.OptionSG.place(x = 10, y = 130)
                            self.OptionSG.configure(fg = '#FF0000', bg = '#FFFFFF')
                                                        
                            self.labelEntry2L = Label(self.master, text = 'You can skim for stellar gas')
                            self.labelEntry2L.place(x = 40, y = 130)
                            self.labelEntry2L.configure(bg = '#FFFFFF')
                            
                        else:
                                                        
                            self.labelEntry2L = Label(self.master, text = 'Your hull points are too low to skim')
                            self.labelEntry2L.place(x = 40, y = 130)
                            self.labelEntry2L.configure(bg = '#FFFFFF')
  
                    else:
                    
                        self.Option2B = Button(self.master, text = '[#]',command = self.activateTrade)
                        self.Option2B.place(x = 10, y = 130)
                        self.Option2B.configure(fg = '#FF0000', bg = '#FFFFFF')

                        self.labelEntry2L = Label(self.master, text = 'Trade market')
                        self.labelEntry2L.place(x = 40, y = 130)
                        self.labelEntry2L.configure(bg = '#FFFFFF')

                        self.Option3B = Button(self.master, text = '[#]',command = self.activateLand)
                        self.Option3B.place(x = 10, y = 155)
                        self.Option3B.configure(fg = '#FF0000', bg = '#FFFFFF')

                        self.labelEntry3L = Label(self.master, text = 'Planetary utilities')
                        self.labelEntry3L.place(x = 40, y = 155)
                        self.labelEntry3L.configure(bg = '#FFFFFF')
                    
                        self.Option3B = Button(self.master, text = '[#]',command = self.activateMission)
                        self.Option3B.place(x = 10, y = 180)
                        self.Option3B.configure(fg = '#FF0000', bg = '#FFFFFF')
                        
                        self.labelEntry5L = Label(self.master, text = 'Mission management')
                        self.labelEntry5L.place(x = 40, y = 180)
                        self.labelEntry5L.configure(bg = '#FFFFFF')
                        
                        if dataListSystems[mark][2] == 'G':
                                        
                            self.OptionSG = Button(self.master, text = '[#]',command = self.activateStellarGas)
                            self.OptionSG.place(x = 10, y = 205)
                            self.OptionSG.configure(fg = '#FF0000', bg = '#FFFFFF')
                                                    
                            self.labelEntrySG = Label(self.master, text = 'You may skim for stellar gas')
                            self.labelEntrySG.place(x = 40, y = 205)
                            self.labelEntrySG.configure(bg = '#FFFFFF')

            self.master.mainloop()
            
#C - Player Voyageur Status Check

        def activateVoyageurStatus(self):
                         
            self.master.destroy()

            class VoyageurStatus:
                
                global nameVoyageur
                global profession
                global bankAmount
                global nameShip
                global dataListSystems
                global shipLocation
                global shipSystem
                global cargoCapacity
                global dataListCargo
                global numberPackages
                global fuelAmount
                global hullPoints
                global missileArmed
                global bountyLevel

                def __init__(self):
                    self.master = Tk()
                    self.master.title('Voyageur Details')
                    self.master.geometry('360x395+50+50')
                    self.master.configure(bg = "#FFFFFF" )
                                                 
                    self.activateButton = Button(self.master, text = 'Press to Return',command = self.activateEntry)
                    self.activateButton.place(x = 10, y = 0)
                    self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
                
                    self.labelEntryA = Label(self.master, text = nameVoyageur + ' -' + profession)
                    self.labelEntryA.place(x = 10, y = 30)
                    self.labelEntryA.configure(bg = '#FFFFFF')
        
                    lengthS = len(dataListSystems)
                    worldType = 'Unknown'
                    for mark in range (0, lengthS):
                            if shipLocation == dataListSystems[mark][1]:
                                worldType = dataListSystems[mark][2]
                          
                    self.labelEntryB = Label(self.master, text = 'At ' + shipLocation + ' in the ' + shipSystem + ' system, an '
                            + worldType + ' type location')
                    self.labelEntryB.place(x = 10, y = 55)
                    self.labelEntryB.configure(bg = '#FFFFFF')
                    
                    self.labelEntryC = Label(self.master, text = 'There are ' + str(bankAmount) + ' credits in the bank')
                    self.labelEntryC.place(x = 10, y = 80)
                    self.labelEntryC.configure(bg = '#FFFFFF')
                    
                    self.labelEntryD = Label(self.master, text = 'Ship "' + nameShip + '"')
                    self.labelEntryD.place(x = 10, y = 105)
                    self.labelEntryD.configure(bg = '#FFFFFF')
                    
                    self.labelEntryE = Label(self.master, text = 'Total ' + str(cargoCapacity) + ' units allowed cargo space'
                          + ' includes ' + str(numberPackages) + ' packages')
                    self.labelEntryE.place(x = 10, y = 130)
                    self.labelEntryE.configure(bg = '#FFFFFF')
                
                    self.labelEntryE1a = Label(self.master, text = dataListCargo[0][0])
                    self.labelEntryE1a.place(x = 25, y = 150)
                    self.labelEntryE1a.configure(bg = '#FFFFFF')
                    
                    self.labelEntryE1b = Label(self.master, text = dataListCargo[0][1])
                    self.labelEntryE1b.place(x = 60, y = 150)
                    self.labelEntryE1b.configure(bg = '#FFFFFF')
            
                    self.labelEntryE1c = Label(self.master, text = str(dataListCargo[0][2]) + ' units')
                    self.labelEntryE1c.place(x = 140, y = 150)
                    self.labelEntryE1c.configure(bg = '#FFFFFF')
                    
                    self.labelEntryE2a = Label(self.master, text = dataListCargo[1][0])
                    self.labelEntryE2a.place(x = 25, y = 170)
                    self.labelEntryE2a.configure(bg = '#FFFFFF')
                    
                    self.labelEntryE2b = Label(self.master, text = dataListCargo[1][1])
                    self.labelEntryE2b.place(x = 60, y = 170)
                    self.labelEntryE2b.configure(bg = '#FFFFFF')
            
                    self.labelEntryE2c = Label(self.master, text = str(dataListCargo[1][2]) + ' units')
                    self.labelEntryE2c.place(x = 140, y = 170)
                    self.labelEntryE2c.configure(bg = '#FFFFFF')
                    
                    self.labelEntryE3a = Label(self.master, text = dataListCargo[2][0])
                    self.labelEntryE3a.place(x = 25, y = 190)
                    self.labelEntryE3a.configure(bg = '#FFFFFF')
                    
                    self.labelEntryE3b = Label(self.master, text = dataListCargo[2][1])
                    self.labelEntryE3b.place(x = 60, y = 190)
                    self.labelEntryE3b.configure(bg = '#FFFFFF')
            
                    self.labelEntryE3c = Label(self.master, text = str(dataListCargo[2][2]) + ' units')
                    self.labelEntryE3c.place(x = 140, y = 190)
                    self.labelEntryE3c.configure(bg = '#FFFFFF')
                    
                    self.labelEntryE4a = Label(self.master, text = dataListCargo[3][0])
                    self.labelEntryE4a.place(x = 25, y = 210)
                    self.labelEntryE4a.configure(bg = '#FFFFFF')
                    
                    self.labelEntryE4b = Label(self.master, text = dataListCargo[3][1])
                    self.labelEntryE4b.place(x = 60, y = 210)
                    self.labelEntryE4b.configure(bg = '#FFFFFF')
            
                    self.labelEntryE4c = Label(self.master, text = str(dataListCargo[3][2]) + ' units')
                    self.labelEntryE4c.place(x = 140, y = 210)
                    self.labelEntryE4c.configure(bg = '#FFFFFF')
                    
                    self.labelEntryF = Label(self.master, text = 'Current fuel level is ' +str(fuelAmount) + ' units')
                    self.labelEntryF.place(x = 10, y = 235)
                    self.labelEntryF.configure(bg = '#FFFFFF')                  
                                  
                    self.labelEntryF = Label(self.master, text = 'Combat Features')
                    self.labelEntryF.place(x = 10, y = 260)
                    self.labelEntryF.configure(bg = '#FFFFFF')
                
                    self.labelEntryF1 = Label(self.master, text = 'Currently ' +str(hullPoints) + ' defence points')
                    self.labelEntryF1.place(x = 25, y = 280)
                    self.labelEntryF1.configure(bg = '#FFFFFF')
                    
                    self.labelEntryF2 = Label(self.master, text = 'Carrying ' + str(missilesArmed) + ' missiles')
                    self.labelEntryF2.place(x = 25, y = 300)
                    self.labelEntryF2.configure(bg = '#FFFFFF')
                                      
                    self.labelEntryF3 = Label(self.master, text = 'Have ' + str(bountyLevel) + ' bounties to cash in')
                    self.labelEntryF3.place(x = 25, y = 320)
                    self.labelEntryF3.configure(bg = '#FFFFFF')
                  
                    if numberPackages == 0:
                        self.labelEntryMS1 = Label(self.master, text = 'Currently no current mission')
                        self.labelEntryMS1.place(x = 10, y = 345)
                        self.labelEntryMS1.configure(bg = '#FFFFFF')
                        
                    if numberPackages != 0:                    
                        
                        self.labelEntryE4c = Label(self.master,
                             text = 'Currently a misison to ' + missionPlanet + ' in ' + missionSystem + ' system')
                        self.labelEntryE4c.place(x = 10, y = 345)
                        self.labelEntryE4c.configure(bg = '#FFFFFF')
                        
                        self.labelEntryE4c = Label(self.master, text = 'Carrying ' + str(numberPackages) + ' packages')
                        self.labelEntryE4c.place(x = 25, y = 365)
                        self.labelEntryE4c.configure(bg = '#FFFFFF')
 
                    self.master.mainloop()
    
                def activateEntry(self):
            
                    self.master.destroy()

            VoyageurStatus()                  
 
                  
#D - Current System Status Check

        def activateSystemStatus(self):
                           
            self.master.destroy()
                
            global shipSystem
            global shipLocation
            
            with open('Data/Systems.csv') as file:
               readCSV = csv.reader(file, delimiter = ',')
    
               dataListCSPlanets = []
        
               for row in readCSV:
               
                  system = row[0]
                  place = row[1]
                  config = row [2]
    
                  if system  == shipSystem:

                     if shipLocation == place:
                            
                        combo = [place, config, '#']

                     else:

                        combo = [place, config, '']
                            
                     dataListCSPlanets= dataListCSPlanets + [combo]
                            
            lengthG = len(dataListCSPlanets)

            class SystemStatus:

                def __init__(self):
                    self.master = Tk()
                    self.master.title('System Details')
                    self.master.geometry('220x220+50+50')
                    self.master.configure(bg = "#FFFFFF" )
                      
                    self.activateButton = Button(self.master, text = 'Press to Return',command = self.activateEntry)
                    self.activateButton.place(x = 10, y = 0)
                    self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')

                    self.labelEntryCS = Label(self.master, text = 'Current System - ' + shipSystem)
                    self.labelEntryCS.place(x = 10, y = 25)
                    self.labelEntryCS.configure(bg = '#FFFFFF')
                                             
                    self.labelEntryHT = Label(self.master, text = 'Type' )
                    self.labelEntryHT.place(x = 30, y = 50)
                    self.labelEntryHT.configure(bg = '#FFFFFF')
                    
                    self.labelEntryHP = Label(self.master, text = 'Location')
                    self.labelEntryHP.place(x = 70, y = 50)
                    self.labelEntryHP.configure(bg = '#FFFFFF')
            
                    self.labelEntryPl = Label(self.master, text = dataListCSPlanets[0][0])
                    self.labelEntryPl.place(x = 70, y = 70)
                    self.labelEntryPl.configure(bg = '#FFFFFF')
                    
                    self.labelEntryC1 = Label(self.master, text = dataListCSPlanets[0][1])
                    self.labelEntryC1.place(x = 35, y = 70)
                    self.labelEntryC1.configure(bg = '#FFFFFF')
                 
                    self.labelEntryL1 = Label(self.master, text = dataListCSPlanets[0][2])
                    self.labelEntryL1.place(x = 10, y = 70)
                    self.labelEntryL1.configure(fg = '#FF0000', bg = '#FFFFFF')
             
                    self.labelEntryP2 = Label(self.master, text = dataListCSPlanets[1][0])
                    self.labelEntryP2.place(x = 70, y = 90)
                    self.labelEntryP2.configure(bg = '#FFFFFF')
                    
                    self.labelEntryC2 = Label(self.master, text = dataListCSPlanets[1][1])
                    self.labelEntryC2.place(x = 35, y = 90)
                    self.labelEntryC2.configure(bg = '#FFFFFF')
                    
                    self.labelEntryL2 = Label(self.master, text = dataListCSPlanets[1][2])
                    self.labelEntryL2.place(x = 10, y = 90)
                    self.labelEntryL2.configure(fg = '#FF0000', bg = '#FFFFFF')
                     
                    if lengthG > 2:
                
                        self.labelEntryP3 = Label(self.master, text = dataListCSPlanets[2][0])
                        self.labelEntryP3.place(x = 70, y = 110)
                        self.labelEntryP3.configure(bg = '#FFFFFF')
                        
                        self.labelEntryC3 = Label(self.master, text = dataListCSPlanets[2][1])
                        self.labelEntryC3.place(x = 35, y = 110)
                        self.labelEntryC3.configure(bg = '#FFFFFF')
 
                        self.labelEntryL3 = Label(self.master, text = dataListCSPlanets[2][2])
                        self.labelEntryL3.place(x = 10, y = 110)
                        self.labelEntryL3.configure(fg = '#FF0000', bg = '#FFFFFF')
            
                    if lengthG > 3:
                  
                        self.labelEntryP4 = Label(self.master, text = dataListCSPlanets[3][0])
                        self.labelEntryP4.place(x = 70, y = 130)
                        self.labelEntryP4.configure(bg = '#FFFFFF')
                        
                        self.labelEntryC4 = Label(self.master, text = dataListCSPlanets[3][1])
                        self.labelEntryC4.place(x = 35, y = 130)
                        self.labelEntryC4.configure(bg = '#FFFFFF')
   
                        self.labelEntryL4 = Label(self.master, text = dataListCSPlanets[3][2])
                        self.labelEntryL4.place(x = 10, y = 130)
                        self.labelEntryL4.configure(fg = '#FF0000', bg = '#FFFFFF')
            
                    if lengthG > 4:
            
                        self.labelEntryP5 = Label(self.master, text = dataListCSPlanets[4][0])
                        self.labelEntryP5.place(x = 70, y = 150)
                        self.labelEntryP5.configure(bg = '#FFFFFF')
                        
                        self.labelEntryC5 = Label(self.master, text = dataListCSPlanets[4][1])
                        self.labelEntryC5.place(x =35, y = 150)
                        self.labelEntryC5.configure(bg = '#FFFFFF')
   
                        self.labelEntryL5 = Label(self.master, text = dataListCSPlanets[4][2])
                        self.labelEntryL5.place(x = 10, y = 150)
                        self.labelEntryL5.configure(fg = '#FF0000', bg = '#FFFFFF')
              
                    if lengthG > 5:
            
                        self.labelEntryP5 = Label(self.master, text = dataListCSPlanets[5][0])
                        self.labelEntryP5.place(x = 70, y = 170)
                        self.labelEntryP5.configure(bg = '#FFFFFF')
                        
                        self.labelEntryC5 = Label(self.master, text = dataListCSPlanets[5][1])
                        self.labelEntryC5.place(x = 35, y = 170)
                        self.labelEntryC5.configure(bg = '#FFFFFF')
                     
                        self.labelEntryL5 = Label(self.master, text = dataListCSPlanets[5][2])
                        self.labelEntryL5.place(x = 10, y = 170)
                        self.labelEntryL5.configure(fg = '#FF0000', bg = '#FFFFFF')                 
                        
                    if lengthG > 6:
            
                        self.labelEntryP5 = Label(self.master, text = dataListCSPlanets[6][0])
                        self.labelEntryP5.place(x = 70, y = 190)
                        self.labelEntryP5.configure(bg = '#FFFFFF')
                        
                        self.labelEntryC5 = Label(self.master, text = dataListCSPlanets[6][1])
                        self.labelEntryC5.place(x = 35, y = 190)
                        self.labelEntryC5.configure(bg = '#FFFFFF')
                     
                        self.labelEntryL5 = Label(self.master, text = dataListCSPlanets[6][2])
                        self.labelEntryL5.place(x = 10, y = 190)
                        self.labelEntryL5.configure(fg = '#FF0000', bg = '#FFFFFF')
            
                    self.master.mainloop()
    
                def activateEntry(self):
            
                    self.master.destroy()

            SystemStatus()                  
  
#E - Fly to New Planet or SG         
        
        def activateFly(self):

            self.master.destroy()
            
            with open('Data/Systems.csv') as file:
                readCSV = csv.reader(file, delimiter = ',')

                dataListSyDistances = []
    
                for row in readCSV:
           
                    system = row[0]
                    place = row[1]
                    config = row [2]
                    d1 = int(row[3])
                    d2 = int(row[4])
                    d3 = int(row[5])
                    d4 = int(row[6])
                    d5 = int(row[7])
                    d6 = int(row[8])

                    combo = [system, place, d1, d2, d3, d4, d5, d6]

                    dataListSyDistances = dataListSyDistances + [combo]

            global shipSystem
            global shipLocation
            
            lengthSyS = len(dataListSyDistances) + 1
            dataListDestination = []
            dataListPlanetsC = []
            dataListDistancesC = []
            
            lengthSyS = len(dataListSyDistances)
            
            for mark in range (0, lengthSyS):
                if shipSystem == dataListSyDistances [mark][0]:
                    dataListDestination = dataListDestination + [dataListSyDistances[mark]]

            lengthPlan = len(dataListDestination)
                                                                                               
            for mark in range (0, lengthPlan):

                if dataListDestination[mark][1] != shipLocation:
                     dataListPlanetsC = dataListPlanetsC + [dataListDestination[mark][1]]

            for mark in range (0, lengthPlan):

               if dataListDestination [mark][1] == shipLocation:

                  for counter in range(2,8):

                     dataListDistancesC = dataListDistancesC + [dataListDestination [mark][counter]]
            
            lengthG = len(dataListPlanetsC)
         
            class LocationToLocation:
                 
                def __init__(self):
                    self.master = Tk()
                    self.master.title('Flying to New Location')
                    self.master.geometry('240x220+50+50')
                    self.master.configure(bg = "#FFFFFF" )
         
                    self.labelEntryTSl = Label(self.master, text = 'Current Location - ' + shipLocation)
                    self.labelEntryTSl.place(x = 10, y = 0)
                    self.labelEntryTSl.configure(bg = '#FFFFFF')
                    
                    if shipSystem == 'GH678':
                    
                        indexEvent = random.randint(1,8)
                        
                        indexEvent = 8
                    
                        if indexEvent == 8:
                                        
                            self.Option2B = Button(self.master, text = 'Press to Fly', command = self.activateSpEvent)
                            self.Option2B.place(x = 10, y = 30)
                            self.Option2B.configure(fg = '#FF0000', bg = '#FFFFFF')
                            
                        else:
                            
                            self.activateButton = Button(self.master, text = 'Press to Fly',command = self.activateEntry)
                            self.activateButton.place(x = 10, y = 30)
                            self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
                    
                    else:
                        self.activateButton = Button(self.master, text = 'Press to Fly',command = self.activateEntry)
                        self.activateButton.place(x = 10, y = 30)
                        self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
                        
                    
                    self.labelEntryTSl = Label(self.master, text = 'Distance to')
                    self.labelEntryTSl.place(x = 35, y = 60)
                    self.labelEntryTSl.configure(bg = '#FFFFFF')
                       
                    self.variable1S = StringVar()
                    self.labelEntry1S = Entry(self.master, width = 3, textvariable = self.variable1S)
                    self.labelEntry1S.place(x = 10, y = 85)
                    
                    self.labelEntryPl = Label(self.master, text = dataListPlanetsC[0])
                    self.labelEntryPl.place(x = 85, y = 85)
                    self.labelEntryPl.configure(bg = '#FFFFFF')
                    
                    self.labelEntryD1 = Label(self.master, text = str(dataListDistancesC[0])  + ' days' )
                    self.labelEntryD1.place(x = 40, y = 85)
                    self.labelEntryD1.configure(bg = '#FFFFFF')
        
                    if lengthG > 1:
               
                        self.variable2S = StringVar()
                        self.labelEntry2S = Entry(self.master, width = 3, textvariable = self.variable2S)
                        self.labelEntry2S.place(x = 10, y = 105)
                
                        self.labelEntryP2 = Label(self.master, text = dataListPlanetsC[1])
                        self.labelEntryP2.place(x = 85, y = 105)
                        self.labelEntryP2.configure(bg = '#FFFFFF')
                        
                        self.labelEntryD2 = Label(self.master, text = str(dataListDistancesC[1])  + ' days' )
                        self.labelEntryD2.place(x = 40, y = 105)
                        self.labelEntryD2.configure(bg = '#FFFFFF')
            
                    if lengthG > 2:
  
                        self.variable3S = StringVar()
                        self.labelEntry3S = Entry(self.master, width = 3, textvariable = self.variable3S)
                        self.labelEntry3S.place(x = 10, y = 125)
                      
                        self.labelEntryP3 = Label(self.master, text = dataListPlanetsC[2])
                        self.labelEntryP3.place(x = 85, y = 125)
                        self.labelEntryP3.configure(bg = '#FFFFFF')
                        
                        self.labelEntryD3 = Label(self.master, text = str(dataListDistancesC[2])  + ' days' )
                        self.labelEntryD3.place(x = 40, y = 125)
                        self.labelEntryD3.configure(bg = '#FFFFFF')

                    if lengthG > 3:
                                        
                        self.variable4S = StringVar()
                        self.labelEntry4S = Entry(self.master, width= 3, textvariable = self.variable4S)
                        self.labelEntry4S.place(x = 10, y = 145)
                    
                        self.labelEntryP4 = Label(self.master, text = dataListPlanetsC[3])
                        self.labelEntryP4.place(x = 85, y = 145)
                        self.labelEntryP4.configure(bg = '#FFFFFF')
                            
                        self.labelEntryD4 = Label(self.master, text = str(dataListDistancesC[3])  + ' days' )
                        self.labelEntryD4.place(x = 40, y = 145)
                        self.labelEntryD4.configure(bg = '#FFFFFF')

                    if lengthG > 4:
 
                        self.variable5S = StringVar()
                        self.labelEntry5S = Entry(self.master, width = 3, textvariable = self.variable5S)
                        self.labelEntry5S.place(x = 10, y = 165)                   
             
                        self.labelEntryP5 = Label(self.master, text = dataListPlanetsC[4])
                        self.labelEntryP5.place(x = 85, y = 165)
                        self.labelEntryP5.configure(bg = '#FFFFFF')
                                
                        self.labelEntryD5 = Label(self.master, text = str(dataListDistancesC[4])  + ' days' )
                        self.labelEntryD5.place(x = 40, y = 165)                            
                        self.labelEntryD5.configure(bg = '#FFFFFF')
                        
                    if lengthG > 5:
                              
                        self.variable6S = StringVar()
                        self.labelEntry6S = Entry(self.master, width = 3, textvariable = self.variable6S)
                        self.labelEntry6S.place(x = 10, y = 185)           
             
                        self.labelEntryP6 = Label(self.master, text = dataListPlanetsC[5])
                        self.labelEntryP6.place(x = 85, y = 185)
                        self.labelEntryP6.configure(bg = '#FFFFFF')
                                
                        self.labelEntryD6 = Label(self.master, text = str(dataListDistancesC[5])  + ' days' )
                        self.labelEntryD6.place(x = 40, y = 185)
                        self.labelEntryD6.configure(bg = '#FFFFFF')
          
                    self.master.mainloop()
                
            #E2 - Fly to New Location
                
                def activateEntry(self):
                        
                    self.master.destroy()
                  
                    fly1 = self.variable1S.get()
                    if lengthG > 1:
                        fly2 = self.variable2S.get()
                    if lengthG > 2:
                        fly3 = self.variable3S.get()
                    if lengthG > 3:
                        fly4 = self.variable4S.get()
                    if lengthG > 4:
                        fly5 = self.variable5S.get()
                    if lengthG > 5:
                        fly6 = self.variable6S.get()
                       
                    global shipLocation
                    global fuelAmount
                    
                    if fly1 == 'x':
                        shipLocation = dataListPlanetsC[0]
                        fuelAmount = fuelAmount - dataListDistancesC[0]
                    if lengthG > 1:
                        if fly2 == 'x':
                            shipLocation = dataListPlanetsC[1]
                            fuelAmount = fuelAmount - dataListDistancesC[1]                           
                    if lengthG > 2:
                        if fly3 == 'x':
                            shipLocation = dataListPlanetsC[2]
                            fuelAmount = fuelAmount - dataListDistancesC[2]                     
                    if lengthG  > 3:
                        if fly4 == 'x':
                            shipLocation = dataListPlanetsC[3]
                            fuelAmount = fuelAmount - dataListDistancesC[3]
                    if lengthG  > 4:
                        if fly5 == 'x':
                            shipLocation = dataListPlanetsC[4]
                            fuelAmount = fuelAmount - dataListDistancesC[4]                          
                    if lengthG  > 5:
                        if fly6 == 'x':
                            shipLocation = dataListPlanetsC[5]
                            fuelAmount = fuelAmount - dataListDistancesC[5]
                            
                    if fuelAmount < 1:
            
                        Option.activateRescue(self)
       
                def activateSpEvent(self):

                    self.master.destroy()

                    Option.activateCombat(self)

            LocationToLocation()

            self.__init__()
 
#F - Jump to New System
  
        def activateJump(self):

            global shipSystem
            global shipLocation
            global fuelAmount
            
            fuelAmount = fuelAmount - 5

            checker = 0
            
            self.master.destroy()
                                 
            if fuelAmount < 1:
            
                Option.activateRescue(self)
            
            lengthJ = len(dataListJumps)
            for mark in range (0, lengthJ):

                if checker == 0:
          
                    if shipSystem == dataListJumps[mark][0] and shipLocation == dataListJumps[mark][1]:
                        shipSystem = dataListJumps[mark][2]
                        shipLocation = dataListJumps[mark][3]
                        checker = 1
                        
#G - Rescued due to No Fuel

        def activateRescue(self):   
            
            lengthR = len(dataListRescue)
            
            global fuelAmount
            global shipSystem
            global shipLocation
            global bankAmount
            
            mark = 0
            
            while fuelAmount < 1:
            
                if shipSystem == dataListRescue[mark][0]:
                        
                    shipSystem = dataListRescue[mark][1]
                    shipLocation = dataListRescue[mark][2]
                        
                    if bankAmount > 0:
                        bankAmount = bankAmount - 2000
                            
                    else:
                        bankAmount = 0
                            
                    fuelAmount = 100

                    class ShipRescue:

                        def __init__(self):
                            self.master = Tk()
                            self.master.title('Rescue Outcome')
                            self.master.geometry('300x100+50+50')
                            self.master.configure(bg = "#FFFFFF" )
                    
                            self.activateButton = Button(self.master, text = 'Press to Fly',command = self.activateEntry)
                            self.activateButton.place(x = 10, y = 0)
                            self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')

                            self.labelEntry1L = Label(self.master, text = 'You ran out of fuel')
                            self.labelEntry1L.place(x = 10, y = 30)
                            self.labelEntry1L.configure(bg = '#FFFFFF')
                                
                            self.labelEntry2L = Label(self.master, text = 'You are rescued by the Imperial Navy')
                            self.labelEntry2L.place(x = 10, y = 55)
                            self.labelEntry2L.configure(bg = '#FFFFFF')

                            self.master.mainloop()
                                       
                        def activateEntry(self):
                
                            self.master.destroy()
                         
                    ShipRescue()                 
               
                else:
                  
                    mark = mark + 1 
  
#K - Landing Operations

        def activateLand(self):
                
            self.master.destroy()
            
            class LandPlanet:

                def __init__(self):
                    self.master = Tk()
                    self.master.title('Planetary Utilities Options')
                    self.master.geometry('300x145+50+50')
                    self.master.configure(bg = "#FFFFFF" )
                    
                    self.activateButton = Button(self.master, text = 'Press to Fly',command = self.activateEntry)
                    self.activateButton.place(x = 10, y = 0)
                    self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
                    
                    self.Option1B = Button(self.master, text = '[#]',command = self.repairShip)
                    self.Option1B.place(x = 10, y = 30)
                    self.Option1B.configure(fg = '#FF0000', bg = '#FFFFFF')

                    self.labelEntry1L = Label(self.master, text = 'You can repair your ship at 100c per 1 hp')
                    self.labelEntry1L.place(x = 40, y = 30)
                    self.labelEntry1L.configure(bg = '#FFFFFF')

                    self.Option2B = Button(self.master, text = '[#]',command = self.buyMissiles)
                    self.Option2B.place(x = 10, y = 55)
                    self.Option2B.configure(fg = '#FF0000', bg = '#FFFFFF')

                    self.labelEntry2L = Label(self.master, text = 'You can buy missiles at 125c each')
                    self.labelEntry2L.place(x = 40, y =55)
                    self.labelEntry2L.configure(bg = '#FFFFFF')
                    
                    self.Option3B = Button(self.master, text = '[#]',command = self.cashBounty)
                    self.Option3B.place(x = 10, y = 80)
                    self.Option3B.configure(fg = '#FF0000', bg = '#FFFFFF')

                    self.labelEntry3L = Label(self.master, text = 'You can buy cash in bounties for 500c each')
                    self.labelEntry3L.place(x = 40, y = 80)
                    self.labelEntry3L.configure(bg = '#FFFFFF')
         
                    self.Option3B = Button(self.master, text = '[#]',command = self.reFuel)
                    self.Option3B.place(x = 10, y = 105)
                    self.Option3B.configure(fg = '#FF0000', bg = '#FFFFFF')

                    self.labelEntry3L = Label(self.master, text = 'You can refuel at 10c per unit')
                    self.labelEntry3L.place(x = 40, y = 105)
                    self.labelEntry3L.configure(bg = '#FFFFFF')
                                                 
                    self.master.mainloop()
                                       
                def activateEntry(self):
                
                    self.master.destroy()

#K1 - Repair Ship
            
                def repairShip(self):
                         
                  self.master.destroy()
                  
                  class RepairShip:
                      
                      def __init__(self):
                         
                         global hullPoints
                         global bankAmount
                          
                         amountRepair = 25 - hullPoints
                                                    
                         bankAmount = bankAmount - 100 * amountRepair
                              
                         hullPoints = 25
                         
                         self.master = Tk()
                         self.master.title('Ship Repared')
                         self.master.geometry('260x70+50+50')
                         self.master.configure(bg = "#FFFFFF" )
                        
                         self.labelEntry2L = Label(self.master, text = 'Ship repaired - ' + str(amountRepair) + ' points')
                         self.labelEntry2L.place(x = 10, y =0)
                         self.labelEntry2L.configure(bg = '#FFFFFF')
                         
                         self.activateButtonRP = Button(self.master, text = 'Press to Complete',command = self.activateEntry)
                         self.activateButtonRP.place(x = 10, y = 30)
                         self.activateButtonRP.configure(fg = '#FF0000', bg = '#FFFFFF')
                          
                         self.master.mainloop()
                         
                      def activateEntry(self):
                      
                         self.master.destroy()
                         
                  RepairShip()

                  self.__init__()  
        
#K2 - Buy Missiles
                  
                def buyMissiles(self):
                            
                  self.master.destroy()
                     
                  class BuyMissiles:
                         
                     def __init__(self):

                        global missilesArmed

                        amountMissiles = 10 - missilesArmed
                            
                        self.master = Tk()
                        self.master.title('Buy Missiles')
                        self.master.geometry('260x60+50+50')
                        self.master.configure(bg = "#FFFFFF" )
                                                                 
                        self.activateButtonBM = Button(self.master, text = 'Press to Buy',command = self.activateEntry)
                        self.activateButtonBM.place(x = 10, y = 30)
                        self.activateButtonBM.configure(fg = '#FF0000', bg = '#FFFFFF')

                        self.labelEntryAM = Label(self.master, text = 'You can buy upto ' + str(amountMissiles) + ' missiles')
                        self.labelEntryAM.place(x = 10, y = 0)
                        self.labelEntryAM.configure(bg = '#FFFFFF')

                        self.variableAM = StringVar()
                        self.labelEntryAM = Entry(self.master, textvariable = self.variableAM)
                        self.labelEntryAM.place(x = 170, y = 0) 

                        self.master.mainloop()
                            
                     def activateEntry(self):

                        global missilesArmed
                        global bankAmount
                         
                        self.master.destroy()

                        newmissiles = self.variableAM.get()

                        missilesArmed = missilesArmed + int(newmissiles)
                        
                        bankAmount = bankAmount - 125 * int(newmissiles)                            
                            
                  BuyMissiles()

                  self.__init__()
                  
 #K3 - Cash in Bounties
                  
                def cashBounty(self):
                            
                  self.master.destroy()
                     
                  class CashBounty:
                         
                     def __init__(self):

                        global bountyLevel

                        self.master = Tk()
                        self.master.title('Cash In Bounties')
                        self.master.geometry('260x60+50+50')
                        self.master.configure(bg = "#FFFFFF" )
                                                                 
                        self.activateButtonBM = Button(self.master, text = 'Press to Cash In',command = self.activateEntry)
                        self.activateButtonBM.place(x = 10, y = 30)
                        self.activateButtonBM.configure(fg = '#FF0000', bg = '#FFFFFF')

                        self.labelEntryAM = Label(self.master, text = 'You have ' + str(bountyLevel) + ' bounties to cash in')
                        self.labelEntryAM.place(x = 10, y = 0)
                        self.labelEntryAM.configure(bg = '#FFFFFF')

                        self.master.mainloop()
                            
                     def activateEntry(self):

                        global bountyLevel
                        global bankAmount
                         
                        self.master.destroy()
                        
                        bankAmount = bankAmount + 500 * int(bountyLevel)
                        
                        bountyLevel = 0
                            
                  CashBounty()

                  self.__init__()
                  
#K4 - Fill up with Fuel
                  
                def reFuel(self):
                            
                  self.master.destroy()
                     
                  class FillUp:  
                         
                     def __init__(self):
                                            
                        global fuelAmount
                        global bankAmount
                                                      
                        bankAmount = bankAmount - (100 - fuelAmount) * 10
                            
                        self.master = Tk()
                        self.master.title('Refuel')
                        self.master.geometry('260x60+50+50')
                        self.master.configure(bg = "#FFFFFF" )
                                                                 
                        self.activateButtonBM = Button(self.master, text = 'Press to Complete',command = self.activateEntry)
                        self.activateButtonBM.place(x = 10, y = 30)
                        self.activateButtonBM.configure(fg = '#FF0000', bg = '#FFFFFF')

                        self.labelEntryAM = Label(self.master, text = 'Your current fuel level was ' + str(fuelAmount) + ' units')
                        self.labelEntryAM.place(x = 10, y = 0)
                        self.labelEntryAM.configure(bg = '#FFFFFF')
                        
                        fuelAmount = 100

                        self.master.mainloop()
                            
                     def activateEntry(self):
                                             
                        self.master.destroy()
                            
                  FillUp()

                  self.__init__()

            LandPlanet()
            
#L - Operations in an Asteroid Belt

        def activateAFEvent(self):
                
            self.master.destroy()
            
            class AFEvent:

                def __init__(self):
                    self.master = Tk()
                    self.master.title('Asteroid Field Event')
                    self.master.geometry('260x100+50+50')
                    self.master.configure(bg = "#FFFFFF" )
                    
                    indexEvent = random.randint(1,10)
                   
                    if indexEvent == 7 or indexEvent == 8:                                   
                        self.activateButton = Button(self.master, text = 'Engagement Options',command = self.activateEngage)
                        self.activateButton.place(x = 10, y = 0)
                        self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')

                    else:
                        self.activateButton = Button(self.master, text = 'Press to Fly',command = self.activateEntry)
                        self.activateButton.place(x = 10, y = 0)
                        self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
 
                    global cargoCapacity
                    global dataListCargo
                    global bankAmount

                    findCounter = 0
                    spaceCounter = 0

                    allowedCargo = cargoCapacity - numberPackages
                    
                    for mark in range(0, 4):
                        allowedCargo = allowedCargo - dataListCargo[mark][2]
                    
                    if indexEvent < 7:
                        
                        oreFind = 3 + random.randint(1,6) - 2 * findCounter
                                                
                        findCounter = findCounter + 1
                        
                        if oreFind < 0:
                            
                            oreFind = 0
                        
                        self.labelEntryTSl = Label(self.master, text = 'You find ' + str(oreFind) + ' ore')
                        self.labelEntryTSl.place(x = 10, y = 30)
                        self.labelEntryTSl.configure(bg = '#FFFFFF')

                        if oreFind > allowedCargo:
                            
                           oreFind = allowedCargo

                           self.labelEntryTSl = Label(self.master, text = 'You only have room for ' + str(oreFind) + ' ore')
                           self.labelEntryTSl.place(x = 10, y = 50)
                           self.labelEntryTSl.configure(bg = '#FFFFFF')
                           
                        for mark in range(0, 4):

                            if spaceCounter == 0:
                            
                                if dataListCargo[mark][1] == 'None' or dataListCargo[mark][1] == 'Ore':
                                    
                                    dataListCargo[mark][1] = 'Ore'
                                    dataListCargo[mark][2] = dataListCargo[mark][2] + oreFind
                                    
                                    spaceCounter = spaceCounter + 1
                    
                    elif indexEvent == 7 or indexEvent == 8:

                        global asteroidEnemyDefence

                        asteroidEnemyDefence = 20
                        
                        if indexEvent == 7:
                            self.labelEntryTSl = Label(self.master, text = 'You are attacked by a space monster')
                            self.labelEntryTSl.place(x = 10, y = 30)
                            self.labelEntryTSl.configure(bg = '#FFFFFF')
                        
                        if indexEvent == 8:
                            
                            self.labelEntryTSl = Label(self.master, text = 'You are attacked by pirates')
                            self.labelEntryTSl.place(x = 10, y = 30)
                            self.labelEntryTSl.configure(bg = '#FFFFFF')
  
                    elif indexEvent == 9:
                        
                        wreckValue = random.randint(1,6) * 200
                        bankAmount = bankAmount + wreckValue
                        
                        self.labelEntryTSl = Label(self.master, text = 'You are find a space wreck worth ' + str(wreckValue) + ' credits')
                        self.labelEntryTSl.place(x = 10, y = 30)
                        self.labelEntryTSl.configure(bg = '#FFFFFF')
                            
                    elif indexEvent == 10:
                        
                        gemFind = random.randint(1,4)
                                                     
                        self.labelEntryTSl = Label(self.master, text = 'You find ' + str(gemFind) + ' gem stones')
                        self.labelEntryTSl.place(x = 10, y = 30)
                        self.labelEntryTSl.configure(bg = '#FFFFFF')

                        if gemFind > allowedCargo:
                            
                           gemFind = allowedCargo

                           self.labelEntryTSl = Label(self.master, text = 'You only have room for ' + str(gemFind) + ' gemstones')
                           self.labelEntryTSl.place(x = 10, y = 50)
                           self.labelEntryTSl.configure(bg = '#FFFFFF')
                        
                        for mark in range(0, 4):

                            if spaceCounter == 0:
                            
                                if dataListCargo[mark][1] == 'None' or dataListCargo[mark][1] == 'Gem Stones':
                                    
                                    dataListCargo[mark][1] = 'Gem Stones'
                                    dataListCargo[mark][2] = dataListCargo[mark][2] + gemFind
                        
                                    spaceCounter = findCounter + 1
                       
                    self.master.mainloop()
                    
                def activateEntry(self):
                
                    self.master.destroy()
           
                def activateEngage(self):
                
                    self.master.destroy()
                    
                    Option.activateCombat(self)
                
            AFEvent()
            
#Q - Combat
                   
        def activateCombat(self):

            class AFEngage:
                        
                def __init__(self):
                    self.master = Tk()
                    self.master.title('Retreat Option')
                    self.master.geometry('260x50+50+50')
                    self.master.configure(bg = "#FFFFFF" )
                               
                    self.activateButton1 = Button(self.master, text = 'Retreat', command = self.activateRetreat)
                    self.activateButton1.place(x = 10, y = 10)
                    self.activateButton1.configure(fg = '#FF0000', bg = '#FFFFFF')
 
                    self.activateButton1 = Button(self.master, text = 'Attack', command = self.activateAttack)
                    self.activateButton1.place(x = 70, y = 10)
                    self.activateButton1.configure(fg = '#FF0000', bg = '#FFFFFF')
                    
#Q1 - Retreat
        
                def activateRetreat(self):
                        
                    self.master.destroy()
                            
                    class AFRetreat:
        
                        def __init__(self):
                            self.master = Tk()
                            self.master.title('Retreat Option')
                            self.master.geometry('260x70+50+50')
                            self.master.configure(bg = "#FFFFFF" )
                                                
                            self.activateButton = Button(self.master, text = 'Press to Confirm',command = self.activateXEntry)
                            self.activateButton.place(x = 10, y = 0)
                            self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
                                                        
                            global shipSystem
                            global shipLocation
                            global dataListCargo
                            global bankAmount
                            global hullPoints
                                     
                            damage = random.randint(1,6)
                                   
                            hullPoints = hullPoints - damage                       
                               
                            if hullPoints > 0:
                                    
                                self.labelEntryAFR = Label(self.master, text = 'You take ' + str(damage) + ' points damage')
                                self.labelEntryAFR.place(x = 10, y = 30)
                                self.labelEntryAFR.configure(bg = '#FFFFFF')
         
                            else:
                                                        
                                self.master.destroy()
                                Option.activateRespawn(self)
                                
                            self.master.mainloop()
                                                     
                        def activateXEntry(self):
                        
                            self.master.destroy()
        
                    AFRetreat()                       
  
#Q2 - Attack                             
                def activateAttack(self):
         
                    self.master.destroy()
                           
                    class AFAttack:
        
                        def __init__(self):
                            self.master = Tk()
                            self.master.title('Attack Option')
                            self.master.geometry('260x80+50+50')
                            self.master.configure(bg = "#FFFFFF" )
                                                
                            self.activateButton = Button(self.master, text = 'Press to Confirm',command = self.activateATEntry)
                            self.activateButton.place(x = 10, y = 0)
                            self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
                            
                            self.labelEntryAFA1 = Label(self.master, text = 'You can fire lasers')
                            self.labelEntryAFA1.place(x = 10, y = 30)
                            self.labelEntryAFA1.configure(bg = '#FFFFFF')
         
                            self.variableF = StringVar()
                            self.labelEntryF = Entry(self.master, textvariable = self.variableF)
                            self.labelEntryF.place(x = 165, y = 30)
                                    
                            self.labelEntryAFA2 = Label(self.master, text = 'You can fire missiles <' + str(missilesArmed) + '>')
                            self.labelEntryAFA2.place(x = 10, y = 55)
                            self.labelEntryAFA2.configure(bg = '#FFFFFF')
         
                            self.variableM = StringVar()
                            self.labelEntryM = Entry(self.master, textvariable = self.variableM)
                            self.labelEntryM.place(x = 165, y = 55)
        
                            self.master.mainloop()
                                                     
                        def activateATEntry(self):

                            self.master.destroy()
                                                    
                            laserFire = self.variableF.get()
                            missileFire = self.variableM.get()
                                    
                            global missilesArmed
                                    
                            missilesArmed = missilesArmed - int(missileFire)
                                                        
                            global shipSystem
                            global shipLocation
                            global dataListCargo
                            global bankAmount
                            global hullPoints

                            global asteroidEnemyDefence                                    
                                     
                            damage = random.randint(1,6)
                                   
                            hullPoints = hullPoints - damage
                                    
                            if laserFire == 'x':
                                damageV = random.randint(1,6) + 3
                                   
                            else:
                                damageV = 0
                                        
                            damageV = damageV + 4 * int(missileFire)
                                    
                            asteroidEnemyDefence = asteroidEnemyDefence - damageV
                                    
                            class AFBattleOutcome:
        
                                def __init__(self):
                                    self.master = Tk()
                                    self.master.title('Battle Outcome')
                                    self.master.geometry('260x140+50+50')
                                    self.master.configure(bg = "#FFFFFF" )
                                                                               
                                    self.activateButton = Button(self.master, text = 'Press to Confirm',command = self.activateBCExit)
                                    self.activateButton.place(x = 10, y = 0)
                                    self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
                                           
                                    global hullPoints
                                                        
                                    if hullPoints > 0:
                                        
                                        self.labelEntryAFA1 = Label(self.master, text = 'You take ' + str(damage) + ' points damage')
                                        self.labelEntryAFA1.place(x = 10, y = 30)
                                        self.labelEntryAFA1.configure(bg = '#FFFFFF')
                                           
                                        if asteroidEnemyDefence > 0:
                                            self.labelEntryAFA1 = Label(self.master, text = 'Your opponent took ' + str(damageV) + ' points damage')
                                            self.labelEntryAFA1.place(x = 10, y = 55)
                                            self.labelEntryAFA1.configure(bg = '#FFFFFF')
        
                                        else:
                                            self.labelEntryAFA1 = Label(self.master, text = 'Your opponent is destroyed')
                                            self.labelEntryAFA1.place(x = 10, y = 55)
                                            self.labelEntryAFA1.configure(bg = '#FFFFFF')
                                                 
                                            global bountyLevel
                                                 
                                            bountyLevel = bountyLevel + 1
                                                 
                                            self.labelEntryAFA1 = Label(self.master, text = 'Your current fame is level ' + str(victoryFame))
                                            self.labelEntryAFA1.place(x = 10, y = 105)
                                            self.labelEntryAFA1.configure(bg = '#FFFFFF')
                                                 
                                        self.labelEntryAFA1 = Label(self.master, text = 'Your current defence is ' + str(hullPoints))
                                        self.labelEntryAFA1.place(x = 10, y = 80)
                                        self.labelEntryAFA1.configure(bg = '#FFFFFF')
             
                                    else:
                                        
                                        self.master.destroy()
                                        Option.activateRespawn(self)
             
                                    self.master.mainloop()
                                                         
                                def activateBCExit(self):
                        
                                    self.master.destroy()
                                             
                            AFBattleOutcome()
                                    
                    AFAttack()

                    global asteroidEnemyDefence

                    if asteroidEnemyDefence > 0:

                        self.__init__()
                                         
            AFEngage()

#R- Respawning

        def activateRespawn(self):
                                   
            class Respawn:

                def __init__(self):
                    self.master = Tk()
                    self.master.title('Respawning')
                    self.master.geometry('260x80+50+50')
                    self.master.configure(bg = "#FFFFFF" )
                                                                               
                    self.activateButton = Button(self.master, text = 'Press to Confirm',command = self.activateExit)
                    self.activateButton.place(x = 10, y = 0)
                    self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
   
                    self.labelEntryD = Label(self.master, text = 'You are destroyed, losing all cargo!!')
                    self.labelEntryD.place(x = 10, y = 30)
                    self.labelEntryD.configure(bg = '#FFFFFF')
                                           
                    self.labelEntryS = Label(self.master, text = 'You respawn on Terra in the Sol system')
                    self.labelEntryS.place(x = 10, y = 55)
                    self.labelEntryS.configure(bg = '#FFFFFF')
                                                                               
                    global shipSystem
                    global shipLocation
                    global dataListCargo
                    global bankAmount
                    global hullPoints

                    shipSystem = 'Sol'
                    shipLocation = 'Terra'
                    hullPoints = 25
                                           
                    if bankAmount > 5000:
                        if bankAmount > 10000:
                            bankAmount = bankAmount - 5000
                        else:
                            bankAmount = bankAmount - 2500
                            
                    else:
                        bankAmount = bankAmount/2
            
                    dataListCargo = [['Slot 1','None',0,0],['Slot 2','None',0,0],['Slot 3','None',0,0],['Slot 4','None',0,0]]
                                                     
                def activateExit(self):
                        
                    self.master.destroy()
           
            Respawn()
                                                        
#V - Trading

        def activateTrade(self):
                
            self.master.destroy()

            lengthConfig = len(dataListSystems)

            for mark in range(0,lengthConfig):
               if dataListSystems[mark][1] == shipLocation:
                  planetType = dataListSystems[mark][2]

#V1 - Selling Set Up

            length = len(dataListSPrices)
              
            for mark in range (0,4):            
              
               for counter in range (0,length):

                     if planetType == 'M':
                        if dataListCargo[mark][1] == dataListSPrices[counter][0]:
                           dataListCargo[mark][3] = dataListSPrices[counter][5]
                    
                     if planetType == 'R':
                        if dataListCargo[mark][1] == dataListSPrices[counter][0]:
                           dataListCargo[mark][3] = dataListSPrices[counter][6]
                    
                     if planetType == 'G':
                        if dataListCargo[mark][1] == dataListSPrices[counter][0]:
                           dataListCargo[mark][3] = dataListSPrices[counter][7]
                    
                     if planetType == 'SB':
                        if dataListCargo[mark][1] == dataListSPrices[counter][0]:
                           dataListCargo[mark][3] = dataListSPrices[counter][8]

#V2 - Selling Operations

            class SellCargo:
            
                def __init__(self):
                    self.master = Tk()
                    self.master.title('Selling Cargo at ' + shipLocation)
                    self.master.geometry('380x150+50+50')
                    self.master.configure(bg = "#FFFFFF" )
            
#V21 - Display Widgits
            
                    self.labelEntryTSl = Label(self.master, text = 'Ship')
                    self.labelEntryTSl.place(x = 10, y = 0)
                    self.labelEntryTSl.configure(bg = '#FFFFFF')
                    
                    self.labelEntry1 = Label(self.master, text = 'Slot 1')
                    self.labelEntry1.place(x = 10, y = 20)
                    self.labelEntry1.configure(bg = '#FFFFFF')
            
                    self.labelEntry2 = Label(self.master, text = 'Slot 2')
                    self.labelEntry2.place(x = 10, y = 40)
                    self.labelEntry2.configure(bg = '#FFFFFF')
            
                    self.labelEntry3 = Label(self.master, text = 'Slot 3')
                    self.labelEntry3.place(x = 10, y = 60)
                    self.labelEntry3.configure(bg = '#FFFFFF')
            
                    self.labelEntry4 = Label(self.master, text = 'Slot 4')
                    self.labelEntry4.place(x = 10, y = 80)
                    self.labelEntry4.configure(bg = '#FFFFFF')
               
                    self.labelEntry1TTG = Label(self.master, text = 'T Good')
                    self.labelEntry1TTG.place(x = 50, y = 0)
                    self.labelEntry1TTG.configure(bg = '#FFFFFF')
            
                    self.labelEntry1C = Label(self.master, text = dataListCargo[0][1])
                    self.labelEntry1C.place(x = 50, y = 20)
                    self.labelEntry1C.configure(bg = '#FFFFFF')
            
                    self.labelEntry2C = Label(self.master, text = dataListCargo[1][1])
                    self.labelEntry2C.place(x = 50, y = 40)
                    self.labelEntry2C.configure(bg = '#FFFFFF')
            
                    self.labelEntry3C = Label(self.master, text = dataListCargo[2][1])
                    self.labelEntry3C.place(x = 50, y = 60)
                    self.labelEntry3C.configure(bg = '#FFFFFF')
            
                    self.labelEntry4C = Label(self.master, text = dataListCargo[3][1])
                    self.labelEntry4C.place(x = 50, y = 80)
                    self.labelEntry4C.configure(bg = '#FFFFFF')
            
                    self.labelEntryTA = Label(self.master, text = 'Amount')
                    self.labelEntryTA.place(x = 125, y = 0)
                    self.labelEntryTA.configure(bg = '#FFFFFF')
                    
                    self.labelEntry1A = Label(self.master, text = dataListCargo[0][2])
                    self.labelEntry1A.place(x = 125, y = 20)
                    self.labelEntry1A.configure(bg = '#FFFFFF')
            
                    self.labelEntry2A = Label(self.master, text = dataListCargo[1][2])
                    self.labelEntry2A.place(x = 125, y = 40)
                    self.labelEntry2A.configure(bg = '#FFFFFF')
            
                    self.labelEntry3A = Label(self.master, text = dataListCargo[2][2])
                    self.labelEntry3A.place(x = 125, y = 60)
                    self.labelEntry3A.configure(bg = '#FFFFFF')
             
                    self.labelEntry4A = Label(self.master, text = dataListCargo[3][2])
                    self.labelEntry4A.place(x = 125, y = 80)
                    self.labelEntry4A.configure(bg = '#FFFFFF')
                
                    self.labelEntryTP = Label(self.master, text = 'Price')
                    self.labelEntryTP.place(x = 190, y = 0)
                    self.labelEntryTP.configure(bg = '#FFFFFF')
                    
                    self.labelEntry1P = Label(self.master, text = dataListCargo[0][3])
                    self.labelEntry1P.place(x = 190, y = 20)
                    self.labelEntry1P.configure(bg = '#FFFFFF')
            
                    self.labelEntry2P = Label(self.master, text = dataListCargo[1][3])
                    self.labelEntry2P.place(x = 190, y = 40)
                    self.labelEntry2P.configure(bg = '#FFFFFF')
            
                    self.labelEntry3P = Label(self.master, text = dataListCargo[2][3])
                    self.labelEntry3P.place(x = 190, y = 60)
                    self.labelEntry3P.configure(bg = '#FFFFFF')
                    
                    self.labelEntry4P = Label(self.master, text = dataListCargo[3][3])
                    self.labelEntry4P.place(x = 190, y = 80)
                    self.labelEntry4P.configure(bg = '#FFFFFF')
                    
                    self.labelEntryTIn = Label(self.master, text = 'Sale Quantity')
                    self.labelEntryTIn.place(x = 250, y = 0)
                    self.labelEntryTIn.configure(bg = '#FFFFFF')
            
                    self.variable1B = StringVar()
                    self.labelEntry1B = Entry(self.master, textvariable = self.variable1B)
                    self.labelEntry1B.place(x = 250, y = 20)
            
                    self.variable2B = StringVar()
                    self.labelEntry2B = Entry(self.master, textvariable = self.variable2B)
                    self.labelEntry2B.place(x = 250, y = 40)
            
                    self.variable3B = StringVar()
                    self.labelEntry3B = Entry(self.master, textvariable = self.variable3B)
                    self.labelEntry3B.place(x = 250, y = 60)
               
                    self.variable4B = StringVar()
                    self.labelEntry4B = Entry(self.master, textvariable = self.variable4B)
                    self.labelEntry4B.place(x = 250, y = 80) 
                        
                    self.activateButton = Button(self.master, text = 'Press to Trade',command = self.activateEntry)
                    self.activateButton.place(x = 10, y = 110)
                    self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
            
                    self.master.mainloop()

#V22 - Selling Transactions
                    
                def activateEntry(self):
                    
                    self.master.destroy()
              
                    saleamount1 = self.variable1B.get()
                    saleamount2 = self.variable2B.get()
                    saleamount3 = self.variable3B.get()
                    saleamount4 = self.variable4B.get()
                    
                    global bankAmount
            
                    if saleamount1 != '':
                        dataListCargo[0][2]  = int(dataListCargo[0][2]) - int(saleamount1)
                        bankAmount = bankAmount + int(saleamount1) * int(dataListCargo[0][3])
                    if saleamount2 != '':
                        dataListCargo[1][2]  = int(dataListCargo[1][2]) - int(saleamount2)
                        bankAmount = bankAmount + int(saleamount2) * int(dataListCargo[1][3])
                    if saleamount3 != '':
                        dataListCargo[2][2]  = int(dataListCargo[2][2]) - int(saleamount3)
                        bankAmount = bankAmount + int(saleamount3) * int(dataListCargo[2][3])
                    if saleamount4 != '':
                        dataListCargo[3][2]  = int(dataListCargo[3][2]) - int(saleamount4)
                        bankAmount = bankAmount + int(saleamount4) * int(dataListCargo[3][3])
            
                    for mark in range(0,4):
                        if dataListCargo[mark][2] == 0:
                            dataListCargo[mark][1] = 'None'
                            dataListCargo[mark][3] = 0
                    
            SellCargo()

#V3 - Purchasing Operations
  
#V31 - Purchasing Set Up
           
            displayListTGCP = []

            length = len(dataListSPrices)        
              
            for mark in range (0,length):

               typeG = dataListSPrices[mark][0]

               if planetType == 'M':
                  price = dataListSPrices[mark][1]
                             
               if planetType == 'R':
                  price = dataListSPrices[mark][2]
                        
               if planetType == 'G':
                  price = dataListSPrices[mark][3]
                        
               if planetType == 'SB':
                  price = dataListSPrices[mark][4]

               amount = dataListSPrices[mark][9]

               combo = [typeG, price, amount]
               
               displayListTGCP = displayListTGCP + [combo]
   
            length = len(displayListTGCP) - 1
            
            for mark in range(length, -1, -1):

               if displayListTGCP[mark][1] == 0:
                  del displayListTGCP[mark]   
            
            class PurchaseCargo:
            
                def __init__(self):
                    self.master = Tk()
                    self.master.title('Purchasing Trade Goods at ' + shipLocation)
                    self.master.geometry('380x345+50+50')
                    self.master.configure(bg = "#FFFFFF" )
            
#V32 - Display Widgits
            
                    global cargoCapacity
                    global numberPackages

                    allowedCargo = cargoCapacity - numberPackages
                    
                    for mark in range(0, 4):
                        allowedCargo = allowedCargo - dataListCargo[mark][2]
            
                    self.labelallowed = Label(self.master, text = 'You can purchase trade goods up to ' + str(allowedCargo) + ' units')
                    self.labelallowed.place(x = 10, y = 0)
                    self.labelallowed.configure(bg = '#FFFFFF')
                    
                    self.labelallowed = Label(self.master, text = 'You are have ' + str(bankAmount) + ' credits')
                    self.labelallowed.place(x = 10, y = 20)
                    self.labelallowed.configure(bg = '#FFFFFF')
                    
                    self.labelEntryTSl = Label(self.master, text = 'Current Cargo')
                    self.labelEntryTSl.place(x = 10, y = 45)
                    self.labelEntryTSl.configure(bg = '#FFFFFF')
            
                    self.labelEntryTSl = Label(self.master, text = 'Ship')
                    self.labelEntryTSl.place(x = 10, y = 65)
                    self.labelEntryTSl.configure(bg = '#FFFFFF')
                    
                    self.labelEntry1 = Label(self.master, text = 'Slot 1')
                    self.labelEntry1.place(x = 10, y = 85)
                    self.labelEntry1.configure(bg = '#FFFFFF')
            
                    self.labelEntry2 = Label(self.master, text = 'Slot 2')
                    self.labelEntry2.place(x = 10, y = 105)
                    self.labelEntry2.configure(bg = '#FFFFFF')
            
                    self.labelEntry3 = Label(self.master, text = 'Slot 3')
                    self.labelEntry3.place(x = 10, y =125)
                    self.labelEntry3.configure(bg = '#FFFFFF')
                
                    self.labelEntry4 = Label(self.master, text = 'Slot 4')
                    self.labelEntry4.place(x = 10, y =145)
                    self.labelEntry4.configure(bg = '#FFFFFF')
                    
                    self.labelEntry1TTG = Label(self.master, text = 'Trade Good')
                    self.labelEntry1TTG.place(x = 50, y = 65)
                    self.labelEntry1TTG.configure(bg = '#FFFFFF')
            
                    self.labelEntry1C = Label(self.master, text = dataListCargo[0][1])
                    self.labelEntry1C.place(x = 50, y = 85)
                    self.labelEntry1C.configure(bg = '#FFFFFF')
            
                    self.labelEntry2C = Label(self.master, text = dataListCargo[1][1])
                    self.labelEntry2C.place(x = 50, y = 105)
                    self.labelEntry2C.configure(bg = '#FFFFFF')
            
                    self.labelEntry3C = Label(self.master, text = dataListCargo[2][1])
                    self.labelEntry3C.place(x = 50, y = 125)
                    self.labelEntry3C.configure(bg = '#FFFFFF')
             
                    self.labelEntry4C = Label(self.master, text = dataListCargo[3][1])
                    self.labelEntry4C.place(x = 50, y = 145)
                    self.labelEntry4C.configure(bg = '#FFFFFF')
                 
                    self.labelEntryTA = Label(self.master, text = 'Amount')
                    self.labelEntryTA.place(x = 125, y = 65)
                    self.labelEntryTA.configure(bg = '#FFFFFF')
                    
                    self.labelEntry1A = Label(self.master, text = dataListCargo[0][2])
                    self.labelEntry1A.place(x = 125, y = 85)
                    self.labelEntry1A.configure(bg = '#FFFFFF')
            
                    self.labelEntry2A = Label(self.master, text = dataListCargo[1][2])
                    self.labelEntry2A.place(x = 125, y = 105)
                    self.labelEntry2A.configure(bg = '#FFFFFF')
            
                    self.labelEntry3A = Label(self.master, text = dataListCargo[2][2])
                    self.labelEntry3A.place(x = 125, y = 125)
                    self.labelEntry3A.configure(bg = '#FFFFFF')
                    
                    self.labelEntry4A = Label(self.master, text = dataListCargo[3][2])
                    self.labelEntry4A.place(x = 125, y = 145)
                    self.labelEntry4A.configure(bg = '#FFFFFF')
                
                    self.activateButton = Button(self.master, text = 'Press to Trade', command = self.activateEntry )
                    self.activateButton.place(x = 10, y = 175)
                    self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
            
                    lengthTGCP = len(displayListTGCP)
                    
                    self.labelEntryTTG = Label(self.master, text = 'T Good')
                    self.labelEntryTTG.place(x = 10, y = 205)
                    self.labelEntryTTG.configure(bg = '#FFFFFF')       
                          
                    self.labelEntryTP = Label(self.master, text = 'Price')
                    self.labelEntryTP.place(x = 85, y = 205)
                    self.labelEntryTP.configure(bg = '#FFFFFF')
                       
                    self.labelEntryTA = Label(self.master, text = 'Amount')
                    self.labelEntryTA.place(x = 130, y = 205)
                    self.labelEntryTA.configure(bg = '#FFFFFF')
                    
                    self.labelEntryTQ = Label(self.master, text = 'Quantity')
                    self.labelEntryTQ.place(x = 195, y = 205)
                    self.labelEntryTQ.configure(bg = '#FFFFFF')
                               
                    self.labelEntryTS = Label(self.master, text = 'Slot')
                    self.labelEntryTS.place(x = 265, y = 205)
                    self.labelEntryTS.configure(bg = '#FFFFFF')
             
                    self.labelEntry1 = Label(self.master, text = displayListTGCP[0][0])
                    self.labelEntry1.place(x = 10, y = 225)
                    self.labelEntry1.configure(bg = '#FFFFFF')
                    
                    self.labelEntry1P = Label(self.master, text = displayListTGCP[0][1])
                    self.labelEntry1P.place(x = 85, y = 225)
                    self.labelEntry1P.configure(bg = '#FFFFFF')
                    
                    self.labelEntry1A = Label(self.master, text = displayListTGCP[0][2])
                    self.labelEntry1A.place(x = 130, y = 225)
                    self.labelEntry1A.configure(bg = '#FFFFFF')
                 
                    self.variable1Q = StringVar()
                    self.labelEntry1Q = Entry(self.master, textvariable = self.variable1Q)
                    self.labelEntry1Q.place(x = 195, y = 225)
                  
                    self.variable1S = StringVar()
                    self.labelEntry1S = Entry(self.master, textvariable = self.variable1S)
                    self.labelEntry1S.place(x = 265, y = 225)
                    
                    self.labelEntry2 = Label(self.master, text =  displayListTGCP[1][0])
                    self.labelEntry2.place(x = 10, y = 245)
                    self.labelEntry2.configure(bg = '#FFFFFF')
            
                    self.labelEntry2P = Label(self.master, text = displayListTGCP[1][1])
                    self.labelEntry2P.place(x = 85, y = 245)
                    self.labelEntry2P.configure(bg = '#FFFFFF')
             
                    self.labelEntry2A = Label(self.master, text = displayListTGCP[1][2])
                    self.labelEntry2A.place(x = 130, y = 245)
                    self.labelEntry2A.configure(bg = '#FFFFFF')
            
                    self.variable2Q = StringVar()
                    self.labelEntry2Q = Entry(self.master, textvariable = self.variable2Q)
                    self.labelEntry2Q.place(x = 195, y = 245)
                    
                    self.variable2S = StringVar()
                    self.labelEntry2S = Entry(self.master, textvariable = self.variable2S)
                    self.labelEntry2S.place(x = 265, y = 245)
              
                    if lengthTGCP > 2:
            
                        self.labelEntry3 = Label(self.master, text =  displayListTGCP[2][0])
                        self.labelEntry3.place(x = 10, y = 265)
                        self.labelEntry3.configure(bg = '#FFFFFF')
                  
                        self.labelEntry3P = Label(self.master, text = displayListTGCP[2][1])
                        self.labelEntry3P.place(x = 85, y = 265)
                        self.labelEntry3P.configure(bg = '#FFFFFF')
                        
                        self.labelEntry3A = Label(self.master, text = displayListTGCP[2][2])
                        self.labelEntry3A.place(x = 130, y = 265)
                        self.labelEntry3A.configure(bg = '#FFFFFF')
                    
                        self.variable3Q = StringVar()
                        self.labelEntry3Q = Entry(self.master, textvariable = self.variable3Q)
                        self.labelEntry3Q.place(x = 195, y = 265)
                               
                        self.variable3S = StringVar()
                        self.labelEntry3S = Entry(self.master, textvariable = self.variable3S)
                        self.labelEntry3S.place(x = 265, y = 265)
                    
                    if lengthTGCP > 3:
                
                        self.labelEntry4 = Label(self.master, text =  displayListTGCP[3][0])
                        self.labelEntry4.place(x = 10, y = 285)
                        self.labelEntry4.configure(bg = '#FFFFFF')
                        
                        self.labelEntry4P = Label(self.master, text = displayListTGCP[3][1])
                        self.labelEntry4P.place(x = 85, y = 285)
                        self.labelEntry4P.configure(bg = '#FFFFFF')
                        
                        self.labelEntry4A = Label(self.master, text = displayListTGCP[3][2])
                        self.labelEntry4A.place(x = 130, y = 285)
                        self.labelEntry4A.configure(bg = '#FFFFFF')
                  
                        self.variable4Q = StringVar()
                        self.labelEntry4Q = Entry(self.master, textvariable = self.variable4Q)
                        self.labelEntry4Q.place(x = 195, y = 285)
                
                        self.variable4S = StringVar()
                        self.labelEntry4S = Entry(self.master, textvariable = self.variable4S)
                        self.labelEntry4S.place(x = 265, y = 285)
                 
                    if lengthTGCP > 4:
            
                        self.labelEntry5 = Label(self.master, text =  displayListTGCP[4][0])
                        self.labelEntry5.place(x = 10, y = 305)
                        self.labelEntry5.configure(bg = '#FFFFFF')
                      
                        self.labelEntry5P = Label(self.master, text = displayListTGCP[4][1])
                        self.labelEntry5P.place(x = 85, y = 305)
                        self.labelEntry5P.configure(bg = '#FFFFFF')
                
                        self.labelEntry5A = Label(self.master, text = displayListTGCP[4][2])
                        self.labelEntry5A.place(x = 130, y = 305)
                        self.labelEntry5A.configure(bg = '#FFFFFF')
                 
                        self.variable5Q = StringVar()
                        self.labelEntry5Q = Entry(self.master, textvariable = self.variable5Q)
                        self.labelEntry5Q.place(x = 195, y = 305)
                       
                        self.variable5S = StringVar()
                        self.labelEntry5S = Entry(self.master, textvariable = self.variable5S)
                        self.labelEntry5S.place(x = 265, y = 305)
                        
                    self.master.mainloop()    
            
#V33 - Purchasing Transactions
            
                def activateEntry(self):
                    
                    self.master.destroy()
                    
                    lengthTGCP = len(displayListTGCP)
                
                    purchaseamount1 = self.variable1Q.get()
                    positionslot1 = self.variable1S.get()
                    
                    purchaseamount2 = self.variable2Q.get()
                    positionslot2 = self.variable2S.get()
                    
                    if lengthTGCP > 2:
                        purchaseamount3 = self.variable3Q.get()
                        positionslot3 = self.variable3S.get()
                    
                    if lengthTGCP > 3:
                        purchaseamount4 = self.variable4Q.get()
                        positionslot4 = self.variable4S.get()
                     
                    if lengthTGCP > 4:
                        purchaseamount5 = self.variable5Q.get()
                        positionslot5 = self.variable5S.get()
                        
                    dataNewPurchase = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '' ], ['', '', '', '']]
                        
                    if purchaseamount1 != '':
                        dataNewPurchase[0][0] = positionslot1
                        dataNewPurchase[0][1] = displayListTGCP[0][0]
                        dataNewPurchase[0][2] = purchaseamount1
                        dataNewPurchase[0][3] = displayListTGCP[0][1]
                   
                    if purchaseamount2 != '':
                        dataNewPurchase[1][0] = positionslot2
                        dataNewPurchase[1][1] = displayListTGCP[1][0]
                        dataNewPurchase[1][2] = purchaseamount2        
                        dataNewPurchase[1][3] = displayListTGCP[1][1]
                        
                    if lengthTGCP > 2:
                        if purchaseamount3 != '':
                            dataNewPurchase[2][0] = positionslot3
                            dataNewPurchase[2][1] = displayListTGCP[2][0]
                            dataNewPurchase[2][2] = purchaseamount3          
                            dataNewPurchase[2][3] = displayListTGCP[2][1]
                            
                    if lengthTGCP > 3:
                        if purchaseamount4 != '':
                            dataNewPurchase[3][0] = positionslot4
                            dataNewPurchase[3][1] = displayListTGCP[3][0]
                            dataNewPurchase[3][2] = purchaseamount4
                            dataNewPurchase[3][3] = displayListTGCP[3][1]
                    
                    if lengthTGCP > 4:
                        if purchaseamount5 != '':
                            dataNewPurchase[4][0] = positionslot5
                            dataNewPurchase[4][1] = displayListTGCP[4][0]
                            dataNewPurchase[4][2] = purchaseamount5
                            dataNewPurchase[4][3] = displayListTGCP[4][1]
                        
                    global dataListCargo
                    
                    global bankAmount
            
                    for mark in range(0,lengthTGCP):
                        if dataNewPurchase[mark][0] == '1':
                            bankAmount = bankAmount - int(dataNewPurchase[mark][2]) * int(dataNewPurchase[mark][3])
                            if dataListCargo[0][1] == dataNewPurchase[mark][1]:
                                comboamount = int(dataListCargo[1][2]) + int(dataNewPurchase[mark][2])
                                dataListCargo[0][2] = comboamount
                            else:
                                dataListCargo[0][1] = dataNewPurchase[mark][1]
                                dataListCargo[0][2] = int(dataNewPurchase[mark][2])
                        
                        elif dataNewPurchase[mark][0] == '2':
                            bankAmount = bankAmount - int(dataNewPurchase[mark][2]) * int(dataNewPurchase[mark][3])
                            if dataListCargo[1][1] == dataNewPurchase[mark][1]:
                                comboamount = int(dataListCargo[1][2]) + int(dataNewPurchase[mark][2])
                                dataListCargo[1][2] = comboamount
                            else:
                                dataListCargo[1][1] = dataNewPurchase[mark][1]
                                dataListCargo[1][2] = int(dataNewPurchase[mark][2])
                        
                        elif dataNewPurchase[mark][0] == '3':
                            bankAmount = bankAmount - int(dataNewPurchase[mark][2]) * int(dataNewPurchase[mark][3])
                            if dataListCargo[2][1] == dataNewPurchase[mark][1]:
                                comboamount = int(dataListCargo[2][2]) + int(dataNewPurchase[mark][2])
                                dataListCargo[2][2] = comboamount
                            else:
                                dataListCargo[2][1] = dataNewPurchase[mark][1]
                                dataListCargo[2][2] = int(dataNewPurchase[mark][2])
                        
                        elif dataNewPurchase[mark][0] == '4':
                            bankAmount = bankAmount - int(dataNewPurchase[mark][2]) * int(dataNewPurchase[mark][3])
                            if dataListCargo[3][1] == dataNewPurchase[mark][1]:
                                comboamount = int(dataListCargo[3][2]) + int(dataNewPurchase[mark][2])
                                dataListCargo[3][2] = comboamount
                            else:
                                dataListCargo[3][1] = dataNewPurchase[mark][1]
                                dataListCargo[3][2] = int(dataNewPurchase[mark][2])
             
            PurchaseCargo()
            
#Z - Mission Managment

        def activateMission(self):
                         
            self.master.destroy()

            class MissionStatus:
               
                def __init__(self):
                    self.master = Tk()
                    self.master.title('Mission Status')
                    self.master.geometry('340x120+50+50')
                    self.master.configure(bg = "#FFFFFF" )
              
                    global shipSystem
                    global shipLocation
                    global missionSystem
                    global missionPlanet
                    global dataListSyPackage
                    global numberPackages
                    global missionReward
           
                    if numberPackages > 0:
                        
                        if shipSystem != missionPlanet:
                
                            self.labelEntryA = Label(self.master,
                                    text = 'You have a mission to ' + missionPlanet + ' in ' + missionSystem + ' system')
                            self.labelEntryA.place(x = 10, y = 0)
                            self.labelEntryA.configure(bg = '#FFFFFF')
                                                                    
                            self.activateButtonK = Button(self.master, text = 'Press to Keep',command = self.activateKeep)
                            self.activateButtonK.place(x = 10, y = 30)
                            self.activateButtonK.configure(fg = '#FF0000', bg = '#FFFFFF')
                    
                            self.activateButtonD = Button(self.master, text = 'Press to Drop',command = self.activateDrop)
                            self.activateButtonD.place(x = 10, y = 60)
                            self.activateButtonD.configure(fg = '#FF0000', bg = '#FFFFFF')                           
                            
                        if shipLocation == missionPlanet:
                
                            self.labelEntryA = Label(self.master, text = 'You complete the mission and deliver the packages')
                            self.labelEntryA.place(x = 10, y = 0)
                            self.labelEntryA.configure(bg = '#FFFFFF')
                        
                            self.activateButtonD = Button(self.master, text = 'Press to Deliver',command = self.activateDeliver)
                            self.activateButtonD.place(x = 10, y = 30)
                            self.activateButtonD.configure(fg = '#FF0000', bg = '#FFFFFF')

                    else:
                        
                        mark = 0                                
                        lengthL = len(dataListSyPackage)
                        
                        while mark == 0:

                            index = random.randint(0,lengthL)
                            
                            missionSystem = dataListSyPackage[index][0]
                            missionPlanet = dataListSyPackage[index][1]
                            
                            if missionPlanet == shipLocation:
                                mark = 0
                            
                            else:
                                mark = 1
                           
                        lengthM = len(dataMissionDistance)
                        factor = 0.5
                        
                        for mark in range (0,lengthM):
                            
                            if dataMissionDistance[mark][0] == shipSystem:
                               if dataMissionDistance[mark][1] == missionSystem:
                                
                                factor = int(dataMissionDistance[mark][2])
                          
                        numberPackages = numberPackages + random.randint(2,6)
                          
                        missionReward = int(numberPackages * 250 * factor)

                        self.labelEntryA = Label(self.master,
                                text = 'You have a misison to ' + missionPlanet + ' in ' + missionSystem + ' system')
                        self.labelEntryA.place(x = 10, y = 0)
                        self.labelEntryA.configure(bg = '#FFFFFF')
                        
                        self.labelEntryA = Label(self.master,
                                 text = 'It pays ' + str(missionReward) + 'c to deliver ' + str(numberPackages) + ' packages')
                        self.labelEntryA.place(x = 10, y = 25)
                        self.labelEntryA.configure(bg = '#FFFFFF')                      
                                                                  
                        self.activateButton = Button(self.master, text = 'Press to Accept',command = self.activateKeep)
                        self.activateButton.place(x = 10, y = 55)
                        self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
                    
                        self.activateButton = Button(self.master, text = 'Press to Drop',command = self.activateDrop)
                        self.activateButton.place(x = 10, y = 85)
                        self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
           
                    self.master.mainloop()
                    
                def activateKeep(self):

                    self.master.destroy()
                    
                def activateDrop(self):

                    global missionSystem
                    global missionPlanet
                    global numberPackages
                    global missionReward
                                  
                    missionPlanet = 'None'
                    missionSystem = 'None'
                    numberPackages = 0
                    missionReward = 0
                
                    self.master.destroy()
                                                       
                def activateDeliver(self):
                    
                    global bankAmount                       
                    global missionSystem
                    global missionPlanet
                    global numberPackages
                    global missionReward
                    
                    bankAmount = int(bankAmount) + int(missionReward)
                                           
                    missionPlanet = 'None'
                    missionSystem = 'None'
                    numberPackages = 0
                    missionReward = 0
                
                    self.master.destroy()
     
            MissionStatus()

#AE -  Collect Stellar Gas

        def activateStellarGas(self):
                
            self.master.destroy()
            
            class SGCollect:

                def __init__(self):
                    self.master = Tk()
                    self.master.title('Stellar Gas Collection')
                    self.master.geometry('260x100+50+50')
                    self.master.configure(bg = "#FFFFFF" )

                    self.activateButton = Button(self.master, text = 'Press to Fly',command = self.activateEntry)
                    self.activateButton.place(x = 10, y = 0)
                    self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
 
                    global cargoCapacity
                    global dataListCargo
                    global hullPoints
                    
                    findCounter = 0
                    spaceCounter = 0

                    allowedCargo = cargoCapacity - numberPackages
                    
                    for mark in range(0, 4):
                        allowedCargo = allowedCargo - dataListCargo[mark][2]
                        
                    gasFind = 5 + random.randint(1,6)
                    
                    self.labelEntryTSl = Label(self.master, text = 'You skim ' + str(gasFind) + ' stellar gas')
                    self.labelEntryTSl.place(x = 10, y = 30)
                    self.labelEntryTSl.configure(bg = '#FFFFFF')
                    
                    if gasFind > allowedCargo:
                            
                        gasFind = allowedCargo

                        self.labelEntryTSl = Label(self.master, text = 'You only have room for ' + str(gasFind) + ' stellar gas')
                        self.labelEntryTSl.place(x = 10, y = 50)
                        self.labelEntryTSl.configure(bg = '#FFFFFF')
                           
                    for mark in range(0, 4):
                        
                        if gasFind > 0:
                            
                            if dataListCargo[mark][1] == 'None' or dataListCargo[mark][1] == 'Stellar Gas':
                                    
                                dataListCargo[mark][1] = 'Stellar Gas'
                                dataListCargo[mark][2] = dataListCargo[mark][2] + gasFind
                                
                                gasFind = 0
                                                    
                    indexEvent = random.randint(1,8)
                    
                    if indexEvent == 10:
                        
                        if hullPoints > 15:
                            
                            explosionDamage = 2
                            hullPoints = hullPoints - 2
                            
                        else:
                            
                            explosionDamage = 1
                            hullPoints = hullPoints - 1
                                            
                    self.labelEntryTSl = Label(self.master, text = 'You take ' + str(explosionDamage) +
                        ' damage from an explosion')
                    self.labelEntryTSl.place(x = 10, y = 70)
                    self.labelEntryTSl.configure(bg = '#FFFFFF')                       
                
                def activateEntry(self):
                
                    self.master.destroy()
         
            SGCollect()
            
#AJ - Ending Game
        
        def activateEndGame(self):
                
            self.master.destroy()
            
            print('Game Over')

            global endGame

            endGame = 'Y'
            
    Option()
    
    global endGame
    
    if endGame== 'N':
        main()

    else:

      newData = [[int(bankAmount)]]     
      exportData = z(*newData, fillvalue = '')  
          
      with open('C:/Users/Peter/Documents/Peter - Toshiba/Python Project/Space Trading Game/Data/Bank.csv','w', newline ='') as newFile:
         writer = csv.writer(newFile)
         writer.writerows(exportData)
         newFile.close()


      slotCargo = []
      goodsCargo  = []
      amountCargo = []
          
      for mark in range (0, 4):
          
         slotCargo = slotCargo  + [dataListCargo[mark][0]] 
         goodsCargo  = goodsCargo + [dataListCargo[mark][1]] 
         amountCargo = amountCargo + [dataListCargo[mark][2]] 
              
         newData = [slotCargo, goodsCargo, amountCargo]
          
      exportData = z(*newData, fillvalue = '')  
          
      with open('C:/Users/Peter/Documents/Peter - Toshiba/Python Project/Space Trading Game/Data/Cargo.csv','w', newline ='') as newFile:
         writer = csv.writer(newFile)
         writer.writerows(exportData)
         newFile.close()


      newData = [[nameVoyageur], [profession], [nameShip], [shipSystem], [shipLocation], [cargoCapacity], [hullPoints],
                [missilesArmed], [bountyLevel], [numberPackages], [missionSystem], [missionPlanet], [missionReward],
                [fuelAmount]]   
      
      exportData = z(*newData, fillvalue = '')  
          
      with open('C:/Users/Peter/Documents/Peter - Toshiba/Python Project/Space Trading Game/Data/Voyageur.csv','w', newline ='') as newFile:
         writer = csv.writer(newFile)
         writer.writerows(exportData)
         newFile.close()

main()




