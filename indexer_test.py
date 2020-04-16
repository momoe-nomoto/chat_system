import indexer_student

my_idx = indexer_student.Index('hihi')

my_idx.add_msg_and_index("what is this thing called?")

my_idx.add_msg_and_index("who knows who?")

print(my_idx.msgs)
print(my_idx.index)
print(my_idx.total_msgs)
print(my_idx.total_words)


print(my_idx.search('who'))
