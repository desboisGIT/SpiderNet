from .field import Field

class MyObject:
    def __init__(self, object_name, attributes):
        if not isinstance(object_name, str):
            raise TypeError(f"Expected object_name to be a string, got {type(object_name).__name__} instead.")
        
        if not isinstance(attributes, dict):
            raise TypeError(f"Expected attributes to be a dictionary, got {type(attributes).__name__} instead.")
        
        self.name = object_name
        self.fields = {}  
        self.elements = []

        
        for field_name, field_type in attributes.items():
            if not isinstance(field_name, str):
                raise TypeError(f"Expected field_name to be a string, got {type(field_name).__name__} instead.")
            if not isinstance(field_type, type):
                raise TypeError(f"Expected field_type to be a type (e.g., int, str), got {type(field_type).__name__} instead.")
            
            
            self.fields[field_name] = Field(field_name, field_type)

    def push(self, element):
        if not isinstance(element, dict):
            raise TypeError(f"Expected element to be a dictionary, got {type(element).__name__} instead.")
        
        
        for field_name, field in self.fields.items():
            if field_name not in element:
                raise ValueError(f"Missing required field '{field_name}' in the element.")
            if not isinstance(element[field_name], field.field_type):
                raise TypeError(f"Expected field '{field_name}' to be of type {field.field_type.__name__}, got {type(element[field_name]).__name__} instead.")
        
        
        self.elements.append(element)
        
    def get_recomendation(self, field, input_data):
        prediction_counts = {}  

        for user, element in enumerate(self.elements):
            for i in input_data:
                for j in element[field]:
                    if i == j:
                        print(f"user {user} also liked {i}, his like: {element[field]}")
                        
                        
                        for liked_element in element[field]:
                            if liked_element not in input_data:  
                                if liked_element in prediction_counts:
                                    prediction_counts[liked_element] += 1  
                                else:
                                    prediction_counts[liked_element] = 1  

        
        sorted_predictions = sorted(prediction_counts.items(), key=lambda x: x[1], reverse=True)

        
        prediction = [element for element, count in sorted_predictions]
        return prediction


            
    def __str__(self):
            fields_str = ', '.join(str(field) for field in self.fields.values())
            
            
            elements_str = '\n'.join(f'    {element}' for element in self.elements)  
            return (f'Object {self.name}: fields={{{fields_str}}}, \ncontain {len(self.elements)} elements:\n{elements_str}')  