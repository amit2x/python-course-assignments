call_count=0
def track_calls():
    global call_count
    call_count+=1
    print("Function is called")

def main():
    while True:
        char = input("Do You want to call the function, press Y else N")
        if char == "Y":
            track_calls()
        elif char == "N":
            print("Thankyou for using this program")
            break
        else:
            print("Please enter Y or N")
            continue

    print(f"Total calls : {call_count}")

if __name__ == "__main__":
    main()
