{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "6f14c3a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n",
      "Hello World\n",
      "Hello World \n",
      " Hello World\n",
      "www.salihalgul.com\n",
      "salihalgul\n",
      "python kursu: baştan sona python programlama öğreniyorum.\n",
      "PYTHON KURSU: BAŞTAN SONA PYTHON PROGRAMLAMA ÖĞRENIYORUM.\n",
      "Python Kursu: Baştan Sona Python Programlama Öğreniyorum.\n",
      "3\n",
      "True\n",
      "True\n",
      "-1\n",
      "*********************Contents*********************\n",
      "Content*******************************************\n",
      "*******************************************Content\n",
      "Python-Kursu:-Baştan-sona-Python-programlama-öğreniyorum.\n",
      "Python-Kursu:-Baştan-sona Python programlama öğreniyorum.\n",
      "PythonKursu:BaştansonaPythonprogramlamaöğreniyorum.\n",
      "Hello There\n"
     ]
    }
   ],
   "source": [
    "website = \"http://www.salihalgul.com\"\n",
    "course = \"Python Kursu: Baştan sona Python programlama öğreniyorum.\"\n",
    "\n",
    "message = \" Hello World \"\n",
    "message = message.strip()\n",
    "print(message)\n",
    "result = \" Hello World \".strip()\n",
    "print(result)\n",
    "result = \" Hello World \".lstrip()\n",
    "print(result)\n",
    "result = \" Hello World \".rstrip()\n",
    "print(result)\n",
    "result = website.lstrip(\"/:pth\")\n",
    "print(result)\n",
    "result = \"http://www.salihalgul.com\".strip(\"mocpth./:w\")\n",
    "print(result)\n",
    "result = course.lower()\n",
    "print(result)\n",
    "result = course.upper()\n",
    "print(result)\n",
    "result = course.title()\n",
    "print(result)\n",
    "result = course.count(\"a\", 0, 30)\n",
    "print(result)\n",
    "result = website.startswith(\"http\")\n",
    "print(result)\n",
    "result = website.endswith(\"com\")\n",
    "print(result)\n",
    "result = website.find(\"com\",0,10)\n",
    "print(result)\n",
    "result = \"Contents\".center(50, \"*\")\n",
    "print(result)\n",
    "result = \"Content\".ljust(50, \"*\")\n",
    "print(result)\n",
    "result = \"Content\".rjust(50, \"*\")\n",
    "print(result)\n",
    "result = course.replace(\" \", \"-\")\n",
    "print(result)\n",
    "result = course.replace(\" \", \"-\", 3)\n",
    "print(result)\n",
    "result = course.replace(\" \", \"\")\n",
    "print(result)\n",
    "result = \"Hello World\".replace(\"World\", \"There\")\n",
    "print(result)\n",
    "result = course.split(\" \")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "496c0616",
   "metadata": {},
   "source": [
    "message = \"Hello World\".replace(\"Hello\", \"This\")\n",
    "print(message)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8235de79",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36a08baf",
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
