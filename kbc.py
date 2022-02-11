def question():
    question=["How many continents are there",
    "What is the capital of India?",            
    "NG mei kaun se course padhaya jaata hai?"
    
]
    return question
question_list=question()
def option():
    
    option=[["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
    return option
option_list=option()
def solution():
#    solution= ([3, 4, 1])
   return solution
solution_list=solution()
def answer():
    answer=["3 seven", "4 eight","4 delhi","1 Chandigarh","1 Software Engineering","2 Counseling"]
    return answer
answer_list=answer()
i=0
a=0
b=1
count=0
while i<len(question_list):
    print(question_list[i])
    j=0
    while j<=len(option_list):
        l=(option_list)[i][j]
        print(j+1,l)
        j+=1
    
    print("YOU HAVE 50-50 LIFE LINE ")
    life_line=input("IF YOU WANT LIFE LINE ...FOR:- YES ,PRESS'Y' AND FOR:- NO ,PRESS 'N'")
    if life_line=="y":
        if count==0:
            print(answer_list[i+a])
            print(answer_list[i+b])
            answer=int(input("ENTER YOUR ANSWER "))
            if solution_list[i]==answer:
                print("KYA 6BAAT HAI ....KYA BAAT HAI ......BILKUL SHI JAWAP ....")
                count+=1
            else:
                print("YOUR ANSWER IS WRONG ")
            count=count+1
        else:
            print("YOUR LIFE IS FINISHED")
            print("NOW YOUR LIFELINE IS OVER SO PLZ MAKE UP YOUR MIND")
            m=int(input("enter answer"))
            if solution_list[i]==m:
                print("right ")
            else:
                print("YOUR ANSWER IS WRONG")
                # break
    elif life_line=="n":
        user=int(input(" CHOOSE BY YOURSELF "))
        if solution_list[i]==user:
            print("YOUR ANSWER IS CORRECT,")
        else:
            print("SHRM KARO APNE UPER ITNA BHI NHI AATA,,,,YOUR ANSWER IS WRONG")
            break
    else:
        print("THANKS FOR PLAY THIS GAME")
        # break
    a+=1
    b+=1
    i+=1
