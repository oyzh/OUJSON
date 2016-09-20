from enum import Enum


class Token():
    token = Enum('LCURLY','RCURLY','LSQUARE','RSQUARE','COMMA','COLON','STRING','NUMBER','TRUE','FALSE','NULL','END','ERROR')
    def __init__(self, text):
        try:
            self.text = text
            self.position = 0
            self.length = len(text)
        except e:
            print "Text Error"

    def next_token(self):
        if self.position >= self.length:
            return self.token.END,""

        current_position = self.position
        while self.text[current_position] == ' ' or self.text[current_position] == '\n' or self.text[current_position] == '\t':
            current_position = current_position + 1
            if current_position >= self.length:
                return self.token.END,""
        self.position = current_position

        current_char = self.text[self.position]
        current_value = ""
        if current_char == '{':
            current_token = self.token.LCURLY
            self.position = self.position + 1
        elif current_char == '}':
            current_token = self.token.RCURLY
            self.position = self.position + 1
        elif current_char == '[':
            current_token = self.token.LSQUARE
            self.position = self.position + 1
        elif current_char == ']':
            self.position = self.position + 1
            current_token = self.token.RSQUARE
        elif current_char == ',':
            self.position = self.position + 1
            current_token = self.token.COMMA
        elif current_char == ':':
            self.position = self.position + 1
            current_token = self.token.COLON
        elif current_char == '\"':
            current_token, current_value = self.__str_value__()
        elif current_char == 't':
            current_token, current_value = self.__true__()
        elif current_char == 'n':
            current_token, current_value = self.__null__()
        elif current_char == 'f':
            current_token, current_value = self.__false__()
        else:
            current_token, current_value = self.__num_value__()
        return current_token, current_value


    def __str_value__(self):
        current_position = self.position + 1
        current_value = ""
        while current_position < self.length:
            if self.text[current_position] == '\"':
                self.position = current_position + 1
                return self.token.STRING,current_value
            elif self.text[current_position] == '\\':

                current_value = current_value + self.text[current_position+1]
                current_position = current_position + 2
            else:
                current_value = current_value + self.text[current_position]
                current_position = current_position + 1

    def __true__(self):
        if (self.position + 4 < self.length):
            if self.text[self.position:(self.position+4)] == "true":
                self.position = self.position + 4
                return self.token.TRUE,True
            else:
                return self.token.ERROR, ""
        else:
            return self.token.ERROR, ""

    def __null__(self):
        if (self.position + 4 < self.length):
            if self.text[self.position:(self.position+4)] == "null":
                self.position = self.position + 4
                return self.token.NULL, None
            else:
                return self.token.ERROR, ""
        else:
            return self.token.ERROR, ""

    def __false__(self):
        if (self.position + 5 < self.length):
            if self.text[self.position:(self.position+5)] == "false":
                self.position = self.position + 5
                return self.token.FALSE,False
            else:
                return self.token.ERROR, ""
        else:
            return self.token.ERROR, ""

    def __num_value__(self):
        current_value = ""
        print self.text[self.position]
        while self.text[self.position] != '\t' and self.text[self.position] != ' ' and self.text[self.position] != '\n' and self.text[self.position] != ',' and self.text[self.position] != ']' and self.text[self.position] != '}':
            current_value = current_value + self.text[self.position]
            self.position = self.position + 1

        try:
            current_value = int(current_value)
        except:
            current_value = float(current_value)
        return self.token.NUMBER,current_value
