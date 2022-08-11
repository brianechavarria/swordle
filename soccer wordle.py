import pandas as pd
import random


clean=pd.read_csv("topfive.csv")



def guess(goal, dataset, check): #target here is supposed to work with goal
    test=["_","_","_","_","_"]
    attempt=str(input("Please enter your guess: "))
    if (attempt not in dataset["player_name"].values):
        print("That player is not in our database. Try again")
        guess(goal, dataset, check)
    elif (attempt==goal[0]):
        for i in range(5):
            test[i]=goal[i]
            check=True
        
    else:
        temp=(dataset[dataset["player_name"]==attempt]).values
        for i in range(5):
            if (temp[0][i]==goal[i]): #This line is broken for some reason          
                test[i]=temp[0][i]
    
    return test, check
  



  
def swordle(dataset):
    result=""
    idx=random.randrange(0,2697) #later replace this number with the size of the dataframe so i can easily change things if i want
    target=dataset.iloc[idx]
    turns=1
    correctCheck=False
    while turns<5:
        turn,correctCheck=guess(target,dataset,correctCheck)
        print(turn)
        if correctCheck==True:
            result="You Win!!!"
            return result
        
        turns+=1
    
    result="You ran out of tries. Better luck next time"
    return result
    


def play(dataset):
    answer=swordle(dataset)
    print(answer)

    
    


