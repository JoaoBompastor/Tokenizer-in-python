from tokenizer_class import tokenizer, ValidTokens


def main():
    _tokenizer: tokenizer = tokenizer()
    print(_tokenizer)

    print(_tokenizer.add_token(
          ValidTokens.CHAR_TOKEN,
          ValidTokens.CHAR_TOKEN,
          ValidTokens.CHAR_TOKEN,
          ValidTokens.CHAR_TOKEN,
    ))
    print(_tokenizer)




if __name__ == "__main__":
    main()
