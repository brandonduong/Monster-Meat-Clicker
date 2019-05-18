import pygame
import time
import random

pygame.init()
displayWidth = 1200
displayHeight = 800

black = (0, 0, 0)
gray = (211, 211, 211)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
brightGreen = (0, 200, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight)) #Sets screen
pygame.display.set_caption("Mitra Meat Clicker") #Sets window title
clock = pygame.time.Clock()

mitraWidth = 465
mitraHeight = 598

def text_objects(text, font): #can make parameters (text, font, colour) to add customizable colour to text
    textSurface = font.render(text, True, black) #string, anti aliasing?, colour
    return textSurface, textSurface.get_rect()

def button(msg, x, y, width, height, inactive, active): #Action default to none
    mouse = pygame.mouse.get_pos() #Get mouse position in tuple (x, y)
    click = pygame.mouse.get_pressed() #Get mouse click in tuple (left, middle, right mouse buttons)
    result = None
    if x + width > mouse[0] > x and y < mouse[1] < y + height: #Play Button
        pygame.draw.rect(gameDisplay, active, (x, y, width, height))
        if click[0] == 1:
            result = True
            
    else:
        pygame.draw.rect(gameDisplay, inactive, (x, y, width, height)) #Play Button
        result = False

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (width / 2)), (y + (height / 2)))
    gameDisplay.blit(textSurf, textRect)
    return result

    
def picButton(pic, active, x, y, width, height): #Button function for pictures
    mouse = pygame.mouse.get_pos() #Get mouse position in tuple (x, y)
    click = pygame.mouse.get_pressed() #Get mouse click in tuple (left, middle, right mouse buttons)


    if x + width > mouse[0] > x and y < mouse[1] < y + height: #Play Button
        gameDisplay.blit(active, (x, y))
        if click[0] == 1:
            gameDisplay.blit(pic, (x, y))
            return True
    else:
        gameDisplay.blit(pic, (x, y))

def clickingCooldown(clickCooldown): #Ensures that clickCooldown only gets set back to 0 when LMB is not pressed
    click = pygame.mouse.get_pressed()
    if click[0] == 0 and clickCooldown != 0:
        return -1
    else:
        return 0

def shopDisplay(counter, text, cost, x, y, colour, size): #Displays shop items
    font = pygame.font.SysFont(None, size)
    text = font.render(text + str(counter) + " / Cost: " + str(cost), True, colour)
    gameDisplay.blit(text, (x, y))

def meatDisplay(counter, text, x, y, colour, size): #Displays meat money
    font = pygame.font.SysFont(None, size)
    text = font.render(text + str(counter), True, colour)
    gameDisplay.blit(text, (x, y))

def messageDisplay(msg, x, y, size): #Displays message
    font = pygame.font.Font("freesansbold.ttf", size)
    text = font.render(msg, True, black)
    gameDisplay.blit(text, (x, y))

def lootbox(total): #Rolling lootbox
    topLootbox = pygame.image.load("lootboxTop.png") #Top of lootbox
    botLootbox = pygame.image.load("lootboxBottom.png") #Bot of lootbox
    rngMeat = random.randint(0, total)
    for i in range(0, 50, 2):
        gameDisplay.fill(white)
        messageDisplay("Won: " + str(rngMeat) + " Meat!", (displayWidth / 2) - 130, 480, 30)
        gameDisplay.blit(topLootbox, ((displayWidth / 2) - 205, 70 - i))
        gameDisplay.blit(botLootbox, ((displayWidth / 2) - 205, 471 + i))
        pygame.display.update()
        time.sleep(0.05)
    time.sleep(1)
    return rngMeat
    
    




def gameLoop():
    #Initialize
    mitraImg = pygame.image.load("mitra.png") #Loads big Mitra picture
    smallMitraImg = pygame.image.load("mitraSmall.png") #Loads small Mitra picture

    meat = 0 #Meat money
    payoutRate = 60 #Countdown til miners give money
    mitraLevel = 1 #Mitra Clicking Face
    mitraClickPayout = 1 #How much meat a mitra click gives
    mitraLevelCost = 500 #Mitra Level Up Cost
    
    miners = 0 #Miners
    minerCost = 10 #Miner Meat Cost

    factories = 0 #Factories
    factoryCost = 100 #Factory Meat Cost

    basements = 0 #Basements
    basementCost = 1500 #Basement Meat Cost

    babies = 0 #Babies
    babyCost = 25000 #Baby Meat Cost

    butts = 0 #Butts
    buttCost = 100000 #Butt Meat Cost

    payoutUpgradeCost = 250 #Payout Upgrade Meat Cost

    minerUpgrades = 0 #Miner Upgrades
    minerUpgradeCost = 1000 #Miner Upgrade Meat Cost

    factoryUpgrades = 0 #Factory Upgrades
    factoryUpgradeCost = 5000 #Factory Upgrade Meat Cost

    basementUpgrades = 0 #Basement Upgrades
    basementUpgradeCost = 25000 #Basement Upgrade Meat Cost

    babyUpgrades = 0 #Baby Upgrades
    babyUpgradeCost = 100000 #Baby Upgrade Meat Cost

    buttUpgrades = 0 #Butt Upgrades
    buttUpgradeCost = 150000 #Butt Upgrade Meat Cost
    
    mitraClickCD = 0 #Mitra Level buying clicking cooldown
    clickCooldown = 0 #Mitra clicking cooldown
    minerClickCD = 0 #Miner buying clicking cooldown
    facClickCD = 0 #Factory buying clicking cooldown
    basClickCD = 0 #Basement buying clicking cooldown
    babyClickCD = 0 #Baby buying clicking cooldown
    buttClickCD = 0 #Butt buying clicking cooldown
    payoutClickCD = 0 #Payout upgrade buying click cooldown
    minUpgradeClickCD = 0 #Miner upgrade buying click cooldown
    facUpgradeClickCD = 0 #Factory upgrade buying click cooldown
    basUpgradeClickCD = 0 #Basement upgrade buying click cooldown
    babUpgradeClickCD = 0 #Baby upgrade buying click cooldown
    butUpgradeClickCD = 0 #Butt upgrade buying click cooldown
    lootboxClickCD = 0 #Lootbox buying click cooldown

    counter = 0 #Counter for all shop items payout
    
    while True:
        for event in pygame.event.get(): #Gets any event happening like where mouse is, keys pressed. Event handling loop, all inputs and events in this loop 
            if event.type == pygame.QUIT: #pygame.QUIT is when user hits the "x"
                pygame.quit() #Closes pygame window
                quit() #Closes Python in general

        gameDisplay.fill(white)
        #gameDisplay.blit(background, (-450, -275)) #Background

        button("Meat Shop!", 540, 0, 650, 100, gray, gray)

                
        if picButton(mitraImg, smallMitraImg, 10, 105, mitraWidth, mitraHeight) == True and clickCooldown == 0: #Clicking Mitra
            meat += mitraClickPayout #+ Meat when clicking Mitra
            clickCooldown = 1 #Click Cooldown set to 1 to prevent holding Mitra down
        clickCooldown += clickingCooldown(clickCooldown) #Runs function clickingCooldown, ensures that clickCooldown only gets set back to 0 when LMB is not pressed

        if button("Buy a Different Monster! / Cost: " + str(mitraLevelCost), 15, 710, 465, 75, green, brightGreen) == True and meat >= mitraLevelCost and mitraClickCD == 0: #Buy Different Mitras
            meat = int(meat - mitraLevelCost) #Subtract Meat from Cost
            mitraLevel += 1 #Bought a Different Mitra
            mitraClickPayout *= 5 #Mitra Click Payout
            mitraLevelCost = int(mitraLevelCost * 7.5) #Increase Different Mitra Cost
            mitraClickCD  = 1 #Mitra Click Cooldown set to 1 to prevent holding buy button down
            #Switching Mitra Faces
            if mitraLevel == 2:
                mitraImg = pygame.image.load("mitra2.png")
                smallMitraImg = pygame.image.load("mitra2Small.png")

            elif mitraLevel == 3:
                mitraImg = pygame.image.load("mitra3.png")
                smallMitraImg = pygame.image.load("mitra3Small.png")
        messageDisplay("Meat per Click: " + str(mitraClickPayout), 170, 755, 18) #Displays meat per click payout
                
        mitraClickCD += clickingCooldown(mitraClickCD) #Runs function clickingCooldown


        if button("Buy!", 540, 115, 75, 75,  green, brightGreen) == True and meat >= minerCost and minerClickCD == 0: #Buy Meat Miners
            meat = int(meat - minerCost) #Subtract Meat from Cost
            miners += 1 #Bought a Miner
            minerCost = int(minerCost * 1.1) #Increase Miner Cost
            minerClickCD  = 1 #Miner Click Cooldown set to 1 to prevent holding buy button down
        minerClickCD += clickingCooldown(minerClickCD) #Runs function clickingCooldown
        shopDisplay(miners, "M.Miner: ", minerCost,  625, 140, black, 50) #Displays Shop Item: Miners

        if button("Buy!", 540, 200, 75, 75,  green, brightGreen) == True and meat >= factoryCost and facClickCD == 0: #Buy Meat Factories
            meat = int(meat - factoryCost) #Subtract Meat from Cost
            factories += 1 #Bought a Factory
            factoryCost = int(factoryCost * 1.15) #Increase Factory Cost
            facClickCD  = 1 #Factory Click Cooldown set to 1 to prevent holding buy button down
        facClickCD += clickingCooldown(facClickCD) #Runs function clickingCooldown
        shopDisplay(factories, "M.Factory: ", factoryCost,  625, 225, black, 50) #Displays Shop Item: Factory

        if button("Buy!", 540, 285, 75, 75,  green, brightGreen) == True and meat >= basementCost and basClickCD == 0: #Buy Meat Basements
            meat = int(meat - basementCost) #Subtract Meat from Cost
            basements += 1 #Bought a Basement
            basementCost = int(basementCost * 1.2) #Increase Basement Cost
            basClickCD  = 1 #Basement Click Cooldown set to 1 to prevent holding buy button down
        basClickCD += clickingCooldown(basClickCD) #Runs function clickingCooldown
        shopDisplay(basements, "M.Basement: ", basementCost,  625, 310, black, 50) #Displays Shop Item: Basement

        if button("Buy!", 540, 370, 75, 75,  green, brightGreen) == True and meat >= babyCost and babyClickCD == 0: #Buy Meat Babies
            meat = int(meat - babyCost) #Subtract Meat from Cost
            babies += 1 #Bought a Baby
            babyCost = int(babyCost * 1.25) #Increase Baby Cost
            babyClickCD  = 1 #Baby Click Cooldown set to 1 to prevent holding buy button down
        babyClickCD += clickingCooldown(babyClickCD) #Runs function clickingCooldown
        shopDisplay(babies, "M.Baby: ", babyCost,  625, 395, black, 50) #Displays Shop Item: Baby

        if button("Buy!", 540, 455, 75, 75,  green, brightGreen) == True and meat >= buttCost and buttClickCD == 0: #Buy Meat Butts
            meat = int(meat - buttCost) #Subtract Meat from Cost
            butts += 1 #Bought a Butt
            buttCost = int(buttCost * 1.3) #Increase Butt Cost
            buttClickCD  = 1 #Butt Click Cooldown set to 1 to prevent holding buy button down
        buttClickCD += clickingCooldown(buttClickCD) #Runs function clickingCooldown
        shopDisplay(butts, "M.Butt: ", buttCost,  625, 480, black, 50) #Displays Shop Item: Butt
        ##############################################

        if payoutRate == 1: #Sold Out Button
            button("Sold Out!", 22, 70, 465, 30,  red, red)
        #Payout Upgrade Button
        elif button("Buy Payout Upgrade! / Cost: " + str(payoutUpgradeCost), 22, 70, 465, 30,  green, brightGreen) == True and meat >= payoutUpgradeCost and payoutClickCD == 0 and payoutRate != 1: #Buy Payout Upgrade
            meat = int(meat - payoutUpgradeCost) #Subtract Meat from Cost
            payoutRate -= 1 #Bought a payout upgrade
            payoutUpgradeCost = int(payoutUpgradeCost * 1.125) #Increase Payout Upgrade Cost
            payoutClickCD  = 1 #Butt Click Cooldown set to 1 to prevent holding buy button down
        payoutClickCD += clickingCooldown(payoutClickCD) #Runs function clickingCooldown

        if button("x2 Miner Meat Upgrade!", 540, 540, 315, 75, green, brightGreen) == True and meat >= minerUpgradeCost and minUpgradeClickCD == 0: #Buy Miner Upgrade
            meat = int(meat - minerUpgradeCost) #Subtract Meat from Cost
            minerUpgrades += 1 #Bought a miner upgrade
            minerUpgradeCost = int(minerUpgradeCost * 4) #Increase Miner Upgrade Cost
            minUpgradeClickCD  = 1 #Buying Click Cooldown set to 1 to prevent holding buy button down
        minUpgradeClickCD += clickingCooldown(minUpgradeClickCD) #Runs function clickingCooldown
        shopDisplay(minerUpgrades, "Upgrades: ", minerUpgradeCost, 625, 588, black, 20) #Displays Miner Upgrade

        if button("x2 Factory Meat Upgrade!", 540, 625, 315, 75, green, brightGreen) == True and meat >= factoryUpgradeCost and facUpgradeClickCD == 0: #Buy Factory Upgrade
            meat = int(meat - factoryUpgradeCost) #Subtract Meat from Cost
            factoryUpgrades += 1 #Bought a factory upgrade
            factoryUpgradeCost = int(factoryUpgradeCost * 4.5) #Increase Factory Upgrade Cost
            facUpgradeClickCD  = 1 #Buying Click Cooldown set to 1 to prevent holding buy button down
        facUpgradeClickCD += clickingCooldown(facUpgradeClickCD) #Runs function clickingCooldown
        shopDisplay(factoryUpgrades, "Upgrades: ", factoryUpgradeCost, 625, 673, black, 20) #Displays Factory Upgrade

        if button("x2 Basement Meat Upgrade!", 540, 710, 315, 75, green, brightGreen) == True and meat >= basementUpgradeCost and basUpgradeClickCD == 0: #Buy Basement Upgrade
            meat = int(meat - basementUpgradeCost) #Subtract Meat from Cost
            basementUpgrades += 1 #Bought a basement upgrade
            basementUpgradeCost = int(basementUpgradeCost * 4.75) #Increase Basement Upgrade Cost
            basUpgradeClickCD  = 1 #Buying Click Cooldown set to 1 to prevent holding buy button down
        basUpgradeClickCD += clickingCooldown(basUpgradeClickCD) #Runs function clickingCooldown
        shopDisplay(basementUpgrades, "Upgrades: ", basementUpgradeCost, 625, 758, black, 20) #Displays Basement Upgrade

        if button("x2 Baby Meat Upgrade!", 875, 540, 315, 75,  green, brightGreen) == True and meat >= babyUpgradeCost and babUpgradeClickCD == 0: #Buy Baby Upgrade
            meat = int(meat - babyUpgradeCost) #Subtract Meat from Cost
            babyUpgrades += 1 #Bought a baby upgrade
            babyUpgradeCost = int(babyUpgradeCost * 4.875) #Increase Baby Upgrade Cost
            babUpgradeClickCD  = 1 #Buying Click Cooldown set to 1 to prevent holding buy button down
        babUpgradeClickCD += clickingCooldown(babUpgradeClickCD) #Runs function clickingCooldown
        shopDisplay(babyUpgrades, "Upgrades: ", babyUpgradeCost,  960, 588, black, 20) #Displays Baby Upgrade

        if button("x2 Butt Meat Upgrade!", 875, 625, 315, 75,  green, brightGreen) == True and meat >= buttUpgradeCost and butUpgradeClickCD == 0: #Buy Butt Upgrade
            meat = int(meat - buttUpgradeCost) #Subtract Meat from Cost
            buttUpgrades += 1 #Bought a butt upgrade
            buttUpgradeCost = int(buttUpgradeCost * 5) #Increase Butt Upgrade Cost
            butUpgradeClickCD  = 1 #Buying Click Cooldown set to 1 to prevent holding buy button down
        butUpgradeClickCD += clickingCooldown(butUpgradeClickCD) #Runs function clickingCooldown
        shopDisplay(buttUpgrades, "Upgrades: ", buttUpgradeCost,  960, 673, black, 20) #Displays Butt Upgrade

        if button("Monster Meat Lootbox!", 875, 710, 315, 75,  green, brightGreen) == True and lootboxClickCD == 0: #Buy Lootbox
            totalMeat = int(meat * 1.5)
            meat = int(meat * 0.45) #Subtract Meat from Cost
            meat += lootbox(totalMeat)
            lootboxClickCD  = 1 #Buying Click Cooldown set to 1 to prevent holding buy button down
        lootboxClickCD += clickingCooldown(lootboxClickCD) #Runs function clickingCooldown
        shopDisplay("1.5 x Total Meat", "Payout: 0 - ", "55% of Total Meat",  885, 758, black, 18) #Displays Lootbox

        
        

        
        


            
        if counter % payoutRate == 0: #Payout Rate
            payout = (miners * (2 ** minerUpgrades))  + ((factories*5) * (2 ** factoryUpgrades)) + ((basements*25) * (2 ** basementUpgrades)) + ((babies*100) * (2 ** babyUpgrades)) + ((butts*1000) * (2 ** buttUpgrades)) #Payout Calculations
            meat += payout

        elif counter > 1000000: #To prevent counter hitting sys.max number
            counter = 0
            
        counter += 1
        meatDisplay(meat, "Meat: ", 20, 5, black, 70) #Displays total meat
        meatDisplay(payout, "Meat per " + str(payoutRate) + " ticks: ", 21, 45, black, 40) #Displays meat/sec
        clock.tick(60) #Number entered = fps

        pygame.display.update()

gameLoop()
