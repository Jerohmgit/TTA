{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Home Learning Task 3.ipynb",
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
        "Create your own Flow Diagram, a subject of your own choice, \n",
        "\n",
        "Example: Fast food order and convert it into code.\n",
        "\n",
        "Solution: see Flow Diagram Task 1.pdf\n",
        "\n",
        "(Home Learning Task 2 e.g. Write a program that allows user to enter their favourite starter, main course dessert and drink.\n",
        "\n",
        "Concatenate these and output a message which says––“Your favourite meal is………with a glass of….”)"
      ],
      "metadata": {
        "id": "n1a4svAxl3aw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Task 1 #refactor code from Home Learning Task 2\n",
        "\n",
        "def function():\n",
        "  name = input(\"What is your name? \")\n",
        "\n",
        "  output = \"Hello\", name + \"!\" , \"what is your favourite starter, main course, dessert and drink?\"\n",
        "\n",
        "  return output\n",
        "\n",
        "user = function()\n",
        "print(user)\n",
        "\n",
        "def function_order():\n",
        "  starter = input(\"\")\n",
        "  main_course = input(\"\")\n",
        "  dessert = input(\"\")\n",
        "  drink = input(\"\")\n",
        "\n",
        "  output = \"Your favourite meal is\", starter + \" for starter,\", main_course + \" for main, and\", dessert + \" for dessert\", \"……… with a glass of\", drink + \"!\"\n",
        "\n",
        "  return output\n",
        "\n",
        "order = function_order()\n",
        "print(order)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aSeUr-bJmHpw",
        "outputId": "82a713ae-98ef-4e47-f62a-ebbfe93eec66"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "What is your name? a\n",
            "('Hello', 'a!', 'what is your favourite starter, main course, dessert and drink?')\n",
            "q\n",
            "w\n",
            "e\n",
            "r\n",
            "('Your favourite meal is', 'q for starter,', 'w for main, and', 'e for dessert', '……… with a glass of', 'r!')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Task 2\n",
        "\n",
        "As an extension to the motorbike task that costs £2000 and loses 10% of its value every year. \n",
        "\n",
        "Set up a function that performs the calculation by passing in parameters. \n",
        "\n",
        "Then using a loop, print the value of the bike every following year until it falls below £1000\n",
        "\n",
        "(Home Learning Task 2 e.g. A motorbike costs £2000 and loses 10% of its value every year. \n",
        "\n",
        "Using a loop, print the value of the bike every following year until it falls below £1000.)"
      ],
      "metadata": {
        "id": "yH8bMGFeuMNO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Task 2 #refactor code from Home Learning Task 2\n",
        "\n",
        "bike = 2000\n",
        "\n",
        "def depreciation(value):\n",
        "\n",
        "  output = \"The value of a motorbike costs £2000 and loses 10% of its value every following year equal to £\" + str(value)\n",
        "\n",
        "  return output\n",
        "\n",
        "while bike > 1000: #until it falls below £1000\n",
        "  bike = bike * 0.9\n",
        "  \n",
        "  print(depreciation(bike))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "88b35be7-f575-4b64-d4b0-8ecca61a6342",
        "id": "qt1pYMZ-wynJ"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The value of a motorbike costs £2000 and loses 10% of its value every following year equal to £1800.0\n",
            "The value of a motorbike costs £2000 and loses 10% of its value every following year equal to £1620.0\n",
            "The value of a motorbike costs £2000 and loses 10% of its value every following year equal to £1458.0\n",
            "The value of a motorbike costs £2000 and loses 10% of its value every following year equal to £1312.2\n",
            "The value of a motorbike costs £2000 and loses 10% of its value every following year equal to £1180.98\n",
            "The value of a motorbike costs £2000 and loses 10% of its value every following year equal to £1062.882\n",
            "The value of a motorbike costs £2000 and loses 10% of its value every following year equal to £956.5938000000001\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Task 3\n",
        "\n",
        "Write a program which will ask for two numbers from a user. \n",
        "\n",
        "Then offer an option menu to the user giving them a choice of maths operators.\n",
        "\n",
        "Once the user has selected which operator they wish to use, perform the calculation by using a procedure and passing parameters.\n",
        "\n",
        "(Home Learning Task 2 e.g. Write a program which will ask for two numbers from a user. \n",
        "\n",
        "Then offer a menu to the user giving them a choice of operator:\n",
        "\n",
        "e.g. Enter “a” if you want to add “b” if you want to subtract\n",
        "\n",
        "Include +,--, /, *, ** square (to the power of).) \n",
        "\n",
        "Once the user has selected which operator they wish to use, perform the calculation."
      ],
      "metadata": {
        "id": "HFJy_QHojICY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Task 3 #refactor code from Home Learning Task 2\n",
        "\n",
        "def user(input_name):\n",
        "\n",
        "  print(\"Hello\", input_name + \"!\" , \"Please ask for two numbers?\", '\\n')\n",
        "\n",
        "name = input(\"What is your name? \")\n",
        "\n",
        "user(name)\n",
        "\n",
        "number_1 = int(input(\"1st number: \"))\n",
        "number_2 = int(input(\"2nd number: \"))\n",
        "\n",
        "def choose_operator():\n",
        "\n",
        "  print('\\n', \"Please choose a math operator:\")\n",
        "  print(\"+ : This is to add\")\n",
        "  print(\"- : This is to subtrack\")\n",
        "  print(\"* : This is to multiply\")\n",
        "  print(\"/ : This is to divide\")\n",
        "  print(\"//: This is to divide and show the integer value\")\n",
        "  print(\"% : This shows the remainder value\")\n",
        "  print(\"**: This will do a multiplication to the power of\", '\\n')\n",
        "  \n",
        "choose_operator()\n",
        "\n",
        "math_operator = input(\"operator is: \")\n",
        "print(\"\")\n",
        "\n",
        "def math(math_operator):\n",
        "  \n",
        "  if math_operator == \"+\":\n",
        "    output = print(\"The calculation is:\", number_1 + number_2)\n",
        "    return output\n",
        "  elif math_operator == \"-\":\n",
        "    output = print(\"The calculation is:\", number_1 - number_2)\n",
        "    return output\n",
        "  elif math_operator == \"*\":\n",
        "    output = print(\"The calculation is:\", number_1 * number_2)\n",
        "    return output\n",
        "  elif math_operator == \"/\":\n",
        "    output = print(\"The calculation is:\", number_1 / number_2)\n",
        "    return output\n",
        "  elif math_operator == \"//\":\n",
        "    output = print(\"The calculation is:\", number_1 // number_2)\n",
        "    return output\n",
        "  elif math_operator == \"%\":\n",
        "    output = print(\"The calculation is:\", number_1 % number_2)\n",
        "    return output\n",
        "  elif math_operator == \"**\":\n",
        "    output = print(\"The calculation is:\", number_1 ** number_2)\n",
        "    return output\n",
        "  else: #no choice of math_operator    \n",
        "    print(\"You have not typed a valid operator, please run the program again.\")\n",
        "    print(\"Python can perform mathematical computations easily.\")\n",
        "    \n",
        "calculate = math_operator\n",
        "\n",
        "math(calculate)\n",
        "\n"
      ],
      "metadata": {
        "id": "olCMYJOGKld3",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fd6a4290-6401-41a0-99a1-d6b98f4199b6"
      },
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "What is your name? q\n",
            "Hello q! Please ask for two numbers? \n",
            "\n",
            "1st number: 2\n",
            "2nd number: 1\n",
            "\n",
            " Please choose a math operator:\n",
            "+ : This is to add\n",
            "- : This is to subtrack\n",
            "* : This is to multiply\n",
            "/ : This is to divide\n",
            "//: This is to divide and show the integer value\n",
            "% : This shows the remainder value\n",
            "**: This will do a multiplication to the power of \n",
            "\n",
            "operator is: //\n",
            "\n",
            "The calculation is: 2\n"
          ]
        }
      ]
    }
  ]
}