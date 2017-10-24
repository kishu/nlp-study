02
통계 언어 모델링
===

---

자연어 텍스트에서 수행할 수 있는 전처리 작업 혹은 계산
* 단어 빈도 계산(1-gram, 2-gram, 3-gram)
* 주어진 텍스트의 MLE 개발
* MLE 모델의 스무딩 적용
* MLE의 백-오프 메커니즘 개발
* 믹스 앤 매치를 얻기 위한 데이터 보간법 적용
* 혼잡도를 통한 언어 모델 평가
* 모델링 언어에서 메트로폴리스-헤이스팅스 적용
* 언어 처리에서 깁스 샘플링 적용

---


단어의 빈도 계산
확률적 계산
===

---

# N-gram

통계와 확률을 바탕으로 한 색인 분석에 널리 사용
n개의 문자열 크기의 윈도우를 만들어 윈도우 단위로 추출
* 시퀀스 집합
* 출현 빈도수

n = 1 : unigram
n = 2 : bigram
n = 3 : trigram
n = 4 : quadgram(fourgram)

반복해 나타나는 키워드 조사
많이 반복하는 키워드 일수록 중요할 확률이 높다?

---

# "I am a boy" -> 3-gram
* "I m"
* " am"
* "am "
* "m a"
* " a "
* "a b"
* " bo"
* "boy"

---

# sony mdr 시리즈 검색

![ 80%](http://cfile7.uf.tistory.com/image/032A1241518FA6E90B3CFE)

검색어가 "mdr"?
* 키워드 색인으로 안됨
* n-gram으로 처리

---

# sony mdr-v55 -> 2-gram

``` text
"so", "on", "ny", "y ", " m", "md"
"dr", "r-", "-v", "v5", "55"
```

검색어가 "mdr" -> 2-gram으로 검색
``` text
"md", "dr"
```

단점
* 색인어 수, 인덱스 수, 만드는 시간, 공간낭비
* n의 크기에 따라 검색 품질 문제
  * 2-gram, 검색어 "father", 검색결과 "the fat player"
* "is", "has" ?
* 문서군에서 공통적으로 나오는 단어는 중요도를 낮춰야. -> td-if

---

# 텍스트 MLE 개발

MLE
최대우도추정(Maximum Likelihood Estimation)
텍스트에서 주어진 발생에 대한 확률 분포를 포함하는 freqdist 생성에 사용

![](http://cfile9.uf.tistory.com/image/13013B344F79105C266660)

https://m.blog.naver.com/jaebum8888/220747546227

---

# 은닉 마르코프 모델

![](http://cfile29.uf.tistory.com/image/221BAF4357C981D60ABBA8)

http://dl.dongascience.com/magazine/view/M201209N010

---

MLE 모델의 스무딩
===

---
이전에 발생하지 않은 단어가 나오면 조건부 확률이 0이 되는 문제 해결
* 라플라스 스무딩
* Good Turing
* 크네저 네이 추정
* 위튼 벨 추정



