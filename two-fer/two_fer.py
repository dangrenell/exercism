def two_fer(name='you'):
    try:
        return f"One for {name}, one for me."
    except:
        raise Exception("Print failed")
