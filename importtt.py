# import math # importing the whole module
# instead you can import selective functions such as
import math as m

from testmodule import test, testt

# from math import pi, sqrt as s

# from math import sqrt, pi

# ans = math.sqrt(9)
# when we are importing just the function then we don't need to write the name of the module

# ans = s(9) * pi
# print(ans)
print(dir(m))  # to print all the directories in the module
print(testt)
test()
