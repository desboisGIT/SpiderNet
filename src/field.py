class Field():
    def __init__(self, field_name, field_type):
        if not isinstance(field_name, str):
            raise TypeError(f"Expected field_name to be a string, got {type(field_name).__name__} instead.")
        if not isinstance(field_type, type):
            raise TypeError(f"Expected field_type to be a type (int, bool, dict...), got {type(field_type).__name__} instead.")
        
        self.field_name = field_name
        self.field_type = field_type

    def __str__(self):
        return f'{self.field_name}: {self.field_type.__name__}'