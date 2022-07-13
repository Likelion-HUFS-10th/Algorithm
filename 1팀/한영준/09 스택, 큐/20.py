inputs = input()
gwalhoz = {
    '(' : ')',
    "{" : "}",
    "[" : "]"
}
tf = 0

gwalhoz_1 = ["(","{","["]

for i in range(len(inputs)-1):
    print(inputs[i])
    if inputs[i] in gwalhoz_1 :
        if inputs.index(gwalhoz[inputs[i]]) < inputs.index(gwalhoz[inputs[i+1]]):
            tf = 1
    
if tf == 1:
    print("false")
else:
    print("true")
        

    

