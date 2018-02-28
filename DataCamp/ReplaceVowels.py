def eliminateVowelString(Var):
    result =[]
    for i in Var:
        if i.lower() not in 'aeiou':
            result.append(i)

    return ''.join(result)

res = eliminateVowelString('The quick brown fox jumps over the lazy dog')
print('\n',len(res))
print('\n',res)
