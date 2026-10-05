class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        largo = 0
        conteo_letras = {}

        for R, letra in enumerate(s):
            conteo_letras[letra] = conteo_letras.get(letra, 0) + 1

            while ((R - L) + 1) - max(conteo_letras.values()) > k:
                conteo_letras[s[L]] -= 1
                L += 1

            largo = max(largo, (R - L) + 1)
        return largo