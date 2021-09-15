{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "양정수를 입력하세요: 3\n",
      "양정수를 입력하세요: 5\n",
      "양정수를 입력하세요: 7\n",
      "양정수를 입력하세요: 3\n",
      "양정수를 입력하세요: -1\n",
      "error! negative integer\n",
      "최대값은:  7\n",
      "최소값은:  3\n",
      "합은:  18\n",
      "평균은:  4.5\n"
     ]
    }
   ],
   "source": [
    "# Homework Assignment 1-1 \n",
    "# Name: 최윤정 \n",
    "# Time Spent: 2:00\n",
    "\n",
    "def my_max(L):\n",
    "    return max(L)\n",
    "def my_min(L):\n",
    "    return min(L)\n",
    "def my_sum(L):\n",
    "    return sum(L)\n",
    "def my_ave(L):\n",
    "    return sum(L)/len(L)\n",
    "\n",
    "L=[]\n",
    "while (1):\n",
    "    x=int(input(\"양정수를 입력하세요: \"))\n",
    "    if x>=0:\n",
    "        L.append(x)\n",
    "    else:\n",
    "        print(\"error! negative integer\")\n",
    "        break\n",
    "        \n",
    "print(\"최대값은: \",my_max(L))\n",
    "print(\"최소값은: \",my_min(L))\n",
    "print(\"합은: \",my_sum(L))\n",
    "print(\"평균은: \",my_ave(L))"
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
