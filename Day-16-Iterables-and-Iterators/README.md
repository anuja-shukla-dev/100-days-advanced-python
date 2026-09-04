# Day 16 – Iterables and Iterators

## 📚 Topics Covered

- Iterable vs Iterator
- iter() function
- next() function
- StopIteration exception
- Iterator Protocol
- __iter__() method
- __next__() method
- How for loops work internally
- Iterator state
- Creating custom iterators

## 💻 Practice Programs

### 01. Custom Iterator
- Created a custom Countdown iterator.
- Practiced maintaining iterator state.
- Used __iter__() and __next__().
- Raised StopIteration when iteration was complete.

### 02. StopIteration Exception
- Practiced manually calling next().
- Handled StopIteration using try-except.

### 03. Even Numbers
- Created a custom iterator to generate even numbers.
- Practiced updating iterator state after every next() call.

### 04. Square Numbers
- Created a custom iterator to generate square numbers one at a time.
- Practiced using iterator state to control the sequence.

## 🧠 Key Concepts

### Iterable
An iterable is an object that can be iterated over, such as a list, tuple, string, or dictionary.

### Iterator
An iterator is an object that produces values one at a time and maintains its current iteration state.

### iter()
iter() takes an iterable and returns an iterator.

### next()
next() retrieves the next value from an iterator.

### StopIteration
When an iterator has no more values to return, next() raises the StopIteration exception.

### Iterator Protocol
A custom iterator implements:

- __iter__() → returns the iterator object
- __next__() → returns the next value or raises StopIteration

## 🔄 How a for Loop Works

Conceptually, Python's for loop:

1. Calls iter() on the iterable.
2. Gets an iterator.
3. Repeatedly calls next().
4. Processes each returned value.
5. Stops when StopIteration is raised.

## 🎯 Key Takeaway

An iterable can provide an iterator.

An iterator maintains its state and produces values one at a time using next().

When there are no more values, the iterator raises StopIteration, which tells Python that the iteration is complete.

## 📌 Day 16 Status

✅ Iterables & Iterators Completed
✅ iter() and next() Practiced
✅ StopIteration Practiced
✅ Iterator Protocol Understood
✅ Custom Iterators Practiced
✅ Iterator State Understood