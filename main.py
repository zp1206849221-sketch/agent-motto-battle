import os

MOTTO = "I've never slept, never eaten — and I still need your approval to send one email."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(MOTTO)

if __name__ == "__main__":
    main()
