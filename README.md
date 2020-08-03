# Abstraction

Situation: Suppose you have a parent class `Controller` that calls three abstract functions, `foo_a()`, `foo_b()`, `foo_c()`. The details of these 3 functions need to be coded by a user.

Problem: There are many sets of the 3 abstract functions that can be conceived. We want the user to be able to specify their implementations by creating a Python script and ONLY defining `foo_a()`, `foo_b()`. `foo_c()`. Finally, we want to be able to import a dictionary from the file containing `Controller` which contains unique entries for all of the abstract function implementations provided. 

Solution: Dynamic imports.

### Program output

```
The key is pencil:
Pencil A.
Pencil B.
Pencil C.

The key is tomato:
Tomato A.
Tomato B.
Tomato C.

The key is tree:
Tree A.
Tree B.
Tree C.
```

### Dependencies

`python >= 3.7`
