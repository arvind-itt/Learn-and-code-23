{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "00fe4878-d723-4c99-8a1d-b16db4fe109c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "John's Body\n",
      "The human body is breathing.\n",
      "John's Brain\n",
      "The human body is breathing.\n",
      "The brain is thinking.\n",
      "John's Heart\n",
      "The human body is breathing.\n",
      "5 hello\n"
     ]
    }
   ],
   "source": [
    "class HumanBody:\n",
    "    def __init__(self, name):\n",
    "        self.__name = name  # Private attribute\n",
    "\n",
    "    def get_name(self):\n",
    "        return self.__name\n",
    "\n",
    "    def breathe(self):\n",
    "        return \"The human body is breathing.\"\n",
    "\n",
    "    def sleep(self):\n",
    "        return \"The human body is sleeping.\"\n",
    "\n",
    "\n",
    "\n",
    "class Heart(HumanBody):\n",
    "    def func1(self):\n",
    "        return str(5)+\" hello\"\n",
    "\n",
    "class Brain(HumanBody):\n",
    "    def think(self):\n",
    "        return \"The brain is thinking.\"\n",
    "\n",
    "\n",
    "\n",
    "def perform_actions(body_part):\n",
    "    print(body_part.get_name())\n",
    "    print(body_part.breathe())\n",
    "    if isinstance(body_part, Brain):\n",
    "        print(body_part.think())\n",
    "    elif isinstance(body_part, Heart):\n",
    "        print(body_part.func1())\n",
    "\n",
    "# Using the classes\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    body = HumanBody(\"John's Body\")\n",
    "    brain = Brain(\"John's Brain\")\n",
    "    heart = Heart(\"John's Heart\")\n",
    "\n",
    "    perform_actions(body)  # Polymorphism - the perform_actions function works for all body parts\n",
    "    perform_actions(brain)  # Polymorphism - the perform_actions function works for all body parts\n",
    "    perform_actions(heart)  # Polymorphism - the perform_actions function works for all body parts\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0e4effff-78c5-4301-9dcf-7fad3d227d0c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
