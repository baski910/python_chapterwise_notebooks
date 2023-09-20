import numpy as np

arr1 = np.array([12,18,21,34])

arr2 = np.array([17,35,46,53])

print(arr1+arr2) # addition each elemets from arr1 and arr2

# array shapes
arr1 = np.array([12,18,21,34])
print(arr1.shape)

arr1 = np.array(
  [
    [12,18,21,34],
    [17,35,46,53]    
  ]
)

print(arr1.shaoe)

arr1 = np.array(
  [
  [
    [12,18,21,34],
    [17,35,46,53]    
  ],
  [
    [12,18,21,34],
    [17,35,46,53]    
  ],
  ]
)

print(arr1.shaoe)

# linear spac exaple
arr1 = np.linspace(0,2,50)
print(arr1)

# intialize arrays
arr1 = np.zeros((3,3))
print(arr1)
arr1 = np.ones((3,3))
print(arr1)


