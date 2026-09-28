def student_info(*args, **kwargs):
    print("Positional arguments : ")
    for val in args:
        print(val)
    
    print("Keyword Arguments:")
    for [key, value] in kwargs.items():
        print(f"{key} -> {value}")
    
def create_profile(**kwargs):
    profile = {}
    for [key, value] in kwargs.items():
        profile[key] = value
    
    return profile

profile = create_profile(
    name="Puneet",
    age=21,
    skills=["Python", "C++", "React"]
)

print(profile) 