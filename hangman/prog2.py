{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Loading word list from file...\n",
      "55900 words loaded.\n",
      "------------\n",
      "Welcome to the game, Hangman!\n",
      "I am thinking of a word that is 6 letters long.\n",
      "------------\n",
      "You have 10 guesses left.\n",
      "Available letters:  abcdefghijklmnopqrstuvwxyz\n",
      "Please guess a letter: a\n",
      "Good guess:  -a----\n",
      "------------\n",
      "You have 10 guesses left.\n",
      "Available letters:  bcdefghijklmnopqrstuvwxyz\n",
      "Please guess a letter: i\n",
      "Oops! That letter is not in my word:  -a----\n",
      "------------\n",
      "You have 9 guesses left.\n",
      "Available letters:  bcdefghjklmnopqrstuvwxyz\n",
      "Please guess a letter: l\n",
      "Good guess:  -a---l\n",
      "------------\n",
      "You have 9 guesses left.\n",
      "Available letters:  bcdefghjkmnopqrstuvwxyz\n",
      "Please guess a letter: p\n",
      "Oops! That letter is not in my word:  -a---l\n",
      "------------\n",
      "You have 8 guesses left.\n",
      "Available letters:  bcdefghjkmnoqrstuvwxyz\n",
      "Please guess a letter: t\n",
      "Good guess:  -a-t-l\n",
      "------------\n",
      "You have 8 guesses left.\n",
      "Available letters:  bcdefghjkmnoqrsuvwxyz\n",
      "Please guess a letter: e\n",
      "Good guess:  -a-tel\n",
      "------------\n",
      "You have 8 guesses left.\n",
      "Available letters:  bcdfghjkmnoqrsuvwxyz\n",
      "Please guess a letter: b\n",
      "Oops! That letter is not in my word:  -a-tel\n",
      "------------\n",
      "You have 7 guesses left.\n",
      "Available letters:  cdfghjkmnoqrsuvwxyz\n",
      "Please guess a letter: q\n",
      "Oops! That letter is not in my word:  -a-tel\n",
      "------------\n",
      "You have 6 guesses left.\n",
      "Available letters:  cdfghjkmnorsuvwxyz\n",
      "Please guess a letter: u\n",
      "Oops! That letter is not in my word:  -a-tel\n",
      "------------\n",
      "You have 5 guesses left.\n",
      "Available letters:  cdfghjkmnorsvwxyz\n",
      "Please guess a letter: h\n",
      "Oops! That letter is not in my word:  -a-tel\n",
      "------------\n",
      "You have 4 guesses left.\n",
      "Available letters:  cdfgjkmnorsvwxyz\n",
      "Please guess a letter: d\n",
      "Oops! That letter is not in my word:  -a-tel\n",
      "------------\n",
      "You have 3 guesses left.\n",
      "Available letters:  cfgjkmnorsvwxyz\n",
      "Please guess a letter: n\n",
      "Oops! That letter is not in my word:  -a-tel\n",
      "------------\n",
      "You have 2 guesses left.\n",
      "Available letters:  cfgjkmorsvwxyz\n",
      "Please guess a letter: o\n",
      "Oops! That letter is not in my word:  -a-tel\n",
      "------------\n",
      "You have 1 guesses left.\n",
      "Available letters:  cfgjkmrsvwxyz\n",
      "Please guess a letter: f\n",
      "Oops! That letter is not in my word:  -a-tel\n",
      "------------\n",
      "You lose. The word was: cartel\n"
     ]
    }
   ],
   "source": [
    "## Homework Assignment 2\n",
    "# Name: ?????????\n",
    "# Time Spent: 3 days\n",
    "\n",
    "\n",
    "import random\n",
    "import string\n",
    "\n",
    "WORDLIST_FILENAME = \"words.txt\"\n",
    "\n",
    "def load_words():\n",
    "    \"\"\"\n",
    "    Returns a list of valid words. Words are strings of lowercase letters.\n",
    "    \n",
    "    Depending on the size of the word list, this function may\n",
    "    take a while to finish.\n",
    "    \"\"\"\n",
    "    print (\"Loading word list from file...\")\n",
    "    # inFile: file\n",
    "    inFile = open(WORDLIST_FILENAME, 'r')\n",
    "    # line: string\n",
    "    line = inFile.readline()\n",
    "    # wordlist: list of strings\n",
    "    wordlist = line.split(\" \")\n",
    "\n",
    "    print (len(wordlist), \"words loaded.\")\n",
    "    return wordlist\n",
    "\n",
    "def choose_word(wordlist):\n",
    "    \"\"\"\n",
    "    wordlist (list): list of words (strings)\n",
    "\n",
    "    Returns a word from wordlist at random\n",
    "    \"\"\"\n",
    "    return random.choice(wordlist)\n",
    "\n",
    "\n",
    "def check_guessedLetters():\n",
    "    guessed_word = \"-\" * len(chosen_word)\n",
    "    print(\"Welcome to the game, Hangman!\")\n",
    "    print(\"I am thinking of a word that is\", len(chosen_word), \"letters long.\")\n",
    "    print(\"------------\")\n",
    "    guesse_left = 10\n",
    "    guessed_letter = \"\"\n",
    "    Available_letters = [\"a\", \"b\", \"c\", \"d\", \"e\", \"f\", \"g\", \"h\", \"i\", \"j\", \"k\", \\\n",
    "                         \"l\", \"m\", \"n\", \"o\", \"p\", \"q\", \"r\", \"s\", \"t\", \"u\", \"v\", \\\n",
    "                         \"w\", \"x\", \"y\", \"z\"]\n",
    "    temp1 = []\n",
    "    \n",
    "\n",
    "  \n",
    "    def display_unusedLetters():\n",
    "        temp2 = []\n",
    "        for i in Available_letters:\n",
    "            if guessed_letter in Available_letters:\n",
    "                temp1.append(guessed_letter)   \n",
    "        for k in Available_letters:\n",
    "            if k not in temp1:\n",
    "                temp2.append(k)\n",
    "        print(\"Available letters: \",\"\".join(temp2))\n",
    "        temp2 = []\n",
    "                \n",
    "\n",
    "    while guesse_left != 0 and not guessed_word == chosen_word:\n",
    "        print (\"You have\", guesse_left, \"guesses left.\")\n",
    "        display_unusedLetters()\n",
    "        guessed_letter = input(\"Please guess a letter: \")\n",
    "        guessed_letter=guessed_letter.lower()\n",
    "        \n",
    "    \n",
    "        if len(guessed_letter) != 1:\n",
    "            print(\"Please input only one alphabet!\")\n",
    "            print(\"------------\")\n",
    "            \n",
    "        elif guessed_letter not in Available_letters:\n",
    "            print(\"You did not input the alphabet\")\n",
    "            print(\"------------\")\n",
    "            \n",
    "        elif guessed_letter in temp1:\n",
    "            print(\"You inputted the letter before!\")\n",
    "            print(\"------------\")\n",
    "        \n",
    "        elif guessed_letter in chosen_word:\n",
    "            guessed_word = fillin_guessedLetters(chosen_word, guessed_word, guessed_letter)\n",
    "            print(\"Good guess: \", guessed_word)\n",
    "            print(\"------------\")\n",
    "            \n",
    "        else:\n",
    "            print(\"Oops! That letter is not in my word: \", guessed_word)\n",
    "            guesse_left -= 1\n",
    "            print(\"------------\")\n",
    "            \n",
    "            \n",
    "    \n",
    "    \n",
    "    if guesse_left == 0:\n",
    "        print (\"You lose. The word was: \" + str(chosen_word))\n",
    "\n",
    "    else:\n",
    "        print (\"Congratulations, you won!\")\n",
    "    \n",
    " \n",
    "\n",
    "def fillin_guessedLetters(chosen_word, guessed_word, guessed_letter):\n",
    "    answer_letter = \"\"\n",
    "  \n",
    "    for i in range(len(chosen_word)):\n",
    "        if chosen_word[i] == guessed_letter:\n",
    "            answer_letter += guessed_letter \n",
    "        else:\n",
    "            answer_letter +=  guessed_word[i]\n",
    "    \n",
    "    return answer_letter\n",
    "\n",
    "      \n",
    "    \n",
    "\n",
    "wordlist = load_words()\n",
    "print(\"------------\")\n",
    "chosen_word = choose_word(wordlist)\n",
    "check_guessedLetters()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
