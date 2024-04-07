def split_into_chunks(list, chunk_size):
    if not list:
        return []

    chunks = []
    for i in range(0, len(list), chunk_size):
        chunk = list[i:i + chunk_size]
        chunks.append(chunk)

    return chunks
print(f"\n{'-' * 60}\n")
print("\n")
original_list = input("Enter your list of numbers separated by spaces or commas: ")
original_list = [int(x) for x in original_list.replace(',', ' ').split()]  
chunk_number = int(input("Enter your chuck number size: "))
result = split_into_chunks(original_list, chunk_number)
print("\n")
print(f"\n{'-' * 60}\n")
print("\n")
print(result)
print("\n")
print(f"\n{'-' * 60}\n")
