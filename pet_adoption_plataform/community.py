import os
from pet_adoption_plataform import user_account

topics = {
    "Petshops recomendados" : {
        "owner" : "Isabela",
        "title" : "Recomendação de petshop",
        "message" : "Sou nova na cidade e queria recomendações de petshop para comprar ração de gato",
        "comments" : {
            "Matheus" : {
                "coment" : "Eu sempre levo os meus no petshop do shopping"
            }
        }
    }
}

def showcommunity():
    global topics

    while True:
        for topic in topics.keys():
            print(f"Topic: {topic}")
        
        choice = input("Want to participate in the debate? y/n\n").lower()

        if choice == "y":
            choice_topic = input("Choice a topic to participate: ").lower().capitalize()
            topic_find = topics.get(choice_topic)

            if not topic_find:
                print("Topic dont found")
                continue
            while True:
                os.system("cls")

                print(f"User: {topic_find["owner"]}")
                print(f"Title: {topic_find["title"]}")
                print(f"Message: {topic_find["message"]}")
                print(f"Coments: {len(topic_find["comments"])}")

                comment = input("--Read comments (1)\n--Write a comment (2)\n--Return (3)\n")
                if comment == "1":
                    os.system("cls")
                    for user in topic_find.get("comments"):
                        print(f"User: {user}")
                        print(f"Comment: {topics["Petshops recomendados"]["comments"][user]["coment"]}")

                    input()
                    os.system("cls")
                    continue
                if comment == "2":
                    os.system("cls")
                    if user_account.user_age == "Unknown":
                        print("You need to have a account")
                        input()
                        os.system("cls")
                        continue
                    else:
                        user_profile = user_account.user_name
                        user_comment = input("Enter your comment: ")

                        topic_find["comments"][user_profile] = {"coment" : user_comment}
                        os.system("cls")
                    continue
                if comment == "3":
                    break
                else:
                    print("Try again")
        else:
            break