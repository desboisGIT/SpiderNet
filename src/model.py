from .object import MyObject

class SpiderNetModel:
    def __init__(self): 
        self.objects = []

    def create_object(self, object_name, attributes):
        new_object = MyObject(object_name, attributes) 
        self.objects.append(new_object)

    def get_objects(self):
        return self.objects

    def feed(self, object_name, data):
        for obj in self.objects:
            if obj.name == object_name:
                obj.push(data)  
                return
        raise ValueError(f"Object '{object_name}' not found.")
        
    def predict(self, object_name, field, input_data):
        for obj in self.objects:
            if obj.name == object_name:
                
                return obj.get_recomendation(field, input_data)
        raise ValueError(f"Object '{object_name}' not found.")
    
    def __str__(self):

        result = f'SpiderNetModel with {len(self.objects)} objects:\n'
        for obj in self.objects:
            result += str(obj) + '\n' 
        return result.strip()
