# def concatena(t1, t2):
#     return t1 + t2

# if __name__=='__main__':
#     print(concatena('a', 'b'), type(concatena('a', 'b')))
#     print(concatena(1, 2), type(concatena(1, 2)))
#     print(concatena([1, 2], [3, 4]), type(concatena([1, 2], [3, 4])))


# from typing import List, Tuple, Union
# def concatena(
#         t1: Union[List, Tuple, int], 
#         t2: Union[List, Tuple, int]
#         )-> Union[List, Tuple, int]:
    
#     return t1 + t2

# from typing import Any

# def concatena(
#         t1: Any,
#         t2: Any
#         )-> Any:
    
#     return t1 + t2

from typing import Union, NewType, Type, Dict, Any, TypeVar

Number = TypeVar('Number', int, float, complex)

# DadosDoCadastro = Dict[str,str]

# def concatena(t1: Any, t2: Any) -> Any:
#     return t1 + t2

def soma_numerica(
        x: Number, 
        y: Number
        ) -> Number:
    """
    soma dois números
    """
    return x + y

# def valida_cadastro(user: DadosDoCadastro) -> bool:
#     ...