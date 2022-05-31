{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "244e332c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "88218c1a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lütfen bir sayı giriniz:12\n",
      "Girdiğiniz sayı pozitif ve  12 'tür.\n"
     ]
    }
   ],
   "source": [
    "x = int(input(\"Lütfen bir sayı giriniz:\"))\n",
    "\n",
    "while x < 0:\n",
    "    print(\"Sayınız negatif lütfen pozitif bir sayı giriniz.\")\n",
    "    x = int(input(\"Lütfen bir sayı giriniz:\"))\n",
    "\n",
    "print(f\"Girdiğiniz sayı pozitif ve \",x,\"'tür.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "6818a9fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "Fizz\n",
      "4\n",
      "Buzz\n",
      "Fizz\n",
      "7\n",
      "8\n",
      "Fizz\n",
      "Buzz\n",
      "11\n",
      "Fizz\n",
      "13\n",
      "14\n",
      "FizzBuzz\n",
      "15\n"
     ]
    }
   ],
   "source": [
    "for fizzbuzz in range(1,16):\n",
    "           if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:\n",
    "                print(\"FizzBuzz\")\n",
    "                continue\n",
    "           elif fizzbuzz % 3 == 0:\n",
    "                print(\"Fizz\")\n",
    "                continue\n",
    "           elif fizzbuzz % 5 == 0:\n",
    "                print(\"Buzz\")\n",
    "                continue\n",
    "           print(fizzbuzz)\n",
    "\n",
    "print(fizzbuzz)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "91c59fa3",
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
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
