# project07

#### 1) 1 : N의 관계를 설정하기 

​	Genre : Movie 

​	Movie : Score

​	FK 설정:  `부모테이블소문자 = models.ForeignKey(부모테이블, on_delete=models.CASCADE)`

```python
class Genre(models.Model):
    name = models.CharField(max_length = 20)

class Movie(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description= models.TextField()
    

class Score(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content =  models.CharField(max_length = 140)
    score = models.IntegerField()

```



#### 2) 1:N 관계 테이블 접근하기

1.  부모의 pk로 자식 테이블 접근하기

   ``` python
   movie = Movie.objects.get(pk = movie_pk)
   scores = movie.score_set.all()
   ```

   

2.  자식의 pk로 부모 테이블 접근하기

   ```python
   movie = Movie.objects.get(pk = movie_pk)
   genre = Genre.objects.get(pk = movie.genre_id)
   ```

   

