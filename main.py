def main_loop():
    hp = 5
    gold = 0
    i = 0
    print("You enter the dungeon.")
    while(True):
        i += 1
        decision = input("You have {} hp and {} gold. Do you want to (c)ontinue or (e)xit?".format(
                hp, gold))
        if (decision == "e"):
            print("You exit the dungeon. You found {} gold.".format(gold))
            break
        elif (decision == "c"):
            if (i % 2 == 0):
                print("You find 1 gold.")
                gold += 1
            else:
                print("Trap! You lose 1 hp.")
                hp -= 1
        else:
            continue

##########################################

if __name__ == "__main__":
    main_loop()
