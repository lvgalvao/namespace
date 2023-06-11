from typing import Union

def soma(x: Union[int, float],y: Union[int, float]) -> Union[int, float]:
    return x + y

# print(soma('x', 'y'))
print(soma(1,2))
print(soma(4.5,3.4))