# Binary Search

----

> 
>
> [toc]

<br/>

## Be Careful

- Is in `sorted order` ?



<br/>

## Time Space Complexity

- T.O : 
- C.O :
- Running time : logarithmic time

<br/>

## Templates

```python
def binary_search(list, item):
  low = 0
  high = len(list) - 1
  
  while low <= high:
    mid = (low + high) / 2
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return None
```





