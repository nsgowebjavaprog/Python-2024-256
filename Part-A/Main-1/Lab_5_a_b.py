def count_occurence(s1, s2):
    count = s2.count(s1)
    return count

s1=input("Enter the substring to find(s1): ")
s2=input("Enter the Main string: ")

occurence = count_occurence(s1, s2)
print(f"The substring of{s1} Occurs {occurence} time(s) in the String{s2}")