# 📘 Day 18 — Generators and `yield`

## 📌 Overview

Day 18 focused on **Generators in Python** and how the `yield` keyword allows us to create iterators that produce values one at a time.

Generators are useful when working with large amounts of data because they do not store all values in memory at once. Instead, they generate each value only when it is needed.

---

## 🎯 Topics Covered

- Generators in Python
- `yield` keyword
- Generator functions
- Generator objects
- `next()`
- `StopIteration`
- Generators with loops
- Generator expressions
- Memory efficiency of generators
- Practical generator for reading files

---

## 1. 🔹 Generator Basics

A function containing `yield` becomes a **generator function**.

Unlike `return`, `yield` pauses the function and remembers its current state.

Example:

    def numbers():
        yield 1
        yield 2
        yield 3

    gen = numbers()

    print(next(gen))
    print(next(gen))
    print(next(gen))

Output:

    1
    2
    3

---

## 2. 🔹 `yield` vs `return`

### `return`

- Ends the function completely.
- Sends back a value.
- Function cannot continue from where it stopped.

### `yield`

- Pauses the function.
- Produces one value.
- Remembers the function's state.
- Continues from where it stopped when `next()` is called again.

---

## 3. 🔹 Generator with a Loop

Generators can produce values dynamically using loops.

Example:

    def count_numbers(n):
        for i in range(1, n + 1):
            yield i

    for number in count_numbers(5):
        print(number)

Output:

    1
    2
    3
    4
    5

---

## 4. 🔹 Generator Expressions

Generator expressions provide a shorter way to create generators.

Example:

    squares = (x * x for x in range(5))

    for value in squares:
        print(value)

Output:

    0
    1
    4
    9
    16

A generator expression uses `()` instead of the `[]` used by a list comprehension.

---

## 5. 🔹 Memory Efficiency

A list stores all generated values in memory:

    numbers = [x for x in range(1000000)]

A generator produces values when needed:

    numbers = (x for x in range(1000000))

Therefore, generators are especially useful when:

- Working with large datasets
- Processing files
- Reading data step by step
- Handling streams of data
- Memory usage matters

---

## 6. 🔹 `StopIteration`

When a generator has no more values to produce, calling `next()` again raises `StopIteration`.

Example:

    def demo():
        yield 1

    gen = demo()

    print(next(gen))
    print(next(gen))

The second `next()` raises:

    StopIteration

A `for` loop handles this automatically.

---

## 7. 🔹 Practical File Generator

Generators can be used to read files one line at a time.

Example:

    def read_file(filename):
        with open(filename, "r") as file:
            for line in file:
                yield line.strip()

    for line in read_file("sample.txt"):
        print(line)

This avoids loading the entire file into memory at once.

---

## 📂 Files Created

    Day-18-Generators-and-yield/
    │
    ├── 01-generators_basics.py
    ├── 02-generator_with_loop.py
    ├── 03-generator_expression.py
    ├── 04-generator_memory.py
    ├── 05-generator_practical.py
    └── sample.txt

---

## 🧠 Key Takeaways

- `yield` turns a function into a generator function.
- A generator produces values lazily.
- `next()` requests the next value.
- Generators remember their state between `next()` calls.
- `StopIteration` indicates that the generator is exhausted.
- Generator expressions provide a compact syntax.
- Generators can significantly reduce memory usage.
- Generators are useful for processing files and large datasets.

---

## 🚀 Day 18 Completed

Learned how Python generators work internally and how to use them for memory-efficient data processing.

