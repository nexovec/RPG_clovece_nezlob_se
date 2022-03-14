def move_up(t):
    print(f"""\033[2A""")
def main():
    print("yaay1")
    move_up(2)
    print("yaay2")
    pass

if __name__ == "__main__":
    main()