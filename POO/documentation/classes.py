""" 
Quick and simple description

Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with the release of 
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop 
publishing software like Aldus PageMaker including versions of Lorem Ipsum.

Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with the release of 
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop 
publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""

variable_1 = 'value 1'

class MyClass:
    """
    Normal description

    As per any other documentation you have used previously.
    """

    attribute = 1
    attribute_2 = 'value'

    def __init__(self, text):
        """
        Initialize the data

        :param text: the text from class
        :type text: str
        """
        self.text = text
        self.display_text(text)

    @staticmethod
    def display_text(text):
        """
        Method that displays 100 character text on the screen

        :param text: A text of 100 character
        :type text: str

        :return: The text of 100 character
        :rtype: str

        :raises ValueError: If the text is longer than 100 characters
        :raises TypeError:  If the text is not a string
        """

        if not isinstance(text, str):
            raise TypeError('Text need to be a string!')

        if len(text) > 100:
            raise ValueError('Text to have 100 character or less!')

        return text