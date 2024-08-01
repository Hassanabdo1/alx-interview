nitialize a list opened with False values, indicating that no boxes are opened initially except the first one.
Start with the key to the first box (index 0).
Use a list keys to keep track of keys that can be used to open boxes.
While there are keys available:
Pop a key from the list.
For each key found in the corresponding box:
If the key corresponds to a box that hasn't been opened and is within the range, mark it as opened and add the key to the list.
Finally, check if all boxes have been opened by returning all(opened).
