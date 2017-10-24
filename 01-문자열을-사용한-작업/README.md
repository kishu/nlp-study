예제코드 : https://github.com/PacktPublishing/Mastering-Natural-Language-Processing-with-Python

# 문자열을 사용한 작업
## NLP
* 자연어와 컴퓨터 간 상호작용에 관한 것
* 컴퓨터와 인간의 원할한 상호작용을 제공
* 컴퓨터가 머신러닝을 이용해 인간의 언어를 이해할 수 있는 기능 제공

NLP에서 문자열을 다루는 것이 중요하다.

## 토큰화 Tokenization
* 텍스트를 토큰이라는 작은 부분으로 분할하는 과정
* NLP에서 아주 중요한 단계
* [NLTK](http://www.nltk.org/) 사용

### 텍스트를 문장으로
* `sent_tokenize()`
* `PunktSentenceTokenizer` 로드 후 `tokenize()`

### 문장을 단어로
* `word_tokenize()` - 스페이스와 문장 부호 기준
* `TreebankWordTokenizer`를 사용해 `tokenize()`
  - 축약형을 분리
  - `"Don't"` -> `"Do"`, `"n't"`
* `PunktWordTokenizer`를 사용해 `tokenize()`
  - 문장 부호를 새로운 토큰으로 분할
  - `"Don't"` -> `"Don'"`, `"'"`, `"t"`

### 토크나이저 상속 트리
  ```
  Tokenizer
    - PunkWordTokenizer
    + RegexpTokenizer
        - WordPunctTokenizer
        - WhitespaceTokenizer
    - TreebankWordTokenizer
  ```

### 정규표현식을 사용한 토큰화
* 두가지 정규표현식을 통해 단어 토큰화
  - 단어로 매칭
  - 스페이스 혹은 공백으로 매칭
* `RegexpTokenizer` 인스턴스로 사용
  - 단어 매칭 토큰화는 `re.findall()`
  - 공백 혹은 스페이스로 토큰화는 `re.split()`
* `regexp_tokenize()` 함수로 사용
* `RegexpTokenizer`의 서브클래스로 미리 정의된 정규표현식 사용
  - `BlanklineTokenizer`
  - `WhitespaceTokenizer`
  - `LineTokenizer`
  - `SpaceTokenizer`
* `nltk.tokenize.util` 모듈은 문장에서 토큰의 오프셋 튜플의 순서 반환
  - `" She secured 90.56 % ..."` 
  - `[(1, 4), (5, 12), (13, 18), ... ]`
  - `span`, 구분자 적용 가능

## 정규화 Normalization
자연어 텍스트 처리 하려면
* 문장 부호 제거
* 텍스트를 소문자 혹은 대문자로 변환
* 숫자를 단어로 변환
* 약어 전개
* 텍스트 정규화
등등의 정규화를 수행해야 한다.

### 문장 부호 제거
* 토큰화 하는 동안 문장 부호를 제거하는게 좋을 경우가 있다.
* `NLTK`에서 정규화하는 동안 문장 부호 제거는 주요 작업이다.

### 소문자와 대문자로 변환
* `lower()`, `upper()`

### 불용어 stop words 처리
* 불용어는 문장의 전체적인 의미에 영향을 주지 않는다.
* 따라서 정보 검색 작업 혹은 자연어 작업 동안 필터링 해야 한다.
* 많은 검색 엔진은 검색 공간을 줄이기 위해 불용어를 삭제한다.
* 불용어 제거는 NLP의 중요 정규화 작업이다.
* `NLTK`는 많은 언어데 대한 불용어 목록이 있다. 

## 토큰의 대체 및 수정
* 토큰을 다른 토큰으로 대체하는 방법
* 잘못된 철자의 토큰을 올바른 철자의 토큰으로 수정하는 방법

### 정규 표현식을 사용한 단어 대체
* 정규 표현식으로 `"doesn't"` -> `"does not"`

### 텍스트를 다른 텍스트로 대체
* n/a

### 토큰화 전에 대체 수행
* 토큰 대체를 토큰화 전에 수행해야 축약형을 토큰화하면서 발생하는 문제를 해결 할 수 있다.

### 반복하는 문자 처리
* `"lotttt"` -> `"lot"`
* `"happy"` -> `"hapy"` ???
  - `wordnet`을 임베드 한다.

### 단어를 동의어로 대체
* `"congrats"` -> `"congratulations"`

## 텍스트에 지프의 법칙 적용
* 지프의 법칙(Zipf's law)에 따르면 텍스트의 토큰중 가장 많이 나오는 토큰과 가장 적게 나오는 토큰은 정비례한다.

> 지프의 법칙 : 어떠한 자연어 말뭉치 표현에 나타나는 단어들을 그 사용 빈도가 높은 순서대로 나열하였을 때, 모든 단어의 사용 빈도는 해당 단어의 순위에 반비례한다. 따라서 가장 사용 빈도가 높은 단어는 두 번째 단어보다 빈도가 약 두 배 높으며, 세 번째 단어보다는 빈도가 세 배 높다.

## 유사 척도
* `NLTK`의 `nltk.metrics` 패키지는 NLP 작업에 도움을 주는 다양한 평가 혹은 유사 척도 측정 방법을제공한다.
* NLP에서 태거(taggers), 청커(chunkers) 등의 성능을 테스트하기 위해 정보 검색에서 검색된 표준 점수를 사용할 수 있다.

## 편집 거리(Edit distance) 알고리즘
* 리벤슈타인 편집 거리(Levenshtein edit distance)라고도 함
* 두 문자열을 동일하게 하는 삽입, 대체 혹은 삭제될 수 있는 문자의 수를 계산하기 위해 사용
* http://hsp1116.tistory.com/41 참고

## 자카드 계수를 사용한 유사 척도
* 타니모토 계수(Tanimoto coefficient)라고도 함
* X와 Y의 두 세트의 오버랩 측정으로 정의
* https://www.slideshare.net/TaeYoungLee1/20141214-similarityclustering 참고