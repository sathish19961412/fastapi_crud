from fastapi import FastAPI,HTTPException
from typing import List
from models import User,Gender,Roles,UserUpdateRequest
from uuid import UUID,uuid4
app=FastAPI()

db:List[User]=[
    User(
        id=uuid4(),
        first_name='sathish',
        last_name='mathew',
        gender=Gender.male,
        roles=[Roles.admin,Roles.user]
    ),
     User(
        id=uuid4(),
        first_name='guru',
        last_name='prasanth',
        gender=Gender.male,
        roles=[Roles.student]
    )
]

@app.get('/api/users')
def users():
    return db

@app.post('/api/users')
def addUser(user:User):
    db.append(user)
    return {'id':user.id}

@app.put('/api/users/{user_id}')
def updateUser(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name=user_update.first_name
            if user_update.last_name is not None:
                user.last_name=user_update.last_name
            if user_update.roles is not None:
                user.roles=user_update.roles
        return
    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exists"
    )

@app.delete('/api/users/{user_id}')
def deleteUser(user_id:UUID):

    for user in db:
        if user.id == user_id:
            db.remove(user)
        return {"msg":"Deleted"}

    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exists"
    )
