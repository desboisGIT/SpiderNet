import json
from src.model import SpiderNetModel

def test_user_model():
    user_model = SpiderNetModel()
    user_field = {
        "full_name": str,
        "email": str,
        "country": str,
        "like_number": int,
        "liked_gender": list,
    }
    
    
    user_model.create_object("user", user_field)

    
    with open('test_data.json', 'r') as file:  
        test_data = json.load(file)
        
        
        for user in test_data:
            user_model.feed("user", user)

    print(user_model)

    
    print(user_model.predict("user", "liked_gender", ['jazz']))

test_user_model()
