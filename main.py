from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# @app.get('/')
# def index():
#     return {'data': {'name': 'Devaditya'}}

# @app.get('/about')
# def about():
#     return {'data': 'about page'}

# the function name doesnt matter. whats matter is the decorator we can even use same function name for different decorators also 
 
# now we wanna show all blogs 
@app.get('/')
def index():
    return {'data': 'blog list'}

@app.get('/blog')
def get_blogs(limit:int=10, published:bool=True, sort:Optional[str] = None):
    # only want 10 published blogs from the database instead of forking the whole database in once
    # now as you can see if we define a value for one of the perams then we have to define a default value for all the perams but to overcome this we have to import Optinal from typing library by using of which we can set that a perticular query is optional its syntax it Optional[data_type] = value.
    if (published == True):
        return {'data': f'{limit} published blogs from the list'}
    else:
        return {'data': f'{limit} blogs from the list'}

@app.get('/blog/something')
def something():
    return {'data': 'somthing'}  # to ne noted - fastapi reads the file line by line so in the same route place the static routes before the dynamic routs. for example if i place "something" route after the id route it will give error saying that int-parsing error cause we are specifying int in the 'id' route and it will get encountered first.

@app.get('/blog/{id}')
def show(id: int):
    #fetch blogh with id = id   
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    return{'data': {'1', '2'}}


