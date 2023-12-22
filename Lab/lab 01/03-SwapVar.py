"""SwapVar"""
def convert_string_to_tuples(text_in):
    """function"""
    values = text_in.strip('()').split(', ')
    result = tuple(map(float, values))
    print(result[::-1])
convert_string_to_tuples(input())
