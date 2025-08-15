# Handle Ctrl+C (KeyboardInterrupt) gracefully

try:
    while True:
        name = input("Enter your name (or Ctrl+C to exit): ")
        print("Hello,", name)
except KeyboardInterrupt:
    print("\nGoodbye! Program interrupted by user.")
