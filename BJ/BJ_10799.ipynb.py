{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 백준 10799\n",
    "### 쇠막대기 문제\n",
    "#### Point! 언제 결과 값이 늘어나는지 파악 하는 것이 중요\n",
    "*레이저로 자를때,  쇠막대기가 닫힐때*\n",
    "\n",
    "\n",
    ">1. 입력을 분석해서 쇠막대기이면 쇠막대기 스택에 push()\n",
    "2. \"(\"괄호가 나왔을때 레이저인지 막대기의 닫는 괄호인지 분석하기위해 전 괄호를 사용한다.\n",
    "3. \") 괄호의 직전괄호가 \"( 결과값을 쇠막대기 수만큼 증가 시킨다.\n",
    "\n",
    "---- \n",
    "https://programmers.co.kr/learn/courses/30/lessons/42585"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "()(((()())(())()))(())\n",
      "17\n"
     ]
    }
   ],
   "source": [
    "# ()(((()())(())()))(()) -> 17\n",
    "# 파이프가 닫힐때 하나 생기는것 ++ 1나 추가 \n",
    "l_list = list(input())\n",
    "result = 0 \n",
    "stack = []\n",
    "pre = \"\"\n",
    "for em in l_list:\n",
    "    if em == \")\" and pre == \"(\":\n",
    "        stack.pop()\n",
    "        result += len(stack)          \n",
    "    elif em == \"(\":\n",
    "        stack.append(\"(\")\n",
    "    else:\n",
    "        stack.pop()\n",
    "        result +=1  \n",
    "    pre = em\n",
    "    \n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
