from fastavro import block_reader
with open('test.avro', 'rb') as fo:
    avro_reader = block_reader(fo)
    for block in avro_reader:
        process_block(block)
