# --------------------------------------
# CSCI 127, Lab 8                      |
# October 19, 2021                       |
# Tiegan Cozzie                           |
# --------------------------------------

def first2third(user_string,friend_pronoun):
    pronouns_male={"me":"him","myself":"himself","i":"he","am":"is","im":"hes","my":"his","have":"has","want":"wants"}
    pronouns_female={"me":"her","myself":"herself","i":"her","am":"is","im":"hers","my":"her","have":"has","want":"wants"}
    pronouns_plural={"me":"them","myself":"themselves","i":"they","am":"are","im":"they are","my":"their","have":"have","want":"want"}
    punctuation=[",",".","?",";",":","!"]
    count=0
    for char in user_string:
        if user_string[count] in punctuation:
            user_string=user_string[0:count]+" "+user_string[count:len(user_string)]
            count+=2
        else:
            count+=1
    userList=user_string.split()
    if friend_pronoun=="m":
        for i in userList:
            if i in list(pronouns_male.keys()):
                userList[userList.index(i)]=pronouns_male[i]
    elif friend_pronoun=="f":
        for i in userList:
            if i in list(pronouns_female.keys()):
                userList[userList.index(i)]=pronouns_female[i]
    elif friend_pronoun=="p":
        for i in userList:
            if i in list(pronouns_plural.keys()):
                userList[userList.index(i)]=pronouns_plural[i]

    final=""
    for word in userList:
        if word in punctuation or len(user_string)==0:
           final=final+word
        else:
          final=final+" "+word

    return final

def main():
    user_string = input("Enter the question to be translated: ").lower()
    friend_name = input("Enter the name of the friend: ")
    print(friend_name + "'s pronouns: masculine, feminine, or plural/neutral?  ")
    friend_pronouns = ""
    while (friend_pronouns != 'm' and friend_pronouns != 'f' and friend_pronouns != 'p'):
        friend_pronouns = input("Enter m, f, or p: ").lower()
    translation = first2third(user_string, friend_pronouns)
    print("Asking for a friend,  "+friend_name+"...")
    print(translation)
    
main()
