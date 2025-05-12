# 🐼 Advanced Palindrome Check – Server-Client App

This project creates a client-server application that can detect simple and complex palindromes. The client sends a string to the server, and the server responds with whether it's a palindrome and how complex it is to make one if needed.

---

## 💡 What It Does

### ✅ Simple Palindrome Check
- Ignores spaces, punctuation, and letter case.
- Example:
  ```
  Input:  "A man, a plan, a canal, Panama"
  Output: True
  ```

### 🔄 Complex Palindrome Check
- Checks if a string can be rearranged into a palindrome.
- Calculates a complexity score (minimum number of swaps to make it one).
- Example:
  ```
  Input:  "ivicc"
  Output: Can form palindrome: True
          Complexity score: 2
  ```

---

## 🛠 How to Run

1. **Install Python 3**  
   Make sure Python 3 is installed on your system.

2. **Run the Server**  
   In one terminal:
   ```bash
   python server.py
   ```

3. **Run the Client**  
   In a second terminal:
   ```bash
   python client.py
   ```

4. **Choose an Option**  
   - Simple Palindrome Check
   - Complex Palindrome Check

5. **Enter a String**  
   The client will send it to the server and show you the result.

---

## ⚙️ Notes

- Works with strings that include mixed case, special characters, and spaces.
- Non-alphanumeric characters are ignored in checks.
- The client retries if the server does not respond within 5 seconds (up to 3 times).

---
