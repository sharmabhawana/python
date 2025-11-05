'''In a high-tech fortress, the chief guard was responsible for ensuring that all passwords were extra secure. He discovered a magical way to strengthen any password: by replacing each vowel with the next vowel in a special sequence.
The rule was simple but clever:
The vowels follow a cycle: a → e → i → o → u → a.
Uppercase vowels follow the same cycle but preserve their case: A → E → I → O → U → A.
Consonants remain unchanged.
Whenever someone tried to set a password, the guard would automatically transform it according to this rule, making it harder for intruders to guess while keeping it memorable for the rightful owner.
Input Format
single string S (password).
Constraints
1 ≤ len ≤ 200.
Output Format
resulting string.
Sample Input 0
apple
Sample Output 0
eppli
Sample Input 1
BANANA
Sample Output 1
BENENE'''
s=input()
res=""
for ch in s:
    match ch:
        case 'a':
            res+='e'
        case 'e':
            res+='i'
        case 'i':
            res+='o'
        case 'o':
            res+='u'
        case 'u':
            res+='a'
        case 'A':
            res+='E'
        case 'E':
            res+='I'
        case 'I':
            res+='O'
        case 'O':
            res+='U'
        case 'U':
            res+='A'
        case _:
            res+=ch
print(res)