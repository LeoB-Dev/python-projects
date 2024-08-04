while True:
    try: 
        page_number = float(input("\nWhat page of PCC are you on?"))
        book_length = (467 - 14)
        actual_pages_read = page_number - 14
        progress = ((actual_pages_read)/ book_length * 100)
        
        if page_number > 14 and page_number <= 467:
            print(f"\n\nYou are {round(progress, 1)}% of the way through PCC!\
        \n\nYouv'e read {round(actual_pages_read)} pages out of \
{int(book_length)} pages\n")
            break

        elif page_number > 467 and page_number <= 501:
            print(f"\n\nYou've fininished the main book! Now you're \
{round(progress, 1)}% through PCC!\n\nYou've read {round(actual_pages_read)} \
pages out of {int(book_length)} pages\n")
            break

        elif page_number < 14 and page_number > 0:
            print("You did not read these pages.")

        else: 
            print("Invalid input, please enter a number between 14 and 501.")

    except ValueError:
        print("Please enter a valid number.")

