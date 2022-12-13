"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""

def divide_string(String: str) -> list:
    indice_metade = len(String) // 2
    if len(String) % 2 == 0:
        parte_frente, parte_tras = String[0:indice_metade], String[indice_metade:]
        frente_tras = [parte_frente, parte_tras]
    elif len(String) % 2 != 0:
        parte_frente, parte_tras = String[0:indice_metade + 1], String[indice_metade + 1:]
        frente_tras = [parte_frente, parte_tras]
    return frente_tras


def front_back1(a, b):
    # +++ SUA SOLUÇÃO +++
    String_a = divide_string(a)
    String_b = divide_string(b)
    solução = String_a [0]+ String_b[0] + String_a[1] + String_b[1]
    return solução
    # +++ SUA SOLUÇÃO +++
import math


def pega_metade(string):
    return math.ceil(len(string) / 2)


def separa_front_back(s):
    tam = pega_metade(s)
    return s[:tam], s[tam:]


def front_back(a, b):
    # +++ SUA SOLUÇÃO +++
    metade_a_1, metade_a_2 = separa_front_back(a)
    metade_b_1, metade_b_2 = separa_front_back(b)
    return ''.join([metade_a_1, metade_b_1, metade_a_2, metade_b_2])


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
