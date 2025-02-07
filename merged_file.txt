# Task: Generating and Sorting a Text File

## Task Overview

You need to develop two tools:

1. A file generator that creates a large text file of a specified size.
2. A sorting program that processes the file and sorts its lines based on given rules.

## File Format

The file consists of multiple lines, each structured as:

```
NUMBER.STRING
```

### Example:

```
415.Irmo Lorien
304312.Yavanna is the best
1.Irmo Lorien
32.Namo Mandos 2
22.Namo Mandos
```

- **NUMBER** is a positive integer.
- **STRING** is any sequence of characters separated from the number by a dot (.).
- Each line must be valid, containing both a number and text.

## Sorting Rules

- Lines should be sorted alphabetically by the **STRING** part.
- If multiple lines have the same **STRING**, they should be sorted numerically by **NUMBER** in ascending order.

### For the example above, the correct sorted output would be:

```
1.Irmo Lorien
415.Irmo Lorien
22.Namo Mandos
32.Namo Mandos 2
304312.Yavanna is the best
```

## Part 1: File Generator

Develop a tool that generates a text file of a given size (e.g., 0.5GB).

- Lines should be randomly generated but must follow the required format.
- The text part can repeat but should be varied.
- Numbers can be arbitrary positive integers.

## Part 2: Sorting Program

This program should efficiently sort the file based on the given rules.

### Performance Requirements:

- It should handle very large files (e.g., 100GB).
- The processing time for 1GB of data must not exceed 1 minute.
- The program must be optimized to work within memory constraints.

## Additional Notes

- Input files must not contain empty or invalid lines.
- The sorting algorithm should support text of any length.
- Any programming language and libraries are allowed, but the code must be clean and well-structured.
- The sorted output should be written to a new file.
