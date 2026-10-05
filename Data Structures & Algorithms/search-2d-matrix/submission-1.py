class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Arriba = 0
        Abajo = len(matrix) - 1

        while Arriba <= Abajo:
            fila_medio = (Arriba + Abajo) // 2

            if target > matrix[fila_medio][-1]:
                Arriba = fila_medio + 1
            elif target < matrix[fila_medio][0]:
                Abajo = fila_medio - 1
            else:
                break
        if not (Arriba <= Abajo):
            return False

        L = 0
        R = len(matrix[fila_medio]) -1

        while L <= R:
            M = (L + R) // 2

            if matrix[fila_medio][M] == target:
                return True
            elif matrix[fila_medio][M]< target:
                L = M + 1
            else:
                R = M - 1
        
        return False