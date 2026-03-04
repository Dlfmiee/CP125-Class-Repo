# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    names = set()
    
    f1 = open(file1, "r")
    f2 = open(file2, "r")
    
    for line in f1:
        names.add(line.strip())
        
    for line in f2:
        names.add(line.strip())
        
    f1.close()
    f2.close()
    
    f = open(output_file, "w")
    
    for name in sorted(names):
        f.write(name + "\n")
        
    f.close()
    
    return len(names)


# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
