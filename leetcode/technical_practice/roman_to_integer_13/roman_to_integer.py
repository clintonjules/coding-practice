def romanToInt(self, s: str) -> int:
  rosetta = {
      "I" : 1,
      "V" : 5,
      "X" : 10,
      "L" : 50,
      "C" : 100,
      "D" : 500,
      "M" : 1000
  }
  
  total = 0
  
  for i in range(0, len(s)):
      current = rosetta[s[i]]
  
      total += -current if current < (rosetta[s[i+1]] if i < len(s) - 1 else -100) else current
  
  return total
