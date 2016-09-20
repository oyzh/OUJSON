
from Token import *
from enum import Enum
class Parse():
    def __init__(self, token):
        self.TOKEN = token.token
        self.token = token

    def parse(self):
        [current_token,_] = self.token.next_token()
        if current_token == self.TOKEN.LCURLY:
            return self.__get_object__()
        elif current_token == self.TOKEN.LSQUARE:
            return self.__get_array__()
        else:
            print "JSON error"
            exit(0)

    def __get_object__(self):
        result = {}
        [string_token,string_value] = self.token.next_token()
        while string_token == self.TOKEN.STRING:
            [colon_token,colon_value] = self.token.next_token()
            [value_token, value_value] = self.token.next_token()
            value = self.__get_value__(value_token, value_value)
            result[string_value] = value
            [judge_token,judge_value] = self.token.next_token()

            if judge_token == self.TOKEN.COMMA:
                [string_token,string_value] = self.token.next_token()
            else:
                break

        return result

    def __get_array__(self):
        result = []
        [value_token, value_value] = self.token.next_token()
        while value_token != self.TOKEN.RSQUARE:
            result.append(self.__get_value__(value_token, value_value))
            [value_token, value_value] = self.token.next_token()
            if value_token == self.TOKEN.COMMA:
                [value_token, value_value] = self.token.next_token()
        return result



    def __get_value__(self, value_token, value_value):

        if value_token == self.TOKEN.LCURLY:
            return self.__get_object__()
        elif value_token == self.TOKEN.LSQUARE:
            return self.__get_array__()
        else:
            return value_value
