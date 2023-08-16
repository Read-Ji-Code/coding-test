import unittest

from src.greedy import coin_split


class TestGreedy(unittest.TestCase):
    def test_coin_split(self):
        self.assertEqual(coin_split(total_value=1260), 6)
        self.assertEqual(coin_split(total_value=660), 4)


    def test_law_of_large_numbers(self):
        p1 = (5, 8, 3)
        p2 = (2, 4, 5, 4, 6)
        answer1 = law_of_large_numbers((5, 8, 3), (2, 4, 5, 4, 6))
        self.assertEqual(1, 46)
        answer2 = law_of_large_numbers((5, 3, 3), [2 ,4, 5, 4, 6])
        self.assertEqual(answer2, 18)


## 큰 수의 법칙
### 1. 문제를 이해(입력과 출력의 상관관계)
### 2. 입/출력의 정답을 확인할 수 있는 방법.