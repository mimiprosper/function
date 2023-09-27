
'''def getFullNames(first, middle, last):
    fullName = first + ' ' + middle + ' ' + last
    # convert to dictionary
    # fullName = { 'first':first, 'middle':middle, 'last':last }
    return fullName

student = getFullNames('isaiah', 'madu', 'oko')
print(student)
'''


def getFullName(first, middle, last, age=None):
    fullName = {'first':first, 'middle':middle, 'last':last}
    if age == 40:
        return fullName
    else:
        return 'we dont have your records'

student = getFullName('john', 'uka', 'udoka', 36)
student = getFullName('mark', 'greg', 'oba', 40)
print(student)

