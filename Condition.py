def decission(values):
    var="Not Satisfied condition"
    if values<10:
        var="lessthan 10"
    elif values>10:
        var="gratertan 10"
    return var

print(decission(9))
print(decission(10))
print(decission(11))