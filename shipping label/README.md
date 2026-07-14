# 📦 Shipping Label Program

A simple Python program that demonstrates the use of `*args` and `**kwargs` to generate a formatted shipping label.

## ✨ Features

- 👤 Uses `*args` to accept the recipient's name.
- 🏠 Uses `**kwargs` to accept address details.
- 🏢 Supports both **House Number** and **Apartment Number**.
- 🖨️ Prints a neatly formatted shipping label.
- 🧠 Demonstrates conditional statements and keyword arguments.

## 🛠️ Requirements

- 🐍 Python 3.x

## 🚀 Usage

```python
# Sample input
shipping_label(
    "Mr.", "Ragunanthan",
    House_no=100,
    street="Boston street",
    state="Boston",
    country="USA"
)
```

## 📄 Sample Output

```text
Mr. Ragunanthan
100,
Boston street,
Boston,
USA.
```

## 📚 Concepts Used

- ⚙️ Python Functions
- 📌 `*args` (Variable-length positional arguments)
- 🔑 `**kwargs` (Variable-length keyword arguments)
- 🔀 `if`, `elif`, `else` statements
- 📖 Dictionary methods (`kwargs.get()`)
- ✍️ String formatting (f-strings)

## 📁 Project Structure

```text
📂 Shipping-Label-Program
│── 📄 shipping_label.py
└── 📘 README.md
```

## ⚡ How It Works

1. 👤 Accepts the recipient's name using `*args`.
2. 🏡 Accepts the address using `**kwargs`.
3. 🏢 Prints the apartment number if `apt` is provided.
4. 🏠 Otherwise, prints the house number if `House_no` is provided.
5. 🌍 Prints the street, state, and country in a formatted shipping label.

## 🎯 Example Output

```text
Mr. Ragunanthan
100,
Boston street,
Boston,
USA.
```

## 👨‍💻 Author

**Ragunanthan**

⭐ If you found this project helpful, consider giving it a **star** on GitHub!
