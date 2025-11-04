#2453 - Língua do P

def main():
    ls = input().split()
    ans = []
    for word in ls:
        tmp = []
        for i in range(1, len(word), 2):
            tmp.append(word[i])
        ans.append(''.join(tmp))
    print(' '.join(ans))
    
if __name__ == '__main__':
    while True:
        try:
            main()
        except EOFError:
            break