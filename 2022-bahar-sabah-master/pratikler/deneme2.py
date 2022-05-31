{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b22189b",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "cevap = input(\"x in değeri 2 olsun mu? y/n\")\n",
    "if cevap == \"y\": # cevap == \"y\" testimiz oluyor\n",
    "    x = 2\n",
    "else:\n",
    "    x = 0\n",
    "\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1547682b",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'Python 3.11.0b1 64-bit' requires ipykernel package.\n",
      "Run the following command to install 'ipykernel' into the Python environment. \n",
      "Command: 'c:/Users/salih/AppData/Local/Programs/Python/Python311/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "x = int(input(\"Lütfen bir sayı giriniz:\"))\n",
    "\n",
    "while x < 0:\n",
    "    print(\"Sayınız negatif lütfen pozitif bir sayı giriniz.\")\n",
    "    x = int(input(\"Lütfen bir sayı giriniz:\"))\n",
    "print(\"Girdiğiniz sayı pozitif ve\", x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "201135d6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "interpreter": {
   "hash": "701ff2241ceae646732b1645173280069c74bbc33375d604aef0f5f117b7c504"
  },
  "kernelspec": {
   "display_name": "Python 3.11.0b1 64-bit",
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
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
