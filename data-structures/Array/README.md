# Array

----

> [toc]

</br>

## Definition

-  논리적 저장 순서와 물리적 저장 순서가 일치한다. (배열은 크기가 고정되어야 한다 -> 배열의 크기를 동적으로 늘려서 사용하고 싶을 때 동적배열 사용. 처음부터 자신이 사용할 배열의 크기를 알면 좋겠지만 크기를 너무 크게 잡으면 메모리가 낭비되고, 그렇다고 크기를 작게 잡으면 매번 배열을 새로 만들어서 기존의 배열을 옮겨 담아야 해서 번거롭다 ) 따라서 `인덱스(index)`로 해당 원소(element)에 접근할 수 있다. 그렇기 때문에 찾고자 하는 원소의 인덱스 값을 알고 있으면 `Big-O(1)`에 해당 원소로 접근할 수 있다. 즉 **random access**가 가능하다는 장점이 있다.

- Stores data elements based on sequential, most commonly 0 based, index.

  Based on tuples from set theory.

  One of the oldest, most commonly used data structures.

- Optimal for indexing
  - Bad at searching, inserting, deleting (except at the end)
- Array vs [Linked List](https://github.com/Dinoryong/Algorithms/blob/main/data-structures/Linked%20List/README.md)
  - 

- **Linear Array** - one dimensional array
  - static in size, meaning that they are declared with a fixed size
- **Dynamic Array** - like one dimensional arrays, but have reserved space for additional elements
  - if a dynamic array is full, it copies its contents to a larger array
  - In Python, 정적 배열 대신 동적 배열만 존재하면 list 로 사용
- **Multi Dimensional Array** - nested array that allow for multiple dimensions such as an arrays providing a 2 dimensional spacial represenation via x, y coordinates

<br/>

## Keep in Mind

- sorted or partially sorted ?
  - come up with binary search (that is faster than O(N))
  - sorting the array significantly simplify the problem
    - the order of array elements don't need to be preserved before attempting a sort
  
- sumation or multiplication of a subarray involved question
  - try pre-computation using hashing or a prefix/suffix  sum/product
  
- Given a sequence and the interviewer asks for O(1) space

  - might be possible to use the array itself as a hash table

- O(N) doesn't mean you can only traverse the array once. Traversing more than once can help you solve the problem easily

- Arrays are sequences

  - If there are duplicate values in the array, would it affect the answer ?

  - Be careful not to go out of bounds 

  - Slicing or Concatenating arrays - typically O(N) time complexity , use start and end indices to demarcate a subarray/range where possible

  - traverse from right also

  - Sliding window technique - subarray problems

  - given 2 arrays - one index per array (pointer) to traverse/compare the both of then.

    e.g) same approach to merge two sorted arrays [ref.Merge Sort]()

<br/>

## Time Complexity

- Indexing, Access : O(1)
- Search : O(N)
- Optimized Search : O(N)
- Insert : O(N)
- Delete : O(N)

<br/>

## Corner Cases

- Empty sequence
- Sequence with 1 or 2 elements
- Sequence with repeated elements

<br/>

## Templates

> Array를 기반으로 한 Linked List 구현
>
> ArrayList를 기반으로 한 Linked List 구현
>
> Reversed Array 배열 돌리기
>
> 

### Reverse an array (배열 회전)

Python

```python
```

<br/>

JavaScript

```javascript
```

<br/>

Java

```java
int i = 0;
int j = a.length - 1;
while (i < j) {
	swap(a, i++, j--);
}
```

<br/>

### Binary search in a sorted array algorithm

Python

```python

```

<br/>

JavaScript

```javascript

```

<br/>

Java

```java

```

<br/>

### Find an element in a rotated sorted array

> Solution: binary search
>
> Check first if the array is rotated. If not, apply normal binary search
>
> If rotated, find pivot (smallest element, only element whose previous is bigger)
>
> Then, check if the element is in 0..pivot-1 or pivot..len-1

Python

```python

```

<br/>

JavaScript

```javascript

```

<br/>

Java

```java

```

<br/>

### Given an array, move all the 0 to the left while maintaining the order of the other elements

> Example: 1, 0, 2, 0, 3, 0 => 0, 0, 0, 1, 2, 3
>
> Two pointers technique: read and write starting at the end of the array
>
> If read is on a 0, decrement read. Otherwise swap, decrement both

Python

```python

```

<br/>

JavaScript

```javascript

```

<br/>

Java

```java
public void move(int[] a) {
	int w = a.length - 1, r = a.length - 1;
	while (r >= 0) {
		if (a[r] == 0) {
			r--;
		} else {
			swap(a, r--, w--);
		}
	}
}

// T.C : O(n) , S.C : O(1)
```

<br/>

### How to detect if an element is a pivot in a rotated sorted array

> Only element whose previous is bigger (also the pivot is the smallest element)

<br/>

### How to find a pivot element in a rotated array

> Check first if the array is rotated
>
> Then, apply binary search (comparison with a[right] to know if we go left or right)

Python

```python

```

<br/>

JavaScript

```javascript

```

<br/>

Java

```java
int findPivot(int[] a) {
	int left = 0, right = a.length - 1;

	// Array is not rotated
	if (a[left] < a[right]) {
		return -1;
	}

	while (left <= right) {
		int mid = left + ((right - left) / 2);
		if (mid > 0 && a[mid] < a[mid - 1]) {
			return a[mid];
		}

		if (a[mid] < a[right]) {
			// Pivot is on the left
			right = mid - 1;
		} else {
			// Pivot is on the right
			left = mid + 1;
		}
	}

	return -1;
}

```

<br/>

### How to find the duplicates in an array

> Hashtable
>
> Sorting the array then iterating over each element and check if previous = current

<br/>

### How to manage a dynamic array

> When full, create a new array of twice the size, copy items (System.arraycopy is optimized for that)
>
> Shrink:
>
> - Not when one-half full (otherwise worst case is too expensive: double-shrink-double-shrink etc.)
> - Solution: one-quarter full

<br/>

### How to test if the array is sorted in ascending or descending order

>  Test first and last element (no iteration)

<br/>

### Rotate an array by n elements ( n can be negative )

Example: 1, 2, 3, 4, 5 with n = 3 => 3, 4, 5, 1, 2

- Reverse the initial array
- Reverse from 0 to n-1
- Reverse from n to len - 1

Python

```python

```

<br/>

JavaScript

```javascript

```

<br/>

Java

```java
void rotateArray(List<Integer> a, int n) {
	if (n < 0) {
		n = a.size() + n;
	}

	reverse(a, 0, a.size() - 1);
	reverse(a, 0, n - 1);
	reverse(a, n, a.size() - 1);
}

// T.C : O(N) , S.C : O(1)
```

<br/>



## Problem Sets

[Two Sum](https://leetcode.com/problems/two-sum) -> [SOLVED](https://github.com/Dinoryong/Algorithms/blob/main/data-structures/Array/Two%20Sum.md)

[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

[Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

[Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

[3 Sum](https://leetcode.com/problems/3sum/)

[Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

[K번째 수](https://programmers.co.kr/learn/courses/30/lessons/42748) => [SOLVED](https://github.com/Dinoryong/Algorithms/blob/main/data-structures/Array/prg_Kth%20Number.md)

[가장 큰 수](https://programmers.co.kr/learn/courses/30/lessons/42746) => [SOLVED](https://github.com/Dinoryong/Algorithms/blob/main/data-structures/Array/prg_The%20Largest%20Number.md)

[H-Index](https://programmers.co.kr/learn/courses/30/lessons/42747) => [SOLVED](https://github.com/Dinoryong/Algorithms/blob/main/data-structures/Array/prg_H-Index.md)

<br/>

## Related Topics

Linked List

Binary Search

Matrix

Sliding Window

Hash Table

<br/>

## ... references

[awesome-algorithms](https://github.com/Algorithm-box/awesome-algorithms#websites)

[Tech-Interview-Cheat-Sheet](https://github.com/TSiege/Tech-Interview-Cheat-Sheet#array)

[algodeck](https://github.com/teivah/algodeck/blob/master/array.md)

[Tech Interview Handbook](https://techinterviewhandbook.org/algorithms/array)

[Interview Question for Beginner](https://github.com/CS-box/Interview_Question_for_Beginner/tree/master/DataStructure#array-vs-linked-list)

[파이썬 알고리즘 인터뷰](https://github.com/onlybooks/algorithm-interview)

[코딩 인터뷰 퀘스쳔](http://book.interpark.com/product/BookDisplay.do?_method=detail&sc.prdNo=232182463&gclid=Cj0KCQjwxdSHBhCdARIsAG6zhlXZaxUGTQQVrjWXlFQ1YJy-fA3OhraK87rc7KQ5ngXwDyzO7ti4vhMaAlBOEALw_wcB)

<br/>

