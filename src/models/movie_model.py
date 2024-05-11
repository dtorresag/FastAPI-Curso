 #Schema
import datetime
from pydantic import BaseModel, Field


class Movie(BaseModel):
    id:int
    title:str
    overview:str
    year:int

class MovieUpdate(BaseModel):
    title:str
    overview:str
    year:int

class MovieCreate(BaseModel):
    id:int
    title:str = Field(min_length= 5, max_length= 30)
    overview:str 
    year:int = Field(le=datetime.date.today().year, ge=1900)

    model_config = {

        'json_schema_extra':{
            'example':{
                'id': 1,
                'title': "My movie",
                'overview': "This movie is about...",
                'year':2000
            }
        }
    }
    
#    @Validator('title')
#    def validateTitle(cls, value):
#        if len(value)<5:
#            raise ValueError('Title must have minimun length of 5 characters')
#        if len(value)>30:
#            raise ValueError('Title must hava a maximun of 30 characters')
#        return value