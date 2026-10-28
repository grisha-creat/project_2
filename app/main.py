from fastapi import FastAPI
from app.schemas.post import PostCreate



app = FastAPI(title='CMS API')



posts_db = []
post_id = 1



@app.get('/')
def root():
     return {"message": "CMS API работает"}
 

 
@app.get('/posts')
def get_posts():
    return {'posts':posts_db}



@app.post('/posts')
def create_posts(post:PostCreate):
    global post_id
    new_post = {'id': post_id, 'title': post.title, 'content': post.content}
    posts_db.append(new_post)
    post_id+=1
    return new_post



@app.get('/posts/{post_id}')
def  get_post(post_id :int):
    for post in posts_db:
        if post['id'] == post_id:
            return post
    return {'ERROR': 'пост не найден'}    
    
    
     
@app.put('/posts/{post_id}')
def  get_post(post_id :int, updated_post: PostCreate):
    for post in posts_db:
        if post['id'] == post_id:
            post['title'] = updated_post.title
            post['content'] = updated_post.content
            return post           
    return {'ERROR': 'пост не найден'}



@app.delete('/posts/{post_id}')
def post_delete(post_id: int):
    for  i, post in enumerate(posts_db):
        if post['id'] == post_id:
            posts_db.pop(i)
            return {'message': 'пост удален'}
    return {'ERROR': 'пост не найден'}    
    
    
