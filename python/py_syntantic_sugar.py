# Unpacking tuples and sequences. -> https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments
a,b,c = ["variable a","variable b","variable c"]

string_var = "String"
tuple_var = ("Tuple", "Tuple", "Tuple")
list_var = ["List", "List"]
elements = [string_var, tuple_var, list_var]
for element in elements:
    print(type(element))
    # Each of Python’s built-in sequence types (str, tuple, and list) support the following operator syntaxes:
    print("s[j] element at index j")
    # s[j] element at index j
    print(element[1])
    # s[start:stop] slice including indices [start,stop)
    print("# s[start:stop] slice including indices [start,stop)")
    print(element[3:2])
    # s[start:stop:step] slice including indices start, start + step,
    print("s[start:stop:step] slice including indices start, start + step,")
    print(element[1:4:2])