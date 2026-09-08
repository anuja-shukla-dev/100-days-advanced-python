# Day 17 — Custom Iterators 🐍

## 📚 Topics Covered

- Iterable vs Iterator
- `iter()` and `next()`
- `__iter__()` and `__next__()`
- `StopIteration`
- Iterator state
- Iterator exhaustion
- One-shot nature of iterators
- How `for` loops work internally
- Creating custom iterator classes
- Fibonacci Iterator
- Countdown Iterator
- Even Numbers Iterator
- Range-style Iterator
- Real-world pagination concept
- Interview-level iterator concepts

## 🧠 Key Learnings

- An **iterable** is an object from which an iterator can be obtained using `iter()`.
- An **iterator** produces values one at a time using `next()`.
- `iter(obj)` returns an iterator object.
- `next(iterator)` returns the next value.
- `__iter__()` makes an object iterable.
- `__next__()` defines how the next value is produced.
- `StopIteration` tells Python that there are no more values.
- Iterators maintain their own state.
- Once an iterator is exhausted, it cannot be restarted automatically.
- A `for` loop internally uses `iter()` and repeatedly calls `next()` until `StopIteration`.

## 🔄 Iterator Flow

    iterable
        ↓
    iter(iterable)
        ↓
    iterator
        ↓
    next(iterator)
        ↓
    next value
        ↓
    next(iterator)
        ↓
    ...
        ↓
    StopIteration
        ↓
    loop ends

## 🎯 Interview Concepts

- Difference between Iterable and Iterator
- Difference between `iter()` and `next()`
- Purpose of `__iter__()` and `__next__()`
- Why `StopIteration` is raised
- Why iterators are called one-shot objects
- How a `for` loop works internally
- Why custom iterators maintain state

## ✅ Day 17 Status

Completed Day 17 of the 100 Days of Advanced Python Journey.

**Topic:** Custom Iterators  
**Status:** Completed successfully 🚀


    