questions = [
    {
        " prompt" : " Who wrote the novel ' 1984' ? ",
        " Options" : [ "A. George Orwell" , "B. J.K Rowling " , "C. F.Scott Fitzgerald " , "D. Ernest Hemingway"] , 
        " answer" : "A"
    } , 
    {
        " prompt" : " What the capital city of Australia ? ",
        " Options" : [ "A. Sydney" , "B. Melbourne" , "C. Canberra " , "D. Brisbane"] , 
        " answer" : "C"
    } , 
    {
        " prompt" : " What is the chemical symbol for Gold ? ",
        " Options" : [ "A. Gd" , "B. Go " , "C. Ag " , "D. Au"] , 
        " answer" : "D"
    } , 
    {
        " prompt" : " What is the tallest mountain in the world ? ",
        " Options" : [ "A. K2" , "B. Mount Everest " , "C. Mount Kilimanjaro " , "D. Denali"] , 
        " answer" : "B"
    } , 
    {
        " prompt" : " Which planet is known as the ' Red Planet' ? ",
        " Options" : [ "A. Venus" , "B. Mars " , "C. Jupiter " , "D. Saturn"] , 
        " answer" : "B"
    } 
]
def Quizz_run(questions):
    score = 0 
    for question in questions :
        print(question[" prompt"])
        for option in question[" Options"] :
            print(option)
        answer = input("Enter your answer ( A , B , C or D): ").upper()
        if answer == question[" answer"] :
            print(" Correct answrer 😉 \n")
            score+=1    
        else:
            print(" Wrong answer ☹  , the correct answer is : " + question[" answer"] + "\n ")
    print(f" you got {score} out of { len(questions) } questions correct  ")


Quizz_run(questions)