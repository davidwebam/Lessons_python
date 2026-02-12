"""1․ Գրել MyShows class, որը․
   - __init__ ում կստանա 
     -- սերիալի անունը (պետք է լինի տեքստ),
     -- հարթակը, որտեղ ցուցադրվում է սերիալը (պետք է լինի տեքստ), 
     -- առաջին սերիան դուրս գալու տարեթիվը (պետք է լինի ամբողջ թիվ),
     -- սերիայի համարը, որը դիտում է օգտատերը (որ սերիային է հասել) (պետք է լինի ամբողջ թիվ), default արժեքը պետք է լինի 1,
     -- օգտատիրոջ դրած գնահատականը (պետք է լինի ամբողջ թիվ 1-10 միջակայքում), default արժեքը պետք է լինի None,
     -- գլխավոր դերասանների ցանկը (պետք է լինի լիստ),
   - բոլոր ատրիբուտները կլինեն private,
   - կունենա getter բոլոր ատրիբուտների համար,
   - միայն սերիայի համարի և գնահատականի համար կունենա նաև setter,
   - միայն գնահատականի համար կունենա նաև deleter, այնպես պետք է ռեալիզացնել, որ գնահատականը ջնջելուց հետո այն նորից սահմանելու հնարավորություն լինի,
   - կունենա մեթոդներ դերասանների ցանկը թարմացնելու համար (լիստից անուն ջնջել, լիստում անուն ավելացնել),
   - կունենա մեթոդ, որը կվերադարձնի սերիալի մասին ամբողջ ինֆորմացիան։"""
   
class MyShows:
  def __init__(self, name, platform, year, reached=1, rating=None, *, actors):
    self._validate_name(name)
    self._validate_platform(platform)    
    self._validate_year(year)
    self._validate_reached(reached)
    self._validate_rating(rating)
    self._validate_actors(actors)
    
    self.__name = name
    self.__platform = platform
    self.__year = year
    self.__reached = reached
    self.__actors = actors
    self.__rating = rating
    
  @staticmethod
  def _validate_name(name):
    if not isinstance(name, str):
      raise TypeError('Name should be a string')
    
  @staticmethod
  def _validate_platform(platform):
    if not isinstance(platform, str):
      raise TypeError('Platform should be a string')
    
  @staticmethod
  def _validate_year(year):
    if not isinstance(year, int):
      raise TypeError('Year should be an integer')
    
  @staticmethod
  def _validate_reached(reched):
    if not isinstance(reched, int):
      raise TypeError('Reached should be an integer')
    
  @staticmethod
  def _validate_rating(rating):
    if not isinstance(rating, int):
      raise TypeError('Rating should be an integer')
    elif not 0 <= rating <= 10:
      raise ValueError('Rating should be between 0 and 10')
  
  @staticmethod
  def _validate_actors(actors):
    if not isinstance(actors, list):
      raise TypeError('Actors should be a list')
    
    
  
  @property
  def name(self):
      return self.__name

  @property
  def platform(self):
      return self.__platform

  @property
  def year(self):
      return self.__year

  @property
  def reached(self):
      return self.__reached

  @property
  def rating(self):
      return self.__rating

  @property
  def actors(self):
      return self.__actors
    
    
  @rating.setter
  def rating(self, rating):
    self._validate_rating(rating)
    self.__rating = rating
  
  @reached.setter
  def reached(self, reached):
    self._validate_reached(reached)
    self.__reached = reached
    
    
  @rating.deleter
  def rating(self):
    self.__rating = None
  
  
  def add_actor(self, actor):
    if not isinstance(actor, str):
      raise TypeError('Actor should be a string')
    elif actor not in self.__actors:
      self.__actors.append(actor)
    else:
      raise ValueError('Actor already exists')
      
  def remove_actor(self, actor):
    if actor in self.__actors:
      self.__actors.remove(actor)
    else:
      raise ValueError('Actor not found')
    
  
  def get_full_info(self):
    return (
        f"Name: {self.__name}\n"
        f"Platform: {self.__platform}\n"
        f"Year: {self.__year}\n"
        f"Reached: {self.__reached}\n"
        f"Rating: {self.__rating}\n"
        f"Actors: {', '.join(self.__actors)}"
    )

movie = MyShows(
    'The Matrix',
    'Netflix',
    1999,
    reached=1000000,
    rating=0,
    actors=['Gaspar Hayrapetyan', 'Vaspur Harutyunyan', 'Varazdat Xaribyan']
)


movie.rating = 8
movie.add_actor('Tony Stark')
print(movie.get_full_info())

    
  