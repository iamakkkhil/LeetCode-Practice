# [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray//)

**Difficulty** : Medium

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a __32-bit__ integer.

A __subarray__ is a contiguous subsequence of the array.

---

## Example 1:

```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.cted to every other node, so 2 is the center.
```

## Example 2:

```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

## Constraints:

* `1 <= nums.length <= 2 * 10^4`
* `-10 <= nums[i] <= 10`
* The product of any prefix or suffix of `nums` is __guaranteed__ to fit in a __32-bit__ integer.

<br>

# Submission Details

* 188 / 188 test cases passed.
* Status: Accepted
* Runtime: 80 ms
* Memory Usage: 14.6 MB
