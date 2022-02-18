def main():
    try:
        configuration = open('C:/Users/Usuario/Desktop/config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()