Match_dict = {"Ahmadi":2, "Bagheri":4,
              "Mortazavi":5, "Hosseini":3, "Mahmoodi":4}
while True:
    input_str = input().split()
    if input_str[0] == "End":
        break
    else:
        if input_str[0] not in list(Match_dict.keys()):
            print("Motasefane Shoma Davat Nistid!")
        else:
            if Match_dict[input_str[0]] >= int(input_str[-1]):
                print("Khosh Amadid!")
            else:
                print("Tedade Afrade Davat Shode Kamtar Ast!")
            

