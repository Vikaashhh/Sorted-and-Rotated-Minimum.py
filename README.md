# 🔍 Day 29 - Find Minimum in Sorted and Rotated Array

This repository contains the solution for **"Find Minimum in a Sorted and Rotated Array"**, a classic binary search problem from the **GFG 160 DSA Sheet**.

---

## 📌 Problem Statement

Given a sorted and rotated array of distinct integers, the task is to find the minimum element in the array.

---

## 🚀 Approach

We use **Binary Search** to find the minimum element efficiently.

### 🧠 Logic:
- In a rotated array, the minimum element is the **only** element that is smaller than its previous.
- Using binary search:
  - If `arr[mid] > arr[high]`, the minimum lies in the right half.
  - Else, it lies in the left half (including `mid`).
- Keep narrowing down the search space until `low == high`.

### ⏱️ Time Complexity
- **O(log N)** — efficient search using binary strategy.

### 📦 Space Complexity
- **O(1)** — constant space usage.

---

## 📚 Concepts Practiced
Binary Search

Rotated Arrays

Optimization

---

 ### Day 29 of #gfg160 #geekstreak2025
