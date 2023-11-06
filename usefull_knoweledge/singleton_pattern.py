
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Singleton:
    def __init__(self, name):
        self.name = name


# Example usage:
singleton_instance_1 = Singleton('s')
singleton_instance_2 = Singleton('w')

print(singleton_instance_1 is singleton_instance_2)  # Should print True
print(singleton_instance_1.name)
print(singleton_instance_2.name)