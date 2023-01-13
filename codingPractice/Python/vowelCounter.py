text = input("Write or paste some text here:\n")
a_count = 0    
e_count = 0
i_count = 0
o_count = 0
u_count = 0
spaces = 0
for x in text:
    if x == " ":
        spaces+=1
    if x=="a":
        a_count+=1
    if x=="e":
        e_count+=1
    if x=="i":
        i_count+=1 
    if x=="o":
        o_count+=1
    if x=="u":
        u_count+=1
               
       
        
message = f"This text contained: \n{a_count} a's,\n{e_count} e's, \n{i_count} i's \n{o_count} o's \n{u_count} u's"

print(message)

counts = {"a":a_count, "e": e_count, "i" : i_count, "o" : o_count, "u" : u_count}

sorted_counts = sorted(counts.items(), key=lambda x:x[1])

print(sorted_counts)

print(f"This text is {len(text)-spaces} letters long")

print(f"The most frequent vowel in this text is {sorted_counts[-1][0]}, it appears {sorted_counts[-1][1]} times")

print(f"That is {sorted_counts[-1][1]-sorted_counts[0][1]} more times than the letter {sorted_counts[0][0]}!")

