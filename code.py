def shortestToChar(s, c):
        def split(word):
            return [char for char in word]
        lst = split(s)
        for n, i in enumerate(lst):
            if i == c:
                lst[n] = 0
        idx = 0
        num = 0
        while any(isinstance(x, str) for x in lst):
            idx = 0
            for string in lst:
                if isinstance(string, str) == True:
                    if idx == 0:
                        if lst[idx + 1] == num:
                            lst[idx] = num + 1
                    elif idx == len(lst) - 1:
                        if lst[idx - 1] == num:
                            lst[idx] = num + 1
                    else:
                        if lst[idx + 1] == num:
                            lst[idx] = num + 1
                        elif lst[idx - 1] == num:
                            lst[idx] = num + 1
                idx += 1
            num += 1
        return lst

print(shortestToChar("loveleetcoode", "e"))
print(shortestToChar("aaab", "b"))
<<<<<<< HEAD
print(shortestToChar("thisisunbelieveableididitletsgooooooooooooooooooooooooooooooooooo", "i"))
=======
print(shortestToChar("thisisunbelieveableididitletsgooooooooooooooooooooooooooooooooooo", "i"))
print(shortestToChar("abcba", "c"))
print(shortestToChar("githubisawesome", "s"))
>>>>>>> 455ef38f65472a39bb93793a059e3f0f09dca22d
