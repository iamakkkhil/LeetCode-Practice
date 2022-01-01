# [213. House Robber II](https://leetcode.com/problems/house-robber-ii/)

**Difficulty** : Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are __arranged in a circle__. That means the first house is the neighbor of the last one.  the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and __it will automatically contact the police if two adjacent houses were broken into on the same night__.

Given an integer array `nums` _representing the amount of money of each house, return the maximum amount of money you can rob tonight __without alerting the police___.

---

## Example 1:

```
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

```

## Example 2:

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

## Example 3:

```
Input: nums = [1,2,3]
Output: 3
```

## Constraints:

* `1 <= nums.length <= 100`
* `0 <= nums[i] <= 1000`

<br>

# Submission Details

* 75 / 75 test cases passed.
* Status: Accepted
* Runtime: 65 ms
* Memory Usage: 14.3 MB
