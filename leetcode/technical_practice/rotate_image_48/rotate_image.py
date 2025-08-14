def rotate(self, matrix: List[List[int]]) -> None:
  """
  Do not return anything, modify matrix in-place instead.
  """
  n = len(matrix)
  
  for i in range(0, n):
      for j in range(i, n):
          tmp = matrix[i][j]
          matrix[i][j] = matrix[j][i]
          matrix[j][i] = tmp
  
      matrix[i].reverse()
