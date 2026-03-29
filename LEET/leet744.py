def nextGreatestLetter(letters, target):
        L=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        result=letters[0]
        for I in letters:
                if L.index(I) > L.index(target):
                        result = I
                        return result
        return result

letters = ["c","f","j"]
target = "a"
print(nextGreatestLetter(letters, target))
letters = ["x","x","y","y"]
target = "z"
print(nextGreatestLetter(letters, target))
letters = ["c","f","j"]
target = "c"
print(nextGreatestLetter(letters, target))