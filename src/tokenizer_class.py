from token_class import ValidTokens


class tokenizer:
    def __init__(self):
        self.tokens: list[ValidTokens] = list()
        print("tokenizer instantiated")


    def __repr__(self) -> str:
        return f"{[t for t in self.tokens]}"


    def list_tokens(self) -> list:
        """_summary_: return current array of valid tokens

        Returns:
            tuple: tuple of current valid tokens
        """
        token_buffer: list[ValidTokens] = []

        if len(self.tokens) < 1:
            return [];

        for t in self.tokens:
            token_buffer.append(t)
        return [t for t in token_buffer]


    def add_token(self, *token: ValidTokens) -> bool:
        """_summary_: adds safe tokens with minimal check

        Returns:
            bool: 
            True if succesfull adding to the array
            False if the operation cant be done
        """
        for t in token:
            if type(t) != ValidTokens:
                return False
            self.tokens.append(t)

        return True

        
    def parse_token(self) -> bool:
        return True