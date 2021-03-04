def count_substring(string, sub_string):
    a = 0
    for i in range (len(string)):
        if i + len(sub_string) > len(string):
            break
        for k in range (len(sub_string)):
            if string[i + k] != sub_string[k]:
                break
        if string[i + k] != sub_string[k]:
            continue  
        a += 1
    return a

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)