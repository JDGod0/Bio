def lig_calc():
    vector = int(input("What is the length of the vector in bp?"))
    vector_ammount = int(input("How many ng of vector will you use for the ligation?"))
    insert = int(input("What is the length of the insert in bp?"))
    ratio = int(input("What ratio of vector to insert would you like to use? 1: ?"))
    insert_ammount = ((((vector_ammount * (insert/1000)) / (vector/1000)) * (ratio/1)))
    print(f"You will need to use {insert_ammount}ng of insert for a 1:{ratio} molar ratio ligation reaction")
if __name__ == '__main__':
    lig_calc()