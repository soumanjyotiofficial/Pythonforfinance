"""
Revision lecture
index and slicing
Index       position of object, element or character in sequence
Slicing     Used to extract a range of elements from
            sequence eg: String and other are list , tuples


"""



#Index explanation

country_name = "INDIA IS MY COUNTRY.2M"
pos_ = country_name.index("N")
print(pos_)
"""
for a in country_name:
    print(a,country_name.index(a))
"""
#slicing
#len  = 22
get_1 = country_name[1]
get_2_last= country_name[-2]
print(get_2_last)
gent_1_7 = country_name[1:7] # from 1st to 6th (7)
gent_1_7 = country_name[1:]# from 1st to end
gent_1_7 = country_name[:-2]
print(gent_1_7)
demo_ = f"I am an {country_name[:5]}N"
print(demo_)
#print(len(country_name))








