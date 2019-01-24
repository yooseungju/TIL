# Bootstrap 사용법과  components 정리



## 1. Grid System

| 반응형 사이즈       | Extra small | Small    | Medium   | Large   | Extra large |
| ------------------- | ----------- | :------- | -------- | ------- | ----------- |
| Max container width | None        | 540px    | 720px    | 960px   | 1140px      |
| Class prefix        | .col-       | .col-sm- | .col-md- | .col-lg | .col-xl     |

##### Bootstrap grid system은 레이아웃을 12개의 column, 5개의 반응형 사이즈 조건을 사용하여 구축한다.

---

##### Bootsptrap은 column 단위로 사이즈를 구성할 수 있다. 

```html
<div class="row">
        <div class="square col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12"></div>
        <div class="square col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12"></div>
        <div class="square col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12"></div>
        <div class="square col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12"></div>
        <div class="square col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12"></div>
        <div class="square col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12"></div>
        <div class="square col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12 "></div>
        <div class="square col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12 "></div>
        <div class="square col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12 "></div>
        <div class="square col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12 "></div>
        <div class="square col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12 "></div>
        <div class="square col-xl-2 col-lg-3 col-md-4 col-sm-6 col-12 "></div>
</div>
```
- col-xl-2 : container width >= xl 일때 size는 12/2의 크기이다.

- col-lg-3: container width >= lg 일때 size는 12/3의 크기이다.
- col-md-4: container width >= md 일때 size는 12/4의 크기이다.

- col-sm-6: container width >= sm 일때 size는 12/6의 크기이다.

- col-12: container width <= sm 일때 size는 12/2의 크기이다.

## 2. components
#### 1.alerts



## .Flexbox

정렬 기능을 제공하기 위한 1차원 레이아웃 모델이다.(1차원이란 행,열 만을 다룬다) 

flexbox 를 이용하기위해 부모요소에  **display: flex;** 를 적용해야한다.

#### 1. flex-direction

요소들의 정렬방향축을 결정한다.

flexbox 두개의 교차축이 존재한다.  flex-direction을 이용하여 정렬축을 결정하는데 어느 축을 주축으로 정하느냐에 따라 flexbox의 동작이 결정되기 때문에 중요하다.

- **row** : 정렬축이 inline으로 수평을 따른다.       `주축 - 수평`
- **row-reverse** : row와 시작점이 반대이다. 
- **column**: 정렬축이 하단으로 blockd으로  수직이다.   `주축 - 수직`
- **column**: column과 시작점이 반대이다. 



#### 2. flex-wrap

요소들을 줄 바꿈할지 여부를 결정한다. 

- **wrap**:  요소들의 크기가 container의 크기보다 클 경우 여러행에 나누어 결정된다.
- **nowrap**: 요소들을 container에 맞추어 모든 요소들은 넣는다.



#### 3. align-items

flex-direction의 주축을 따라 정렬된 flex요소의 수직 정렬 방식을 결정한다.

`주축이 수평이면 수직, 주축이 수직이면 수평`

- **flex-start** : 수직 시작점부터 정렬
- **flex-end**: 수직 끝점부터 정렬된다.
- **stretch**: `초기값`항목의 높이는 flex 컨테이너내 flex항복 수직의 최대 높이로 지정 된다.
- **center**: 항목들이 가운데 라인에 정렬된다.



#### 4. justify-content

flex-direction의 주축을 따라 정렬된 flex요소의 수평 정렬 방식을 결정한다.

`주축이 수평이면 수평, 주축이 수직이면 수평`

- **flex-start** :  `초기값` 주축의 수평 시작점부터 정렬

- **flex-end**: 주축의 수평 끝점부터 정렬된다.

- **stretch**: 

- **center**:

- **space-around**:

- **space-between**:

  




