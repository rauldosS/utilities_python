# 💡 Demonstration of string templates functions
from string import Template

def main():
    # 💡 Traditional formatting using the format() method
    phrase = "You are watching {0} with {1}".format(
        "Advanced Python", "Jessica Temporal"
    )
    print(phrase)

    # 💡 Create a template with placeholders
    template = Template("You are watching ${course} with ${instructor}")

    # 💡 Use the substitute method passing named arguments
    phrase_2 = template.substitute(course="Advanced Python", instructor="Jessica Temporal")
    print(phrase_2)

    # 💡 Use the substitute method with a dictionary
    data = {"instructor": "Jessica Temporal", "course": "Advanced Python"}
    phrase_3 = template.substitute(data)
    print(phrase_3)

if __name__ == "__main__":
    main()