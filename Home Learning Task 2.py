{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Home Learning Task 2.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "Task 1\n",
        "\n",
        "The program that does the following:\n",
        "\n",
        "a) Stores a random number (1 10) in a variable see hint below.\n",
        "\n",
        "b) Asks a user for their name and stores this in a variable.\n",
        "\n",
        "c) Asks a user to guess the number between 1 and 10.\n",
        "\n",
        "d) Tells the user whether they have guessed correctly."
      ],
      "metadata": {
        "id": "5pMfD4CnGv5T"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 22,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t3w_FQgN56gK",
        "outputId": "ad6ed6ec-e905-47c6-99d3-a3cfee8fae47"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "What is your name? a\n",
            "Hello a can you guess a number from 1 to 10?\n",
            " 1\n",
            "guess again?\n",
            " 2\n",
            "again?\n",
            " 3\n",
            "Play guess the number Again\n"
          ]
        }
      ],
      "source": [
        "#Task 1\n",
        "import random\n",
        "number = random.randint(0,10)\n",
        "#print(number)\n",
        "\n",
        "user_input = input(\"What is your name? \")\n",
        "print(\"Hello\", user_input, \"can you guess a number from 1 to 10?\")\n",
        "\n",
        "user_input_number1 = int(input(\" \"))\n",
        "if user_input_number1 == number:\n",
        "  print(\"It took you one turn to guess my number, which was\", number)\n",
        "  print(\"Play guess the number Again\")\n",
        "elif user_input_number1 != number:\n",
        "  print(\"guess again?\")  \n",
        "\n",
        "user_input_number2 = int(input(\" \"))\n",
        "if user_input_number2 == number:\n",
        "  print(\"It took you two turns to guess my number, which was\", number)\n",
        "  print(\"Play guess the number Again\")\n",
        "elif user_input_number2 != number:\n",
        "  print(\"again?\")  \n",
        "\n",
        "user_input_number3 = int(input(\" \"))\n",
        "if user_input_number3 == number:\n",
        "  print(\"It took you three turns to guess my number, which was\", number)\n",
        "  print(\"Play guess the number Again\")\n",
        "else:\n",
        "    print(\"Play guess the number Again\")"
      ]
    }
  ]
}