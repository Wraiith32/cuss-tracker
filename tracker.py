import speech_recognition as sr

# List of cuss words
cuss_words = ['fuck', 'fuk', 'fucking', 'mother fucker','motherfucker','mother fucking']  # Add your own cuss words to the list

# Initialize the recognizer
r = sr.Recognizer()

# Function to count cuss words in the transcribed text
def count_cuss_words(transcribed_text):
    count = 0
    for word in transcribed_text.split():
        if word.lower() in cuss_words:
            count += 1
    return count

# Main program loop
def main():
    stop_listening = False
    cuss_word_count = 0

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        print("Listening...")
        while not stop_listening:
            try:
                # Use streaming recognition
                r.pause_threshold = 0.5  # Adjust the pause threshold as needed
                audio = r.listen(source, phrase_time_limit=5)  # Adjust the phrase_time_limit as needed
                transcribed_text = r.recognize_google(audio)
                print("You said:", transcribed_text)

                # Count the cuss words
                cuss_word_count += count_cuss_words(transcribed_text)
                print("Cuss word count:", cuss_word_count)

                # Check for the stop keyword
                if "pineapple" in transcribed_text.lower():
                    stop_listening = True

            except sr.UnknownValueError:
                pass
                #print("Could not understand audio")
            except sr.RequestError as e:
                print("Error occurred; {0}".format(e))

# Start the program
if __name__ == '__main__':
    main()
