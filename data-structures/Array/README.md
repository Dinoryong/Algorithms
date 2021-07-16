# Array

----

> [toc]

</br>

## Definition

- 논리적 저장 순서와 물리적 저장 순서가 일치한다. 따라서 `인덱스(index)`로 해당 원소(element)에 접근할 수 있다. 그렇기 때문에 찾고자 하는 원소의 인덱스 값을 알고 있으면 `Big-O(1)`에 해당 원소로 접근할 수 있다. 즉 **random access**가 가능하다는 장점이 있다.

  하지만, 삭제 또는 삽입의 과정에서는 해당 원소에 접근하여 작업을 완료한 뒤 (O(1)), 또 한 가지의 작업을 추가해줘야 하기 때문에 시간이 더 소요된다. 만약 배열의 원소 중 어느 원소를 삭제했다고 했을 때 , 배열의 연속적인 특징이 깨지게 된다. 즉, 빈 공간이 생긴다. 따라서 삭제한 원소보다 큰 인덱스를 갖는 원소들을 `shift` 해줘야 하는 비용(cost)이 발생하고, 이 경우의 시간 복잡도는 O(N)이 된다. 그렇기 때문에 Array 자료구조에서 삭제 기능에 대한 Time Complexity 의 worst case 는 O(N)이 된다.

  삽입의 경우도 마찬가지이다. 만약 첫번째 자리에 새로운 원소를 추가하고자 한다면 모든 원소들의 인덱스를 1씩 `shift` 해줘야 하므로, 이 경우의 시간 복잡도도 O(N)이 된다.

- Optimal for indexing
  - Bad at searching, inserting, deleting (except at the end)
- Array vs [Linked List](https://github.com/Dinoryong/Algorithms/blob/main/data-structures/Linked%20List/README.md)
  - 

- Linear Array
  - 
- Dynamic Array
  - 
- Multi Dimensional Array



## Keep in Mind

- 



## Time Complexity

- Access : O(1)
- Search : O(N)
- Insert : O(N)
- Delete : O(N)



## Templates

> Array를 기반으로 한 Linked List 구현
>
> ArrayList를 기반으로 한 Linked List 구현
>
> 배열 돌리기
>
> 

### Reverse an array



<br/>

## Problem Sets

[Two Sum](https://leetcode.com/problems/two-sum) -> [click and see my solution]()

[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

[Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

[Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

[3 Sum](https://leetcode.com/problems/3sum/)

[Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

<br/>

## references

[Tech-Interview-Cheat-Sheet](https://github.com/TSiege/Tech-Interview-Cheat-Sheet#array)

[algodeck](https://github.com/teivah/algodeck/blob/master/array.md)

[Tech Interview Handbook](https://techinterviewhandbook.org/algorithms/array)

[Interview Question for Beginner](https://github.com/CS-box/Interview_Question_for_Beginner/tree/master/DataStructure#array-vs-linked-list)

<br/>
