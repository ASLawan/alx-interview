# 0x04. UTF-8 Validation

## Objective
As part of the interview prpartion program, today's project expects us to implement a python function that accepts a list of data values and checks if there valid UTF-8 encoded characters or not.  

## Definition:
__UTF-8 (Unicode Transformation Format - 8-bit)__ is a clever encoding scheme designed to be efficient for a wide range of characters.   
It achieves this by using a variable number of bytes _(1, 2, 3, or 4)_ to represent different characters depending on their code point (numeric value) in the Unicode standard. 

## Here's how it works:

 __-Smaller code points (common characters):__  
 
 - These characters, typically found in English and other Latin-based languages, have lower numerical values in the Unicode standard.   
 UTF-8 takes advantage of this by encoding them using a single byte (8 bits). This is because the first 128 characters of Unicode map directly to the standard 7-bit ASCII characters, making UTF-8 backward compatible with ASCII.

__-Larger code points (less common characters):__   

- Characters with higher code points, often used in languages with special characters or symbols, require more bits to represent accurately. UTF-8 uses 2, 3, or 4 bytes to encode these characters efficiently.  

Here's a table summarizing the relationship between code point size and UTF-8 bytes:

| : Code Point Range (Decimal) : |	: Number of Bytes : | : Example Characters : |
| -------------------- |-------------------- |-------------------- |
| 0 - 127 | 1	| Letters (a-z, A-Z), numbers (0-9), basic punctuation |
| -------------------- |-------------------- |-------------------- |
| 128 - 2047 | 	2  | Many accented letters in European languages |
| -------------------- |-------------------- |-------------------- |
| 2048 - 65535	| 3  | Most characters in Asian languages (Chinese, Japanese, etc.) |
| -------------------- |-------------------- |-------------------- |
| 65536 - 1114111 | 4	| Less common characters and emoji |

## How does UTF-8 determine the number of bytes?

- UTF-8 uses a specific pattern in the most significant bits _(leftmost bits)_ of each byte to indicate how many bytes are used for a character
- The first bit (most significant) tells you if it's a single-byte or multi-byte character:  
    - 0: Single-byte character (uses only the current byte)  
    - 1: Multi-byte character (followed by continuation bytes)
- Subsequent bytes in a multi-byte character have a specific pattern _(starting with 10)_ to differentiate them from single-byte characters. This pattern ensures efficient decoding and avoids ambiguity.
