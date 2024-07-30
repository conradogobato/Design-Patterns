class Singleton:
    _instance = None 

    def __new__(cls, data):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.data = data
        return cls._instance
        
    def get_data(self):
        return self.data
    
    def get_instance(self, instance):
        if self.instance:
            return self.instance
        else:
            self.instance = instance

    def operation():
        print("Operation done!")

    